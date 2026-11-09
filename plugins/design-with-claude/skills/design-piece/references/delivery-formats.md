# Delivery formats: how to build each one

## PNG preview and layered PSD (no Photoshop needed)

- Draw each element as a canvas-sized RGBA image (Pillow), one per layer.
- Composite the layers in order for the PNG preview.
- Write the PSD with `pytoshop` (`pip install pytoshop packbits`); use `raw` compression, since RLE fails in some versions.
- Ready-made helper: `scripts/build_psd.py` (takes the layer list and writes PNG + PSD).
- Fonts: Pillow opens .ttf, .otf and .woff. Free fonts can be fetched with `npm pack @fontsource/<name>` (ships .woff files).
- Letter spacing: Pillow has none; draw letter by letter adding the spacing (`tracked` in the helper).
- Extra weight: `stroke_width=1` in the text color slightly thickens thin fonts.
- Worn or textured letters: multiply the alpha channel by soft noise (`wear` in the helper).

## .jsx script (editable text in Photoshop)

Two uses:
1. On an open PSD: hide the pixel text layers and add real text layers in the same position.
2. From scratch: create the document, fills, shapes and text.

ExtendScript essentials:

```javascript
#target photoshop
app.preferences.rulerUnits = Units.PIXELS;
app.preferences.typeUnits = TypeUnits.PIXELS;
var doc = app.activeDocument; // or app.documents.add(1080, 1920, 72, "Name", NewDocumentMode.RGB)

var l = doc.artLayers.add();
l.kind = LayerKind.TEXT;
l.name = "Headline";
var t = l.textItem;
t.contents = "LINE 1\rLINE 2";          // \r = line break
try { t.font = "Marcellus-Regular"; } catch (e) {}  // PostScript name
t.size = 116;
t.tracking = -50;                        // thousandths of an em
t.useAutoLeading = false; t.leading = 100;
t.justification = Justification.LEFT;
t.position = [52, 872];                  // baseline position
```

- Text position is the baseline, not the top edge: baseline = top edge + cap height.
- Layer names written by pytoshop may end with a null character: compare with `name.replace(/\u0000/g, "")`.
- It cannot be tested without Photoshop: say it may need a small position tweak.

## Figma (official connector)

1. Ask for the file link (or create a new file) and open a connector session.
2. Photos must be in the file. Upload them with the connector's upload tool; if the workspace network blocks it, upload from the browser or ask the user to drag them into Figma.
3. Check fonts exist with `figma.listAvailableFontsAsync()` before using them.
4. Build: a 1080×1920 frame with `clipsContent`, a "Photo" rectangle with an image fill, a "Darken" rectangle with gradients, the text block in auto layout, the logo as a component plus an instance.
5. Review with a screenshot of the frame and fix only what is off.
6. Writing to the canvas is in beta: free for now, usage-based pricing later.

## Common sizes

| Piece | Size |
| --- | --- |
| Story / Reel | 1080×1920 (safe zone: 250 px top and bottom) |
| Portrait post | 1080×1350 |
| Square post | 1080×1080 |
| Reel cover in grid | 1080×1440, visible as 1080×1350 |
