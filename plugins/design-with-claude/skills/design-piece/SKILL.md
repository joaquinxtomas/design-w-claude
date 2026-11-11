---
name: design-piece
description: >
  This skill should be used whenever the user asks for a graphic piece for a brand: "design a story",
  "Instagram story", "make a post", "create a flyer", "a banner", "recreate this design with another
  photo", "make this week's stories", "variations of this piece", "deliver PNG and PSD", "PSD with
  layers"; in Spanish: "diseñá una historia", "armá una historia", "hacé un post", "armá un flyer",
  "entregá PNG y PSD". Load it before designing any such piece, instead of improvising. It takes a
  short brief, uses the brand's design system (or brand.md), designs the piece and delivers a PNG
  plus a layered PSD, a Photoshop .jsx script with editable text, or a Figma frame.
metadata:
  version: "0.7.0"
---

# Design a piece

Claude builds the base; the user decides, corrects and finishes. Golden rule: context once, short requests always.

Always reply in the user's language (the original user writes in Spanish).

## 1. Load context

- Find the brand, in this order: the brand's Design System artifact (list the user's artifacts and read its tokens, fonts, logos and README), then brand.md in the Project or connected folder. If neither exists and the brand is unclear, offer to run the brand-setup skill; if the user wants to move on anyway, work with what was given and note assumptions.
- Reuse the brand's own font files and logo assets when the design system has them; never substitute a different font silently.
- If the request names a saved style ("closed notice"), apply it as is.
- If the request asks for inspiration from one of the brand's sources (website, an account, a board), read its block in the source notes first (`../brand-setup/references/sources.md`) and only browse again if the notes are old or the user asks.
- If the request points to Instagram ("like their latest post", "for the campaign they just launched", `@brand`), take the references first following `../brand-setup/references/instagram-references.md`, then design.
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

## Use the companion plugins

When Marketing, Design, Adobe or Figma plugins/connectors are installed, use them for their part of the flow: copy in the brand's voice (Marketing), photo prep and per-channel variants (Adobe), critique before delivery (Design), native build (Figma). Match skills by purpose, never require them, and say in one line which one was used. Full flow and mapping: `references/companion-plugins.md`.

## 3. Design

- Compose on a 1080 px-wide canvas, respecting the safe zone and margins from the design system or brand.md.
- Keep text legible over photos: a darkening layer or gradient behind the text, a subtle shadow if needed.
- Use the real font when the file is available; otherwise the fallback recorded with the brand for the preview, and the real name in scripts and Figma.
- Put each element on its own clearly named layer (Photo, Darken, Headline, Subhead, Logo, Call to action).
- Check the input photo: if it is smaller than the canvas, say so and ask for the original; flag third-party logos or text visible in it.
- If the piece needs a 3D title (inflated, dripping, glossy lettering), build it with the render-3d skill and place its transparent PNG here.
- Techniques and code: see `references/delivery-formats.md` and `scripts/build_psd.py`. Rendering layers from HTML with a headless browser is also fine when it gives better typography; the deliverables stay the same.

## 4. Review before delivering

Look at the rendered preview and fix issues before showing it. Checklist in `references/review-checklist.md`: text overflowing its box, accents colliding with the line above, poor contrast, elements outside the safe zone, text that differs from the request. If a design-critique skill is available (Design plugin), run it on the preview and fix what it finds before delivering.

## 5. Deliver

Always deliver the PNG preview plus the requested format. **Whenever a PSD is delivered, also deliver the .jsx script that adds the text as real, editable text layers on top of it** (same fonts, sizes and positions), because PSD text written outside Photoshop is pixels. Do not just tell the user the text is not editable: give them the script.

| Delivery | When |
| --- | --- |
| PNG | Quick approval or direct publishing |
| Layered PSD | Adjust positions, colors or swap the photo (text comes as pixels) |
| .jsx script | Editable text in Photoshop, or producing several pieces at once |
| Figma frame | When working in Figma: everything native and editable |

Explain the .jsx in one line: open Photoshop (and the PSD if relevant) → File → Scripts → Browse → pick the file.

For Figma: ask for the file link, get the photos into the file before designing, build with auto layout, logo as a component and real text. Details in `references/delivery-formats.md`.

### Recommend better routes

When part of the result is approximate (font, 3D, photo, background), end the delivery with a short "To get closer" note: 1 or 2 concrete options from `references/tool-recommendations.md` (Illustrator Inflate, Blender connector, Firefly, Adobe Fonts, Figma…), each with what it improves and what it costs. Keep it to two lines; skip it when nothing is missing.

## 6. Iterate

- Ask for concrete notes and apply them all together ("headline 20% smaller, less darkening on the photo").
- Change only what was asked; do not rebuild the whole piece.
- Once approved, offer to save it as a named style in the brand's design system or brand.md (brand-setup skill). Mention this in one line at the end of the first delivery, too.


## Design folder

If the user keeps a design folder (see the design-folder skill), save what this skill produced there and add a line to the brand's historial.md: the delivered files in piezas/YYYY-MM_<campaign>/, an approved style in estilos/, and heavy follow-ups (3D, batches, Photoshop finishing) in pendientes-code.md.

## Batch production

For "this week's 5 stories": if the Marketing plugin is installed, use its planning or drafting skills to propose the list and the copy in the brand's voice. Confirm the text and photo for each in a table, design one first, get it approved, then produce the rest in the same style (one .jsx script that creates them all, or one frame per piece in Figma). After approval, offer per-channel versions with Adobe.

## Adobe connector (around the design)

If the Adobe connector is available, use it to prepare and multiply, not to design from scratch. See `references/adobe-connector.md`.

## Limits

- Do not generate realistic photos or complex illustrations; use brand photos, free stock or Firefly.
- Do not copy current third-party works or designs; take the idea, not the piece.
- Confidential client material: do not upload it without the user's confirmation.
