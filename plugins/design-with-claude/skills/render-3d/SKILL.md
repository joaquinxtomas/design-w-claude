---
name: render-3d
description: >
  This skill should be used when a piece needs a 3D title or lettering: "3D text", "inflated letters",
  "puffy", "bubble letters", "dripping text", "goo", "glossy 3D title", "like this 3D effect", or when a
  reference shows 3D type to imitate; in Spanish: "texto 3D", "letras infladas", "letras que chorrean",
  "gotas", "título 3D brillante", "imitá este efecto 3D". Load it before building any 3D title. It renders
  inflated letters (optional drips and a glossy rim/base) with Blender in the workspace and hands a
  transparent PNG to the design-piece skill, which assembles the PNG/PSD/.jsx.
metadata:
  version: "0.6.0"
---

# Render a 3D title

Always reply in the user's language (the original user writes in Spanish).

The method that works: **2D silhouette → inflate into a height map → 3D mesh → render.** Drawing letters and drips flat first, then inflating them, keeps the drips attached to each letter and the shapes readable. Do not extrude text and attach separate 3D drip objects: drips end up floating or offset.

## 1. Study the reference (when there is one)

- Use the best image available: the user's high-quality screenshot, or the **opened** Instagram post (never the grid thumbnail), zoomed on the title.
- Note: font feel (condensed/wide, rounded, weight), front material and color, rim/base color and thickness, number and position of drips per letter, rotation/bounce of letters, line spacing, and how much of the canvas the title takes.
- Pick the closest free font (download with `npm pack @fontsource/<name>`; convert .woff with fontTools if needed) and compare a few candidates side by side before choosing. Tell the user it is an approximation of the original font.

## 2. Configure and build the silhouette

Copy `examples/spooky_class.json`, set font, lines, drips and colors (keys documented at the top of each script). Then:

```
pip install pillow numpy scipy          # once
python3 scripts/inflate_text.py config.json
```

Look at `mask.png` before rendering. Rules that matter:

- **One weight for all letters.** `fatten` is global. If a counter closes (P, A, R, B) or a letter loses shape (K), lower `fatten` for everyone and recover presence with `width_scale` (wider glyphs), never by thinning single letters.
- **Drips:** `"auto"` places them only where the letter bottom is flat; for an exact imitation give `[x_frac, length]` per letter. The built-in drip shape is fillet → thin neck → swelling body → rounded tip; keep it.
- Leave enough `line_gap` so long drips do not land on the next line's letters (unless the reference does that).

## 3. Render

```
python3.11 -m pip install --break-system-packages bpy numpy    # once, ~300 MB (Blender as a module)
python3.11 scripts/render_inflated.py config.json preview       # ~20 s, check shapes and colors
python3.11 scripts/render_inflated.py config.json               # final, ~2-3 min on CPU
```

Tune with the preview, one change at a time: `front`/`rim_material` colors, `world` (tints reflections; keep it dark and on-palette), `height` (puffiness), `inflate_radius`. If highlights blow out, lower light power in the script, not the material color. Recipes and known limits: `references/recipes.md`.

## 4. Assemble and review

- Hand `title.png` (transparent) to the design-piece flow: crop to content, scale to the layout, add a soft dark shadow layer under it, build background and text layers, deliver PNG + PSD + .jsx.
- Make a side-by-side image (reference | result) and check it before showing: letter weight, counters open, drips natural, rim thickness, title size and position.
- Report in one line what is approximate (font, background) and the render time.

## 5. When it falls short, say what would get closer

End the delivery with 1 or 2 concrete alternatives from `../design-piece/references/tool-recommendations.md` (for 3D: Illustrator 3D and Materials > Inflate on vectors Claude prepares, the Blender connector in the desktop app, Spline, or Firefly text effects), with what each would improve.


## Design folder

If the user keeps a design folder (see the design-folder skill), save what this skill produced there and add a line to the brand's historial.md: the config that worked in 3d/<name>.json with the render, and the font file in fuentes/.

## Limits

- Works well: inflated/bubble letters, goo and drips, glossy plastic, jelly, candy, chrome-ish rims.
- Weak: gems, glass and crystal (refraction needs a different, slower setup and still looks fake), photoreal scenes. Say so up front and recommend an alternative.
- If `bpy` cannot be installed in the workspace, skip to the alternatives instead of improvising a 2D fake.
