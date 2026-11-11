---
name: design-folder
description: >
  This skill should be used whenever the user wants to create or update the design folder that holds
  every brand's context on their computer, so Claude Code can pick up the work: "create the design
  folder", "set up the folder for Claude Code", "add this to the design folder", "save this in the
  brand's folder", "new brand", "update the folder", "prepare this for Claude Code", "leave this for
  Claude Code"; in Spanish: "creá la carpeta de diseños", "armá la carpeta para Claude Code",
  "agregá esto a la carpeta", "guardalo en la carpeta de la marca", "nueva marca", "actualizá la
  carpeta", "dejalo listo para Claude Code", "dejale esto a Code". Also load it after brand-setup,
  after an approved piece or style, after new Instagram references, or when a new tool or idea is
  adopted, if a design folder exists, to keep it current.
metadata:
  version: "0.6.0"
---

# Design folder (context for Claude Code)

Always reply in the user's language (the original user writes in Spanish).

Goal: one folder on the user's computer that holds everything about each brand, kept current from the normal Claude app, so that when a job is hard (3D, batches, finishing in Photoshop) Claude Code can open the brand's folder and already know everything. Claude Code cannot read Claude Projects, chats or artifacts; this folder is the bridge.

## Structure

```
Claude Diseño/                      (name in the user's language; "Claude Design/" in English)
├── CLAUDE.md                       general working rules, all brands (templates/root-CLAUDE.md)
├── _plantillas/                    copies of the brand templates
├── <Brand>/
│   ├── CLAUDE.md                   how to work with this brand: short, imperative (templates/brand-CLAUDE.md)
│   ├── brand.md                    the brand record: colors, fonts, tone, layout rules (templates/brand.md)
│   ├── historial.md                dated log of everything added (newest first)
│   ├── pendientes-code.md          jobs left for Claude Code, with everything needed to do them
│   ├── logos/  fuentes/  fotos/
│   ├── referencias/instagram/      opened posts, full resolution, named YYYY-MM-DD_<topic>.jpg
│   ├── referencias/cliente/        briefs and examples from the client
│   ├── estilos/                    one <style>.md per approved style + <style>.png example
│   ├── 3d/                         render-3d configs (.json) that worked + their renders
│   └── piezas/YYYY-MM_<campaign>/  delivered PNG, PSD, .jsx (and Figma links in a links.md)
```

File and folder names: lowercase, hyphens, no accents in file names (brand folder names may keep the brand's spelling).

## Where to write

1. **Folder on the user's computer reachable** (desktop app with a connected folder, device file tools or a local shell, or Claude Code itself): write there directly. Ask once for the location the first time ("Documents/Claude Diseño?") and reuse it.
2. **Not reachable** (web or phone): build the same structure in the workspace, deliver it as a .zip to unzip inside the design folder, and say in one line that connecting the folder in the desktop app lets future updates land there directly.

To create it from scratch run `scripts/init_design_folder.py <root> [<Brand> ...]` (creates the tree and fills the templates), then fill brand.md and CLAUDE.md with what is known.

## Commands people use and what to do

| Request | Action |
| --- | --- |
| "Create the design folder" | Create the root with CLAUDE.md and _plantillas/. Add one folder per brand already worked on in this account or chat (from its design system, brand.md or the conversation). |
| "New brand: X" | Create `X/` from the templates. If brand-setup already ran, fill brand.md, CLAUDE.md, logos and fonts from it. |
| "Add this to the folder" / "save this in X's folder" | Classify what "this" is and file it (table below). Update historial.md. |
| "Update the folder" | Sync everything decided in the chat since the last update: brand changes, approved styles, pieces, references, tools. |
| "Leave this for Claude Code" | Add a task to pendientes-code.md with goal, inputs (paths), expected outputs, and the skill to use. |

What goes where:

| Thing | Destination | Also |
| --- | --- | --- |
| Brand fact (color, font, tone, margin) | brand.md | If it is a rule ("never…", "always…"), also CLAUDE.md |
| Approved style | estilos/<style>.md + .png | One line in CLAUDE.md "Saved styles" |
| Delivered piece | piezas/YYYY-MM_<campaign>/ | links.md for Figma frames |
| Instagram reference | referencias/instagram/ (+ a short note .md with what was learned) | Update brand.md if it changes the brand |
| 3D title that worked | 3d/<name>.json + render | Note the font file it used |
| New tool, connector or technique adopted | Root CLAUDE.md "Tools and techniques" if general; the brand's CLAUDE.md if only for that brand | |
| Idea for later | historial.md under "Ideas" | |

## Every update

- Write the change, then add a dated line to historial.md: `2026-11-10 — Saved style "BRAVA Sessions" (estilos/brava-sessions.md).`
- Keep CLAUDE.md files short (under ~60 lines): rules and pointers, details live in brand.md and estilos/.
- Never store passwords, tokens or private client data that the user did not ask to keep.
- Say in one line what was added and where.

## Handing off to Claude Code

When a job fits Claude Code better (3D render with GPU, many pieces at once, finishing PSDs in Photoshop automatically, full-resolution Instagram downloads), write it to pendientes-code.md and tell the user: open the brand's folder in Claude Code (desktop app → Code) and say "do the pending tasks". The root CLAUDE.md already tells Claude Code how to work on the user's machine.
