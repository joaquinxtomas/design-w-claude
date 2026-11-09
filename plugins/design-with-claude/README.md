# design-with-claude (plugin)

Skills:
- `brand-setup` — builds `brand.md` (logo, fonts, colors, tone, references) and saves approved styles.
- `design-piece` — designs a piece from a brief and delivers PNG, layered PSD, Photoshop `.jsx` with editable text, or a Figma frame.
- `design-from-ideas` — turns idea references into a design direction, gets approval, then designs.

Connectors (each user signs in with their own account): Figma, Adobe.

Script: `skills/design-piece/scripts/build_psd.py` (needs `pillow numpy pytoshop packbits`).

See the repository README for install and usage.
