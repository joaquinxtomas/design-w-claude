# 3D recipes and lessons learned

## Inflated cream letters on a glossy red base, with drips (tested: BRAVA "Spooky Class")

Config: `examples/spooky_class.json`. Font: Chicle (closest free match), `fatten` 12, `width_scale` 1.22, `inflate_radius` 75, rim grow 26 / offset [14, -9] / radius 40.

| Part | Setting | Why |
| --- | --- | --- |
| Front | color [0.84, 0.75, 0.63], roughness 0.32, coat 0.4, subsurface 0.15 | Ivory, soft but glossy |
| Rim/base | color [0.38, 0, 0.015], roughness 0.12, metallic 0.35, coat 1 | Deep glossy red with white glints |
| World | [0.3, 0.06, 0.07] at 0.45 | Red reflections without tinting the cream pink |
| View | Standard + Medium High Contrast | AgX made the cream salmon |

Iterations it took and what fixed each problem:

1. Extruded text + separate cylinders as drips → drips offset and floating. **Fix:** draw drips in 2D, merged into the letter, then inflate.
2. Letters merged into a blob → **Fix:** each letter is its own piece with its own rim, stacked so the rim separates neighbours.
3. Closed counters (P) and shapeless K → **Fix:** lower `fatten` for ALL letters and widen glyphs; never thin single letters (inconsistent weight is noticed immediately).
4. Drips looked like sticks with a ball → **Fix:** profile fillet → neck → swelling body → tip the same width as the body.
5. Cream looked salmon/pink → **Fix:** neutral key light, darker world, Standard view transform.
6. Terracing rings on the fronts → **Fix:** blur the height map (sigma ~3) before meshing.

## Other looks with the same scripts

- **Bubble/balloon letters, no drips:** `drips: "none"`, `inflate_radius` 90-110, front color of the brand, metallic 0.2, coat 1, no rim (`"rim": null`).
- **Candy/jelly:** front subsurface 0.4-0.6, roughness 0.1, a saturated color; rim slightly darker version of the same color.
- **Chrome-ish:** front metallic 1, roughness 0.08-0.15, light grey; needs a brighter world or more area lights to have something to reflect.

## What did not work

- **Rubies, diamonds, glass:** refraction-heavy scenes took ~30 minutes per render and still did not look like the reference. Recommend Firefly/AI generation or a real 3D artist workflow instead.
- **Low-resolution references (grid thumbnails):** not enough detail to match letter shapes or drips. Ask for a screenshot of the opened post.
