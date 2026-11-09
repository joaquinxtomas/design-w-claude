---
name: brand-setup
description: >
  This skill should be used whenever the user wants to "set up a brand", "configure a brand",
  "load a client's brand", "build a brand kit", "create a design system for a brand", "save this
  style", "save as a template", or starts working with a new client; in Spanish: "configurá la
  marca", "cargá la marca de", "armá el kit de marca", "guardá este estilo", "guardalo como
  plantilla". Load it before building any brand kit or design system for a client. It gathers logo,
  fonts, colors, tone and references, records them in the session's Design System artifact (or a
  brand.md file), and saves approved styles so later pieces take one line.
metadata:
  version: "0.2.0"
---

# Brand setup

Goal: load the brand once, so every later design request starts with full context and the user never re-uploads files or repeats rules.

Always reply in the user's language (the original user writes in Spanish).

## 1. Gather the material

Ask for anything missing in a single, plain-language message. Do not block work if something is missing: record it as pending in the brand record.

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

## 3. Record the brand

Pick where the brand lives, in this order:

1. **Design System artifact (preferred).** If the session's artifact tool lists a "Design System" type, create the brand there: color tokens (with contrast checked), font families and type styles, spacing and radius, logos as assets, and voice and tone in its README. It is visual, the user can open and edit it, and it persists across chats. Follow the type's own instructions for its files.
2. **brand.md (fallback).** If there is no Design System type, use the template in `references/brand-template.md`. Save it in the connected folder (desktop app) or hand it over for the user to upload to the brand's Claude Project.

In both cases, also keep a short "Saved styles" section (in the design system's README, or in brand.md) and the real font names plus free fallbacks for previews. Show a short summary for the user to confirm.

When proposing options (logos, font pairings), present 2 or 3 clearly labeled choices, apply one as the default, and ask the user to pick.

## 4. Suggest a Project

If the user does not work inside one Claude Project per brand, recommend it in one line: one Project per client, with the brand (design system or brand.md), logo, fonts and references, and the fixed rules in the Project instructions.

## Saving a style that worked

When the user approves a piece and asks to save it ("save this as the 'closed today' template"), add an entry to the "Saved styles" section (design system README or brand.md) with: name, purpose, key sizes and positions, fonts and sizes, photo treatment, and the minimal request that reproduces it. Next time, one line is enough.
