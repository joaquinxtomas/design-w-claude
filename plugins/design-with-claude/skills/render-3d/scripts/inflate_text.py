"""Step 1 of the inflated 3D title: build per-letter 2D silhouettes (with optional drips), then
'inflate' each one into a height map (pillow profile) plus a slightly larger rim/base shell.

Usage:  python3 inflate_text.py config.json
Writes: <out_dir>/pieces.npz and <out_dir>/mask.png (preview of the silhouette)

Requirements: pip install pillow numpy scipy
Config keys (see ../examples/spooky_class.json):
  font            path to .ttf/.otf/.woff
  lines           [{"text", "size", "drips": "auto" | [[[x_frac, len_frac], ...] per letter]}]
  fatten          px of stroke added to every glyph (same for ALL letters, keep weight consistent)
  width_scale     horizontal stretch of glyphs (1.0 = font as is)
  tracking        letter spacing as a fraction of size (negative = letters touch/overlap)
  line_gap        distance between baselines as a fraction of size
  jitter          {"rotate": deg, "y": px, "seed": n}  bouncy, hand-made feel (0 for a clean look)
  inflate_radius  px; bigger = rounder, puffier fronts
  rim             {"grow": px, "offset": [dy, dx], "radius": px} or null for no rim/base shell
  drip_style      {"scale": length multiplier}
  out_dir         folder for the outputs
"""
import json, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

cfg = json.load(open(sys.argv[1]))
FONT = cfg["font"]
FAT = int(cfg.get("fatten", 12))
WS = float(cfg.get("width_scale", 1.0))
TRACK = float(cfg.get("tracking", -0.02))
GAP = float(cfg.get("line_gap", 0.95))
JIT = cfg.get("jitter", {"rotate": 3, "y": 8, "seed": 4})
R_INF = float(cfg.get("inflate_radius", 75))
RIM = cfg.get("rim", {"grow": 26, "offset": [14, -9], "radius": 40})
DRIP_SCALE = float(cfg.get("drip_style", {}).get("scale", 0.85))
OUT = cfg["out_dir"].rstrip("/") + "/"
rng = np.random.default_rng(JIT.get("seed", 4))


def glyph(ch, size):
    """Tight binary mask of one fattened, stretched glyph, plus its baseline row inside the mask."""
    f = ImageFont.truetype(FONT, size)
    pad = FAT + 10
    tile = Image.new("L", (size * 2, size * 2), 0)
    d = ImageDraw.Draw(tile)
    d.text((size // 2, int(size * 1.4)), ch, font=f, fill=255, stroke_width=FAT, stroke_fill=255, anchor="ls")
    if WS != 1.0:
        tile = tile.resize((int(tile.width * WS), tile.height), Image.BICUBIC)
    a = np.array(tile) > 127
    ys, xs = np.nonzero(a)
    y0, y1, x0, x1 = ys.min() - pad, ys.max() + pad, xs.min() - pad, xs.max() + pad
    return a[y0:y1, x0:x1], int(size * 1.4) - y0


def drip(mask, xfrac, lfrac, cap):
    """Natural drip: wide fillet at the letter -> thin neck -> slowly swelling body -> rounded teardrop tip."""
    H, W = mask.shape
    ys, xs = np.nonzero(mask)
    x = int(xs.min() + (xs.max() - xs.min()) * xfrac)
    col = np.nonzero(mask[:, x])[0]
    if len(col) == 0:
        return np.zeros_like(mask)
    yb = col.max()
    L = lfrac * cap * DRIP_SCALE
    top, neck = cap * rng.uniform(0.20, 0.24), cap * rng.uniform(0.05, 0.06)
    end = cap * rng.uniform(0.15, 0.17) * (0.8 + 0.2 * min(lfrac / 0.6, 1))
    img = Image.new("L", (W, H), 0); d = ImageDraw.Draw(img)
    y0 = yb - cap * 0.10
    left, right = [], []
    for i in range(81):
        t = i / 80
        w = neck + (top - neck) * np.exp(-t / 0.1) + (end - neck) * (np.clip((t - 0.2) / 0.8, 0, 1) ** 1.25)
        y = y0 + t * (L + cap * 0.10)
        s = np.sin(t * 1.8) * cap * 0.008
        left.append((x - w / 2 + s, y)); right.append((x + w / 2 + s, y))
    d.polygon(left + right[::-1], fill=255)
    ex, ey = (left[-1][0] + right[-1][0]) / 2, left[-1][1]
    d.ellipse((ex - end / 2, ey - end * 0.55, ex + end / 2, ey + end * 0.62), fill=255)
    return np.array(img) > 127


def flat_bottom_spots(mask, cap):
    """x fractions where the letter's lowest edge is flat enough for a drip to hang straight down."""
    ys, xs = np.nonzero(mask)
    x0, x1 = xs.min(), xs.max()
    lowest = np.array([np.nonzero(mask[:, x])[0].max() if mask[:, x].any() else -1 for x in range(mask.shape[1])])
    ymax = lowest.max()
    good = []
    for xf in np.linspace(0.15, 0.85, 15):
        x = int(x0 + (x1 - x0) * xf); w = int(cap * 0.08)
        seg = lowest[max(x - w, 0):x + w]
        if seg.min() > ymax - cap * 0.12 and seg.max() - seg.min() < cap * 0.05:
            good.append(xf)
    return good or [0.5]


# ---- place letters line by line on a big canvas ----
lines = cfg["lines"]
CW = int(max(len(l["text"]) * l["size"] * 1.3 for l in lines)) + 600
CH = int(sum(l["size"] * GAP for l in lines) + max(l["size"] for l in lines) * 2.2)
pieces, masks = {}, []
y_base = int(max(l["size"] for l in lines) * 1.0)
for li, line in enumerate(lines):
    size = line["size"]; cap = size * 0.72
    glyphs = [glyph(ch, size) if ch != " " else None for ch in line["text"]]
    widths = [g[0].shape[1] if g else size * 0.3 for g in glyphs]
    total = sum(widths) + TRACK * size * (len(widths) - 1)
    x = (CW - total) / 2
    drips_cfg = line.get("drips", "auto")
    for k, g in enumerate(glyphs):
        if g is None:
            x += widths[k] + TRACK * size; continue
        gm, gb = g
        rot = rng.uniform(-1, 1) * JIT.get("rotate", 0)
        dy = rng.uniform(-1, 1) * JIT.get("y", 0)
        im = Image.fromarray((gm * 255).astype(np.uint8)).rotate(rot, resample=Image.BICUBIC, expand=False)
        full = np.zeros((CH, CW), bool)
        top = int(y_base + dy - gb)
        sub = np.array(im) > 127
        full[top:top + sub.shape[0], int(x):int(x) + sub.shape[1]] |= sub[:CH - top, :CW - int(x)]
        if drips_cfg == "auto":
            spots = flat_bottom_spots(full, cap)
            n = 2 if rng.random() < 0.3 and len(spots) > 3 else 1
            chosen = rng.choice(spots, size=min(n, len(spots)), replace=False)
            dl = [(float(xf), float(rng.choice([rng.uniform(0.12, 0.25), rng.uniform(0.4, 0.95)]))) for xf in chosen]
        elif drips_cfg in (None, "none"):
            dl = []
        else:
            dl = drips_cfg[k] if k < len(drips_cfg) else []
        for xf, lf in dl:
            full |= drip(full, xf, lf, cap)
        full = ndimage.gaussian_filter(full.astype(float), 7) > 0.5      # smooth union: drips flow out of the letter
        masks.append(full)
        x += widths[k] + TRACK * size
    y_base += int(size * GAP)

# ---- crop to content and inflate each letter ----
union = np.any(masks, axis=0)
ys, xs = np.nonzero(union)
pad = 140
Y0, Y1, X0, X1 = max(ys.min() - pad, 0), min(ys.max() + pad, CH), max(xs.min() - pad, 0), min(xs.max() + pad, CW)
H, W = Y1 - Y0, X1 - X0
for i, full in enumerate(masks):
    m = full[Y0:Y1, X0:X1]
    yy, xx = np.nonzero(m); p = 80
    a0, a1, b0, b1 = max(yy.min() - p, 0), min(yy.max() + p, H), max(xx.min() - p, 0), min(xx.max() + p, W)
    mc = m[a0:a1, b0:b1]
    dist = ndimage.distance_transform_edt(mc)
    h = np.sqrt(np.clip(1 - (1 - np.clip(dist / R_INF, 0, 1)) ** 2, 0, 1)) * R_INF + np.clip(dist - R_INF, 0, None) * 0.25
    pieces[f"c{i}"] = (ndimage.gaussian_filter(h, 3.2) * mc).astype(np.float32)
    if RIM:
        rc = ndimage.binary_dilation(mc, iterations=int(RIM["grow"]))
        rc = ndimage.shift(rc.astype(float), tuple(RIM["offset"]), order=0) > 0.5
        dr = ndimage.distance_transform_edt(rc); rr = float(RIM["radius"])
        hr = np.sqrt(np.clip(1 - (1 - np.clip(dr / rr, 0, 1)) ** 2, 0, 1)) * rr
        pieces[f"r{i}"] = (ndimage.gaussian_filter(hr, 2.5) * rc).astype(np.float32)
    pieces[f"o{i}"] = np.array([a0, b0], np.int32)
pieces["shape"] = np.array([H, W], np.int32); pieces["n"] = np.array([len(masks)])
np.savez_compressed(OUT + "pieces.npz", **pieces)
Image.fromarray((union[Y0:Y1, X0:X1] * 255).astype(np.uint8)).save(OUT + "mask.png")
print("letters:", len(masks), "canvas:", W, "x", H)
