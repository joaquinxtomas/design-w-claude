---
name: brand-setup
description: >
  This skill should be used when the user wants to "set up a brand", "load a client's brand",
  "build a brand kit", "save this style", "save as a template", or starts working with a new client
  (also in Spanish: "configurar una marca", "cargar la marca", "guardá este estilo"). It gathers logo,
  fonts, colors, tone and references, and writes a brand.md file that the rest of the design
  workflow uses as the single source of truth for the brand.
metadata:
  version: "0.1.0"
---

# Brand setup

Goal: load the brand once, so every later design request starts with full context and the user never re-uploads files or repeats rules.

Always reply in the user's language (the original user writes in Spanish).

## 1. Gather the material

Ask for anything missing in a single, plain-language message. Do not block work if something is missing: record it as pending in brand.md.

| Material | Ideal format | If missing |
| --- | --- | --- |
| Logo | Transparent PNG or SVG, light and dark versions | Use what exists and note the missing version |
| Fonts | .otf/.ttf file or the exact name | See "Fonts" below |
| Colors | HEX codes | Extract them from the logo or references and ask for confirmation |
| References | 3 to 5 pieces that already worked | Switch to the design-from-ideas skill |
| Photos | Real brand photos in good resolution | Use free stock (Unsplash) and say so |
| Tone | 4 or 5 lines | Propose a tone from the references and confirm it |

## 2. Analyze the references

If there are reference pieces, look at them and describe them concretely (in px on a 1080-wide canvas):

- Margins, alignment and safe zone (default: keep 250 px clear at top and bottom on stories).
- Type hierarchy: sizes, line height, letter spacing, uppercase or not.
- Photo treatment: darkening, gradients, crops.
- Logo and call-to-action placement.

## Fonts

Offer options without imposing one; the user picks how to find it:

- Use the brand's real font (file or exact name). Best option.
- Suggest fonts that fit the idea (free ones or ones the user already has).
- Adobe Fonts, if the user has Creative Cloud: the Adobe connector can search and recommend fonts.
- Identify a font from an image: Photoshop → Type → Match Font, or Adobe Fonts visual search.

If the font cannot be downloaded into the workspace (e.g. Adobe Fonts), record the real name for scripts and Figma, plus a similar free alternative for previews.

## 3. Write brand.md

Use the template in `references/brand-template.md`. Save it as a file in the brand's Claude Project (or in the working folder if there is no Project) and show a short summary for the user to confirm.

## 4. Suggest a Project

If the user does not work inside one Claude Project per brand, recommend it in one line: one Project per client, with brand.md, logo, fonts and references in its files, and the fixed rules in the Project instructions.

## Saving a style that worked

When the user approves a piece and asks to save it ("save this as the 'closed today' template"), add an entry to the "Saved styles" section of brand.md with: name, purpose, key sizes and positions, fonts and sizes, photo treatment, and the minimal request that reproduces it. Next time, one line is enough.
