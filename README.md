# Design with Claude

A Claude plugin for graphic designers: set up a brand once, ask for a piece with a short brief (or just an idea), and get it back editable in Photoshop or Figma.

Built for social media work (Instagram stories, posts, flyers), but it works for any graphic piece.

## Install (2 minutes)

You need a paid Claude plan (Pro, Max, Team or Enterprise).

1. Open Claude (web or desktop app) and go to **Customize → Plugins**.
2. Click **Add marketplace** and paste: `joaquinxtomas/design-w-claude`
3. Find **design-with-claude** in the list and click **Install**.
4. Optional but recommended: in **Settings → Connectors**, connect **Figma** and **Adobe** and sign in with your own accounts.

Turn on **Sync automatically** on the marketplace so updates arrive on their own.

## Recommended companion plugins

This plugin is the glue; these do specialized parts and it uses them automatically when they are installed (none is required):

| Plugin | Where | What it adds to the flow |
| --- | --- | --- |
| **Marketing** (Anthropic) | Customize → Plugins → Discover | Copy in the brand's voice, campaign and weekly planning |
| **Design** (Anthropic) | Customize → Plugins → Discover | Critique of the piece before delivery (hierarchy, contrast) |
| **Adobe for creativity** | Customize → Plugins → Discover (or the Adobe connector) | Photo prep, licensed fonts, per-channel versions |
| **Figma** | Settings → Connectors | Build pieces natively in your Figma file |

### How it all fits

Brand (design system + voice) → plan the week (Marketing) → copy (Marketing) → photos (Adobe) → design (this plugin) → critique (Design) → PNG + PSD + .jsx or Figma → other formats (Adobe) → save the style.

## Use

Just talk to Claude. The right skill kicks in on its own, or type `/` to pick one.

| Say something like | What happens |
| --- | --- |
| "Set up the brand for Café Lumbre" + logo, colors, fonts, references | Builds the brand's design system (colors, fonts, logos, voice) inside Claude |
| "Design a story: text 'OPEN LATE TODAY', photo attached, deliver PNG + PSD" | Designs, reviews and delivers PNG + layered PSD + a `.jsx` that makes the text editable |
| "Headline smaller, less darkening on the photo" | Applies only those changes |
| "Save this as the 'opening hours' style" | Next time one line is enough |
| "I want a story inspired by 70s movie posters" | Proposes a design direction first, then designs |

Tips:
- Create one Claude **Project per client**.
- To force a skill, start your message with it: `/design-with-claude:brand-setup`, `/design-with-claude:design-piece` or `/design-with-claude:design-from-ideas` (type `/` and pick it from the list).

## What's inside

| Skill | Purpose |
| --- | --- |
| `brand-setup` | Brand kit as a Design System artifact (or `brand.md`): logo, fonts, colors, tone, saved styles |
| `design-piece` | From brief to piece: PNG, layered PSD, Photoshop `.jsx` with editable text, or Figma frame |
| `design-from-ideas` | No exact reference: turns textures, eras, artists or feelings into a design direction |

Connectors: Figma (design directly in a Figma file) and Adobe (prepare photos, find fonts, resize for each channel).

---

## Guía en español

Este plugin te ayuda a diseñar piezas para tus marcas (historias, posts, flyers) con Claude: cargás la marca una vez, pedís la pieza con pocas palabras y la recibís lista para terminar en Photoshop o Figma.

### 1. Instalar el plugin (una sola vez)

Necesitás un plan pago de Claude (Pro, Max, Team o Enterprise).

1. En Claude (web o app de escritorio), andá a **Personalizar → Plugins**.
2. Tocá **Add marketplace** y pegá: `joaquinxtomas/design-w-claude`
3. Buscá **design-with-claude** y tocá **Instalar**.
4. En ese mismo marketplace, activá **Sync automatically** para que las mejoras te lleguen solas.

### 2. Instalar los plugins que lo complementan (recomendado)

El plugin funciona solo, pero **solo usa estas herramientas si las tenés instaladas**. Sin ellas, Claude hace esos pasos por su cuenta, con menos precisión.

| Instalá | Dónde | Qué suma |
| --- | --- | --- |
| **Marketing** | Personalizar → Plugins → Discover | Escribe los textos con la voz de cada marca y planifica la semana de piezas |
| **Design** | Personalizar → Plugins → Discover | Revisa la pieza antes de entregarla (jerarquía, contraste, legibilidad) |
| **Adobe for creativity** | Personalizar → Plugins → Discover | Prepara fotos (color parejo, fondos, pasar a vertical), busca fuentes y genera las versiones para cada red |
| **Figma** | Configuración → Conectores | Arma las piezas directo en tu archivo de Figma |

Para Adobe y Figma, la primera vez te pide iniciar sesión con tu cuenta.

### 3. Cómo usarlo

Trabajá con un **Proyecto de Claude por cliente** y hablale normal:

| Escribí algo como | Qué pasa |
| --- | --- |
| "Configurá la marca de [cliente]" + logo, colores, tipografías o aunque sea una foto | Arma el sistema de diseño de la marca (colores, letras, logo, tono) y lo guarda en Claude |
| "Diseñá una historia: 'HOY ABRIMOS TARDE', foto adjunta" | Diseña y te entrega PNG, PSD y el script para Photoshop |
| "Armame las 3 historias de la semana: lunes…, miércoles…, viernes…" | Te propone los textos, espera tu OK, hace una, y cuando la aprobás hace el resto |
| "Título más chico, oscurecé menos la foto" | Cambia solo eso |
| "Guardá esto como estilo 'aviso de horario'" | La próxima vez alcanza con una línea: "aviso de horario, abrimos a las 12" |
| "Quiero una historia inspirada en [una idea, textura, época o artista]" | Primero te propone una dirección de diseño; cuando la aprobás, diseña |

Si querés asegurarte de que use el plugin, empezá el mensaje con `/design-with-claude:design-piece` (o `:brand-setup`, `:design-from-ideas`). Escribí `/` y elegilo de la lista.

### 4. Qué archivos recibís

- **PNG**: la pieza terminada, lista para publicar.
- **PSD**: el archivo de Photoshop con cada elemento en su capa y con nombre (Foto, Título, Logo…). Ojo: acá **los textos vienen como imagen**.
- **Script `.jsx`**: convierte esos textos en **texto editable de verdad** (con la misma letra, tamaño y posición).
- **Tipografías** (si hacen falta): los archivos de las fuentes para instalar.

### 5. Terminar la pieza en Photoshop (con el `.jsx`)

1. **Instalá las tipografías** (una sola vez por marca): doble clic en cada archivo `.ttf` u `.otf` → **Instalar**. Si la fuente es de Adobe Fonts, activala desde Creative Cloud. Después cerrá y abrí Photoshop.
2. **Poné todo en una carpeta**: los PSD, el `.jsx` y, si vino un `.zip`, descomprimilo ahí mismo.
3. **Ejecutá el script**: en Photoshop, **Archivo → Secuencias de comandos → Explorar** (en inglés: *File → Scripts → Browse*), elegí el `.jsx` y, si te lo pide, la carpeta con los PSD.
4. **Abrí las copias nuevas**: el script guarda cada PSD con **"_editable"** en el nombre. Ahí los textos tienen el ícono **T** en el panel de capas y se editan con doble clic. Las versiones en imagen quedan ocultas.
5. **Ajustá lo fino**: el script no se puede probar fuera de Photoshop, así que algún texto puede quedar corrido unos píxeles. Movelo a mano.
6. **Retocá lo que quieras**: cambiá la foto (colocá la nueva y usala como máscara de recorte sobre la capa "Foto"), colores, sombras.
7. **Exportá**: **Archivo → Exportar → Exportar como** → PNG o JPG, 1080×1920, sRGB.
8. **Publicá** y poné los stickers de Instagram (link, recordatorio) en el espacio que la historia deja libre.
9. **Contale a Claude lo que cambiaste** ("subí el título 40 px", "oscurecí la foto"): así actualiza el estilo guardado y la próxima pieza ya sale como la terminaste.

**Si el script da un error**, copiá el mensaje (o sacale una foto) y pasáselo a Claude en el mismo chat. Lo más común es que falte instalar una tipografía.

## Changelog

- **0.3.2** — Full Spanish guide: install, companion plugins (and that they are only used when installed), how to use, what files you get, and the step-by-step Photoshop flow with the `.jsx` for editable text.
- **0.3.1** — Fix: `build_psd.py` wrote PSDs with width and height swapped (1920×1080); they are now 1080×1920. Regenerate PSDs made with earlier versions.
- **0.3.0** — Works together with the Marketing, Design and Adobe plugins and the Figma connector when installed: copy in the brand's voice, photo prep, critique before delivery, per-channel variants, and a joined-up flow from brand to saved style. Companion plugins are optional.
- **0.2.0** — Brand kit lives in Claude's Design System artifact when available (brand.md as fallback); `design-piece` reads fonts and logos from it, always ships the `.jsx` for editable text with a PSD, and flags low-resolution or third-party content in photos; stronger skill triggers (English and Spanish).
- **0.1.0** — First version: brand setup, piece design (PNG/PSD/jsx/Figma), design from ideas, Figma and Adobe connectors.

## License

MIT
