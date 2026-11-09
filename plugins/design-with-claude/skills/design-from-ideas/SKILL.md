---
name: design-from-ideas
description: >
  This skill should be used when there is no exact reference piece and the user describes an idea:
  "I want this texture", "something inspired by…", "70s look", "it should feel like…",
  "a typeface inspired by…", "no reference, but it should convey…" (also in Spanish: "quiero esta
  textura", "inspirado en…"). It turns ideas (textures, materials, eras, artists, feelings) into a
  concrete design direction, gets it approved, and only then designs with the design-piece skill.
metadata:
  version: "0.1.0"
---

# Design from ideas

When there is no similar piece to copy, design from ideas and turn them into concrete decisions. Propose the direction in writing before designing: it is cheap and avoids redoing work.

Always reply in the user's language (the original user writes in Spanish).

## 1. Understand the ideas

Accept as idea references:
- Textures and materials (plaster, kraft paper, marble, fabric, neon).
- Eras or movements (Renaissance, Bauhaus, 70s posters).
- Artists or works ("Michelangelo's frescoes").
- Mood photos or palettes.
- Words or feelings ("silence", "neighborhood party").

For each image, ask or infer what to take and what not to ("from this photo only the texture, not the colors"). If the idea is an artist or a work, identify the specific works and explain each in one line.

## 2. Propose a written direction

Present a short "Idea → Design decision" table covering:

| Aspect | What to define |
| --- | --- |
| Type | Family and why it comes from the idea (e.g. Roman capitals on the Sistine Chapel plaques → Cinzel) |
| Palette | 3 to 5 HEX colors and where they come from |
| Texture | Material or treatment (plaster, grain, paper) |
| Layout | Structure and hierarchy (central arch, plaque, margins) |
| Elements | Graphic devices (cornices, frames, stamps) |

Wait for approval or corrections. If the user prefers options, propose 2 or 3 different directions in a few lines each.

See `references/example-michelangelo.md` for a complete case.

## 3. Sketch

- With the direction approved, make 2 or 3 different sketches only if the user asked for them; otherwise one.
- If available, lean on Anthropic's skills: theme-factory (palette + font pairing), canvas-design (exploratory pieces), algorithmic-art (original textures and backgrounds).
- Generate textures with code (noise, cracks, grain) instead of copying other people's images.

## 4. Design and deliver

Hand over to the design-piece skill with the direction as the style, to build, review and deliver in the requested format.

## 5. Save the direction

If the user approves the result, offer to save it as a named style in brand.md ("fresco style") using the brand-setup skill.

## Limits

- Drawing inspiration from old, public-domain works is free.
- With current artists, brands or designs: take the idea, do not reproduce the work or its recognizable elements.
- Do not use photos of real public figures in pieces.
