---
name: design-piece
description: >
  This skill should be used when the user asks to "design a story", "make a post", "create a flyer",
  "an Instagram piece", "recreate this design with another photo", "make this week's stories",
  "variations of this piece", or any brand graphic design request (also in Spanish: "diseñá una
  historia", "hacé un post", "armá un flyer"). It takes a short brief, uses brand.md, designs the
  piece and delivers it as a PNG, a layered PSD, a Photoshop .jsx script with editable text, or a
  Figma frame.
metadata:
  version: "0.1.0"
---

# Design a piece

Claude builds the base; the user decides, corrects and finishes. Golden rule: context once, short requests always.

Always reply in the user's language (the original user writes in Spanish).

## 1. Load context

- Look for brand.md in the Project or working folder. If it does not exist and the brand is unclear, offer to run the brand-setup skill; if the user wants to move on anyway, work with what was given and note assumptions.
- If the request names a saved style ("closed notice"), apply it as is.
- Never ask the user to re-upload what is already in the Project.

## 2. Complete the brief

Make sure these are known. Ask only for what is missing and changes the result, in a single question:

```
Goal: what the piece communicates
Exact text: headline / subhead / call to action (verbatim when in quotes)
Image: attached photo, brand photo or free stock
Style: reference or saved style
Format: story 1080×1920 (default), post 1080×1350, other
Delivery: PNG + PSD (default), .jsx script, Figma
```

Keep quoted text exactly as written. If there is no reference or style and the request is an idea ("I want this texture", "inspired by…"), switch to the design-from-ideas skill.

## 3. Design

- Compose on a 1080 px-wide canvas, respecting the safe zone and margins from brand.md.
- Keep text legible over photos: a darkening layer or gradient behind the text, a subtle shadow if needed.
- Use the real font when the file is available; otherwise the fallback from brand.md for the preview, and the real name in scripts and Figma.
- Put each element on its own clearly named layer (Photo, Darken, Headline, Subhead, Logo, Call to action).
- Techniques and code: see `references/delivery-formats.md` and `scripts/build_psd.py`.

## 4. Review before delivering

Look at the rendered preview and fix issues before showing it. Checklist in `references/review-checklist.md`: text overflowing its box, accents colliding with the line above, poor contrast, elements outside the safe zone, text that differs from the request.

## 5. Deliver

Always deliver the PNG preview plus the requested format:

| Delivery | When |
| --- | --- |
| PNG | Quick approval or direct publishing |
| Layered PSD | Adjust positions, colors or swap the photo (text comes as pixels) |
| .jsx script | Editable text in Photoshop, or producing several pieces at once |
| Figma frame | When working in Figma: everything native and editable |

Explain the .jsx in one line: open Photoshop (and the PSD if relevant) → File → Scripts → Browse → pick the file.

For Figma: ask for the file link, get the photos into the file before designing, build with auto layout, logo as a component and real text. Details in `references/delivery-formats.md`.

## 6. Iterate

- Ask for concrete notes and apply them all together ("headline 20% smaller, less darkening on the photo").
- Change only what was asked; do not rebuild the whole piece.
- Once approved, offer to save it as a style in brand.md (brand-setup skill).

## Batch production

For "this week's 5 stories": confirm the text and photo for each in a table, design one first, get it approved, then produce the rest in the same style (one .jsx script that creates them all, or one frame per piece in Figma).

## Adobe connector (around the design)

If the Adobe connector is available, use it to prepare and multiply, not to design from scratch. See `references/adobe-connector.md`.

## Limits

- Do not generate realistic photos or complex illustrations; use brand photos, free stock or Firefly.
- Do not copy current third-party works or designs; take the idea, not the piece.
- Confidential client material: do not upload it without the user's confirmation.
