# Recommending better routes

After delivering, if part of the result is approximate or limited, add a short "To get closer" note: 1 or 2 options, each with what it improves, what it needs, and its cost. Recommend only what fits the gap; never more than two; do not repeat a recommendation the user already declined. Phrase it as an option, not homework.

| Gap in the result | Recommend | What it needs | Cost |
| --- | --- | --- | --- |
| 3D lettering not close enough / needs to stay editable | **Illustrator → Effect → 3D and Materials → Inflate** (or Extrude) on the vector letters and drips Claude prepares (SVG); lower Roughness and raise Metallic for a glossy liquid look; render with ray tracing | Illustrator (in Creative Cloud) | Included |
| 3D scene the user wants to tweak by hand (lights, materials, camera) | **Blender connector** (official, by Blender Lab) in the Claude desktop app, with Blender open | Claude desktop app + Blender (free) | Free |
| Simpler, designer-friendly 3D (objects, shapes, text) | **Spline** connector | Spline account | Check Spline plan |
| Texture-styled title fast ("melted chocolate", "neon", "slime") | **Adobe Express → Generate text effects** (Firefly) | Adobe account | Generative credits (Creative Cloud includes a monthly allowance) |
| Photoreal image, background or object (gems, food, scenes) | **Photoshop → Generate Image / Generative Fill**, or the **Firefly** app; bring the result back to Claude to assemble | Creative Cloud | Generative credits |
| Exact brand font missing | The brand's font file, **Adobe Fonts** (activate from Creative Cloud), or Photoshop **Type → Match Font** to identify it | Creative Cloud for Adobe Fonts | Included |
| Low-resolution photo | The original file from the client, or Photoshop **Super Resolution** / Firefly upscale | Creative Cloud | Included / credits |
| Text in the PSD is not editable | The `.jsx` script (always delivered); later, Adobe's local MCP for Photoshop (private beta announced for early 2027) | Photoshop | Included |
| Needs native, editable layout | Build it in **Figma** with the connector | Figma account | Free tier works |

Notes:
- The Adobe connector in Claude edits images but does not generate them from text; generation happens in Photoshop/Firefly and the result is handed back.
- Higgsfield and similar generators need their own paid plan; mention them only if the user asks for video or heavy AI generation.
