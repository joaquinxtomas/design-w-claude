"""Helpers to build layered design pieces and save them as PNG + PSD.

Typical use (import from another script):

    import sys; sys.path.insert(0, "<folder of this file>")
    from build_psd import canvas, tracked, centered_text, darken, wear, save

    layers = [("Photo", photo_rgba), ("Darken", darken(1080, 1920)), ("Headline", headline_layer)]
    save(layers, "piece_preview.png", "piece.psd")

Requirements: pip install pillow numpy pytoshop packbits
Each layer is a canvas-sized RGBA image; list order is bottom to top.
"""
import numpy as np
from PIL import Image, ImageDraw


def canvas(w=1080, h=1920):
    """Transparent layer the size of the piece."""
    return Image.new("RGBA", (w, h), (0, 0, 0, 0))


def tracked(draw, x, y, text, font, color, spacing=0, stroke=0):
    """Draw text letter by letter with extra spacing (px). Returns the final x."""
    for ch in text:
        draw.text((x, y), ch, font=font, fill=color, stroke_width=stroke, stroke_fill=color)
        x += draw.textlength(ch, font=font) + spacing
    return x


def tracked_width(draw, text, font, spacing=0):
    return sum(draw.textlength(c, font=font) for c in text) + spacing * (len(text) - 1)


def centered_text(draw, canvas_width, y, text, font, color, spacing=0):
    x = (canvas_width - tracked_width(draw, text, font, spacing)) / 2
    return tracked(draw, x, y, text, font, color, spacing)


def darken(w, h, color=(28, 18, 12), base=0.30, center_y=None, strength=0.30, band=420, left=0.18):
    """Dark veil with a denser band behind the text and extra darkening on the left."""
    center_y = h / 2 if center_y is None else center_y
    y = np.arange(h)[:, None]
    x = np.arange(w)[None, :]
    a = base + np.exp(-((y - center_y) / band) ** 2) * strength + np.clip(1 - x / (w * 0.95), 0, 1) ** 1.2 * left
    arr = np.zeros((h, w, 4), np.uint8)
    arr[..., :3] = color
    arr[..., 3] = (np.clip(a, 0, 0.85) * 255).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")


def noise(w, h, scale=40, seed=0):
    r = np.random.default_rng(seed)
    small = r.random((max(2, h // scale), max(2, w // scale)))
    return np.asarray(Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC), float) / 255


def wear(layer, amount=0.4, seed=42):
    """Wear the alpha channel with noise (old paint, stamp, fresco look)."""
    a = np.array(layer).astype(float)
    w, h = layer.size
    n = sum(noise(w, h, s, seed + i) * p for i, (s, p) in enumerate([(120, .5), (30, .3), (6, .2)]))
    a[..., 3] *= (1 - amount) + amount * np.clip((n - 0.18) * 4, 0, 1)
    return Image.fromarray(a.astype(np.uint8), "RGBA")


def save(layers, png_out, psd_out=None):
    """layers: list of (name, RGBA image), bottom to top."""
    w, h = layers[0][1].size
    preview = Image.new("RGBA", (w, h))
    for _, im in layers:
        preview.alpha_composite(im)
    preview.convert("RGB").save(png_out)
    if psd_out:
        from pytoshop import enums
        from pytoshop.user import nested_layers as nl
        psd_layers = []
        for name, im in reversed(layers):
            a = np.array(im)
            ys, xs = np.nonzero(a[..., 3])
            if len(xs) == 0:
                continue
            t, b, l, r = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
            c = a[t:b, l:r]
            psd_layers.append(nl.Image(name=name, top=int(t), left=int(l),
                                       channels={0: c[..., 0], 1: c[..., 1], 2: c[..., 2], -1: c[..., 3]}))
        psd = nl.nested_layers_to_psd(psd_layers, color_mode=enums.ColorMode.rgb, size=(h, w),
                                      compression=enums.Compression.raw)
        with open(psd_out, "wb") as fh:
            psd.write(fh)
    return preview
