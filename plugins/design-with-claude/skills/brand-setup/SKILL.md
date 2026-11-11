---
name: brand-setup
description: >
  This skill should be used whenever the user wants to "set up a brand", "configure a brand",
  "load a client's brand", "build a brand kit", "create a design system for a brand", "save this
  style", "save as a template", "take references from Instagram", "use @brand's Instagram", "get the
  design of their latest post", or starts working with a new client; in Spanish: "configurá la
  marca", "cargá la marca de", "armá el kit de marca", "guardá este estilo", "guardalo como
  plantilla", "tomá referencias del Instagram de", "sacá el diseño de la última publicación". Load it before building any brand kit or design system for a client. It gathers logo,
  fonts, colors, tone and references, records them in the session's Design System artifact (or a
  brand.md file), and saves approved styles so later pieces take one line.
metadata:
  version: "0.7.0"
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
| References | 3 to 5 pieces that already worked, or the brand's website and social accounts | Switch to the design-from-ideas skill |
| Links | Website, social accounts, brand manual, inspiration accounts | Ask once; record what exists |
| Photos | Real brand photos in good resolution | Use free stock (Unsplash) and say so |
| Tone | 4 or 5 lines | Propose a tone from the references and confirm it |

## References from Instagram

If the user gives an Instagram account or post (`@brand`, a link) or asks for the design of the brand's latest post, read `references/instagram-references.md` and follow it: browser with the user's own session, read-only and at a normal pace, skip pinned posts, highlights for stories, and screenshots as the fallback. Record what it finds as approximate and ask for the real files.

## Sources: website, social accounts and inspiration

Keep every link of the brand together and learn from each one only once. Read `references/sources.md` and follow it:

- **Sources list** in the Design System README (and brand.md, for Claude Code), split into brand (authoritative) and inspiration.
- **Source notes** in `fuentes.md`: what each link taught (exact fonts and colors from the website's code, design rules, tone, campaigns), with the date checked. Use the notes before browsing again; recheck only when they are old, the user asks, or the task is about something new.
- **Websites:** read text and code for exact font names, HEX colors and the SVG logo. Web font files are for the web only: record the name, do not design with the file.

## Companion plugins

- **Marketing installed:** use its brand-voice skill to write the voice and tone section (and its guidelines file if it creates one), so copy and design share one voice.
- **Adobe installed:** use it to suggest licensed fonts and to clean up the logo or reference photos.
- **Theme-factory available:** use it to propose palette and font pairings when the brand has none.

Match skills by purpose, never require them, and see `../design-piece/references/companion-plugins.md` for the full flow.

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

In both cases, also keep a "Sources" section (links, see above) and a short "Saved styles" section (in the design system's README, or in brand.md) and the real font names plus free fallbacks for previews. Show a short summary for the user to confirm.

When proposing options (logos, font pairings), present 2 or 3 clearly labeled choices, apply one as the default, and ask the user to pick.


## Design folder

If the user keeps a design folder (see the design-folder skill), save what this skill produced there and add a line to the brand's historial.md: brand.md, CLAUDE.md, logos and fonts in the brand's folder; a new brand gets its folder created.

## 4. Suggest a Project

If the user does not work inside one Claude Project per brand, recommend it in one line: one Project per client, with the brand (design system or brand.md), logo, fonts and references, and the fixed rules in the Project instructions.

## Saving a style that worked

When the user approves a piece and asks to save it ("save this as the 'closed today' template"), add an entry to the "Saved styles" section (design system README or brand.md) with: name, purpose, key sizes and positions, fonts and sizes, photo treatment, and the minimal request that reproduces it. Next time, one line is enough.
