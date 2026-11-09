# Design with Claude

A Claude plugin for graphic designers: set up a brand once, ask for a piece with a short brief (or just an idea), and get it back editable in Photoshop or Figma.

Built for social media work (Instagram stories, posts, flyers), but it works for any graphic piece.

## Install (2 minutes)

You need a paid Claude plan (Pro, Max, Team or Enterprise).

1. Open Claude (web or desktop app) and go to **Customize → Plugins**.
2. Click **Add marketplace** and paste: `joaquinxtomas/design-w-claude`
3. Find **design-with-claude** in the list and click **Install**.
4. Optional but recommended: in **Settings → Connectors**, connect **Figma** and **Adobe** and sign in with your own accounts.

Updates arrive automatically when this repository changes.

## Use

Just talk to Claude. The right skill kicks in on its own, or type `/` to pick one.

| Say something like | What happens |
| --- | --- |
| "Set up the brand for Café Lumbre" + logo, colors, fonts, references | Creates a `brand.md` with everything about the brand |
| "Design a story: text 'OPEN LATE TODAY', photo attached, deliver PNG + PSD" | Designs, reviews and delivers the piece |
| "Headline smaller, less darkening on the photo" | Applies only those changes |
| "Save this as the 'opening hours' style" | Next time one line is enough |
| "I want a story inspired by 70s movie posters" | Proposes a design direction first, then designs |

Tip: create one Claude **Project per client** and keep `brand.md`, the logo and fonts in its files.

## What's inside

| Skill | Purpose |
| --- | --- |
| `brand-setup` | Brand kit (logo, fonts, colors, tone, references) and saved styles |
| `design-piece` | From brief to piece: PNG, layered PSD, Photoshop `.jsx` with editable text, or Figma frame |
| `design-from-ideas` | No exact reference: turns textures, eras, artists or feelings into a design direction |

Connectors: Figma (design directly in a Figma file) and Adobe (prepare photos, find fonts, resize for each channel).

---

## Guía rápida en español

1. En Claude (web o app de escritorio), andá a **Personalizar → Plugins**.
2. Tocá **Add marketplace** y pegá: `joaquinxtomas/design-w-claude`
3. Buscá **design-with-claude** y tocá **Instalar**.
4. Recomendado: en **Configuración → Conectores**, conectá **Figma** y **Adobe** con tus cuentas.

Después, hablale normal y en español: "configurá la marca de [cliente]", "diseñá una historia con este texto y esta foto", "quiero una historia inspirada en…". Las actualizaciones llegan solas.

## License

MIT
