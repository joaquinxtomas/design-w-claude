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

### Claude Code (installed separately)

Plugins installed in the Claude app are **not** shared with Claude Code; install it there too. Inside a Claude Code session (desktop app → **Code**, or the terminal):

```
/plugin marketplace add joaquinxtomas/design-w-claude
/plugin install design-with-claude@design-with-claude
/reload-plugins
```

Update later with `/plugin marketplace update design-with-claude`. For Instagram references in Claude Code, install the **Claude in Chrome** extension and start with `claude --chrome` (or run `/chrome` in a session). Claude Code cannot read Claude Projects or chats: keep each brand's context in the design folder (see the design-folder skill).

## Recommended companion plugins

This plugin is the glue; these do specialized parts and it uses them automatically when they are installed (none is required):

| Plugin | Where | What it adds to the flow |
| --- | --- | --- |
| **Marketing** (Anthropic) | Customize → Plugins → Discover | Copy in the brand's voice, campaign and weekly planning |
| **Design** (Anthropic) | Customize → Plugins → Discover | Critique of the piece before delivery (hierarchy, contrast) |
| **Adobe** | Customize → Plugins → Discover (or the Adobe connector) | Photo prep, licensed fonts, per-channel versions |
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
| "Take the brand info from cafelumbre.com" / "add their TikTok" | Reads exact fonts, colors and logo from the website's code, adds every link to the brand's sources, and saves what it learned so it does not search again |
| "Set up the brand from @cafelumbre's Instagram" | Looks at the profile, latest posts and highlights in your browser and builds the brand from them |
| "Take the design of @cafelumbre's latest post and make a story for the campaign" | Skips pinned posts, reads the latest one and designs in that style |
| "Make the title 3D: inflated cream letters with drips, like this reference" | Renders the 3D title with Blender in the workspace and builds the piece around it |
| "Create the design folder" / "add this to the design folder" / "leave this for Claude Code" | Keeps one folder per brand on your computer (rules, brand record, styles, references, pieces, pending jobs) that Claude Code can open for the heavy work |

Tip: create one Claude **Project per client**. When something in a delivery is approximate (font, 3D, photo), Claude ends with one or two concrete ways to get closer (Adobe Fonts, Illustrator 3D and Materials, Firefly…).

**Claude or Claude Code?** Use the Claude app day to day (brands, references, pieces, Figma). Use Claude Code (desktop app → Code) for heavy work on your computer: faster 3D with your GPU, your installed fonts, running the `.jsx` in Photoshop, big batches. Claude Code reads the design folder, not your Projects or chats.

### References from Instagram

Needs the Claude desktop app with a browser (built-in browser or Claude in Chrome) where you are signed in to Instagram. Claude only looks: no likes, follows or messages, a handful of posts at a normal pace, and it stops if Instagram shows any warning. Opening highlights shows the brand that your account viewed them. Colors and fonts from screenshots are approximate, so share the real files when you have them. No browser? Send 3–5 screenshots instead.

## Commands

Skills usually start on their own. To make sure one runs, start your message with its command (type `/` and pick it from the list).

| Command | What it does | Example |
| --- | --- | --- |
| `/design-with-claude:brand-setup` | Sets up a brand (colors, fonts, logo, tone) as a design system in Claude, from files or from its Instagram, or saves an approved style | `/design-with-claude:brand-setup Set up the brand for "Raíz", a neighborhood flower shop. Use @raiz.flores on Instagram.` |
| `/design-with-claude:design-piece` | Designs a piece from a short brief and delivers PNG + layered PSD + `.jsx` (editable text), or builds it in Figma | `/design-with-claude:design-piece Story for Raíz: "PEONIES ARE HERE". Use the attached photo.` |
| `/design-with-claude:design-folder` | Creates and updates the design folder: one folder per brand with CLAUDE.md, brand.md, styles, references, pieces and jobs for Claude Code | `/design-with-claude:design-folder Create the design folder in Documents and add BRAVA.` |
| `/design-with-claude:render-3d` | Renders a 3D title (inflated letters, drips, glossy rim) as a transparent PNG for the piece | `/design-with-claude:render-3d "SPOOKY CLASS", cream letters with drips on a glossy red base, like the attached post.` |
| `/design-with-claude:design-from-ideas` | No reference? Turns an idea (texture, era, artist, feeling) into a design direction, gets your OK, then designs | `/design-with-claude:design-from-ideas A story inspired by 70s movie posters for the summer sale.` |

Useful commands from the companion **Marketing** plugin (if installed):

| Command | What it does | Example |
| --- | --- | --- |
| `/marketing:campaign-plan` | Plans a campaign or a week of content | `/marketing:campaign-plan Launch week for the first drop on 11/11.` |
| `/marketing:draft-content` | Writes copy for a piece in the brand's voice | `/marketing:draft-content Copy for 3 stories announcing the drop.` |
| `/marketing:brand-review` | Checks copy against the brand voice | `/marketing:brand-review Review these 3 headlines.` |

## What's inside

| Skill | Purpose |
| --- | --- |
| `brand-setup` | Brand kit as a Design System artifact (or `brand.md`): logo, fonts, colors, tone, links and source notes, saved styles; from files, the website or Instagram |
| `design-piece` | From brief to piece: PNG, layered PSD, Photoshop `.jsx` with editable text, or Figma frame |
| `design-from-ideas` | No exact reference: turns textures, eras, artists or feelings into a design direction |
| `render-3d` | Inflated 3D titles (drips, glossy rim) rendered with Blender, as a transparent PNG layer |
| `design-folder` | One folder per brand on your computer (rules, brand record, sources, styles, pieces, pending jobs) so Claude Code has the full context |

Connectors: Figma (design directly in a Figma file) and Adobe (prepare photos, find fonts, resize for each channel).

---

## Guía en español

Este plugin te ayuda a diseñar piezas para tus marcas (historias, posts, flyers) con Claude: cargás la marca una vez, pedís la pieza con pocas palabras y la recibís lista para terminar en Photoshop o Figma. Vos dirigís y terminás; Claude hace lo repetitivo.

### Empezá por acá (lo básico)

1. Instalá el plugin (paso 1).
2. Configurá una marca: "Configurá la marca de [cliente]" + su web o su Instagram, y si tenés, logo y tipografías.
3. Pedí una pieza: "Diseñá una historia: 'HOY ABRIMOS TARDE', foto adjunta".
4. Abrí el PSD, corré el `.jsx` y terminala en Photoshop (paso 5).

Con eso ya ahorrás tiempo. Lo demás (carpeta de diseños, 3D, Claude Code) es para cuando quieras ir más lejos.

### 1. Instalar el plugin (una sola vez)

Necesitás un plan pago de Claude (Pro, Max, Team o Enterprise).

**En la app de Claude (web o escritorio):**

1. Andá a **Personalizar → Plugins**.
2. Tocá **Add marketplace** y pegá: `joaquinxtomas/design-w-claude`
3. Buscá **design-with-claude** y tocá **Instalar**.
4. En ese mismo marketplace, activá **Sync automatically** para que las mejoras te lleguen solas.

**En Claude Code se instala aparte** (lo que instalás en la app no aparece ahí). Abrí una sesión de Claude Code (app de escritorio → pestaña **Code**) y escribí, uno por vez:

```
/plugin marketplace add joaquinxtomas/design-w-claude
/plugin install design-with-claude@design-with-claude
/reload-plugins
```

Para actualizarlo en Claude Code: `/plugin marketplace update design-with-claude`, después `/plugin update design-with-claude@design-with-claude` y `/reload-plugins`.

### 2. Plugins que lo complementan (opcional, recomendado)

El plugin funciona solo, pero **si tenés estos instalados los usa** para su parte. Sin ellos, Claude hace esos pasos por su cuenta, con menos precisión.

| Instalá | Dónde | Qué suma |
| --- | --- | --- |
| **Marketing** | Personalizar → Plugins → Discover | Escribe los textos con la voz de cada marca y planifica la semana de piezas |
| **Design** | Personalizar → Plugins → Discover | Revisa la pieza antes de entregarla (jerarquía, contraste, legibilidad) |
| **Adobe** | Personalizar → Plugins → Discover | Prepara fotos, busca fuentes y genera las versiones para cada red |
| **Figma** | Configuración → Conectores | Arma las piezas directo en tu archivo de Figma |

Para Adobe y Figma, la primera vez te pide iniciar sesión con tu cuenta.

### 3. Cómo usarlo

Trabajá con un **Proyecto de Claude por cliente** y hablale normal:

| Escribí algo como | Qué pasa |
| --- | --- |
| "Configurá la marca de [cliente]" + su web, su Instagram, logo o aunque sea una foto | Arma el sistema de diseño de la marca (colores, letras, logo, tono, links) y lo guarda en Claude |
| "Diseñá una historia: 'HOY ABRIMOS TARDE', foto adjunta" | Diseña y te entrega PNG, PSD y el script para Photoshop |
| "Armame las 3 historias de la semana: lunes…, miércoles…, viernes…" | Te propone los textos, espera tu OK, hace una, y cuando la aprobás hace el resto |
| "Título más chico, oscurecé menos la foto" | Cambia solo eso |
| "Guardá esto como estilo 'aviso de horario'" | La próxima vez alcanza con una línea: "aviso de horario, abrimos a las 12" |
| "Quiero una historia inspirada en [una idea, textura, época o artista]" | Primero te propone una dirección de diseño; cuando la aprobás, diseña |
| "Tomá la info de marca de [web]" / "agregá su TikTok" | Lee de la web tipografías, colores y logo exactos, suma el link a las fuentes de la marca y guarda lo aprendido |
| "Tomá el diseño de la última publicación de @cliente y armá una historia" | Saltea las fijadas, abre la última y diseña con ese estilo |
| "Hacé el título en 3D: letras infladas con gotas, como esta referencia" | Renderiza el título 3D y arma la pieza alrededor |
| "Creá la carpeta de diseños" / "agregá esto a la carpeta" / "dejale esto a Claude Code" | Mantiene una carpeta por marca en tu compu para que Claude Code tenga todo el contexto |

**Al final de cada entrega**, si algo quedó aproximado (una tipografía, un efecto 3D, una foto), Claude te sugiere en una o dos líneas cómo acercarte más: por ejemplo Adobe Fonts, Illustrator (3D y materiales) o Firefly.

### 4. Qué archivos recibís

- **PNG**: la pieza terminada, lista para publicar.
- **PSD**: el archivo de Photoshop con cada elemento en su capa y con nombre (Foto, Título, Logo…). Ojo: acá **los textos vienen como imagen**.
- **Script `.jsx`**: convierte esos textos en **texto editable de verdad** (misma letra, tamaño y posición).
- **Tipografías** (si hacen falta): los archivos de las fuentes para instalar.

### 5. Terminar la pieza en Photoshop (con el `.jsx`)

1. **Instalá las tipografías** (una sola vez por marca): doble clic en cada `.ttf` u `.otf` → **Instalar**. Si la fuente es de Adobe Fonts, activala desde Creative Cloud. Después cerrá y abrí Photoshop.
2. **Abrí el PSD** en Photoshop.
3. **Ejecutá el script**: **Archivo → Secuencias de comandos → Explorar** (en inglés: *File → Scripts → Browse*) y elegí el `.jsx`. Agrega los textos como capas editables (con el ícono **T**) y oculta las versiones en imagen.
4. **Guardalo** con otro nombre (por ejemplo, agregando "_editable").
5. **Ajustá lo fino**: el script no se puede probar fuera de Photoshop, así que algún texto puede quedar corrido unos píxeles. Movelo a mano.
6. **Retocá lo que quieras**: cambiá la foto (colocala como máscara de recorte sobre la capa "Foto"), colores, sombras.
7. **Exportá**: **Archivo → Exportar → Exportar como** → PNG o JPG, sRGB.
8. **Contale a Claude lo que cambiaste** ("subí el título 40 px", "oscurecí la foto"): así actualiza el estilo guardado y la próxima pieza ya sale como la terminaste.

**Si el script da un error**, copiá el mensaje (o sacale una foto) y pasáselo a Claude en el mismo chat. Lo más común es que falte instalar una tipografía.

### 6. Para ir más lejos

#### Fuentes de la marca (web, redes e inspiración)

- **Todos los links juntos**, en el sistema de diseño: los de la marca (web, redes, manual), que mandan, separados de los de inspiración (solo ideas, nunca copiar). Para sumar uno: "agregá este link".
- **Lo aprendido de cada link queda guardado** (tipografías, colores, reglas, tono, con fecha). La próxima vez que pidas inspiración de esa fuente, Claude usa lo guardado en vez de volver a buscar. Para que la revise de nuevo: "fijate si cambió".
- **De una web**, Claude saca los nombres exactos de las tipografías, los colores y el logo en SVG. Las fuentes de una web suelen tener licencia solo para web: el nombre sirve para activarla en Adobe Fonts o pedírsela al cliente.

#### Referencias desde Instagram

- **Qué necesitás:** la app de escritorio con un navegador (el integrado o Claude in Chrome) donde tengas Instagram iniciado.
- **Qué hace Claude:** solo mira. Abre cada publicación (no la grilla, para ver la imagen en buena calidad), pocas y a ritmo normal; no da me gusta, no sigue cuentas ni manda mensajes, y frena si Instagram muestra cualquier aviso.
- **Tené en cuenta:** al abrir destacados, la marca ve que tu cuenta los vio. Lo que sale de capturas es aproximado: si tenés los archivos reales de la marca, pasáselos.
- **Sin navegador:** mandale 3 a 5 capturas y hace lo mismo.

#### Títulos 3D

- **Qué sale bien:** letras infladas, gotas, plástico brillante, gelatina, caramelo. **Qué no:** gemas, vidrio y cristal realistas.
- **Cómo funciona:** Claude dibuja las letras en plano, las "infla" y las renderiza con Blender. Entrega un PNG transparente que va como capa en el PSD.
- **Para el mejor resultado:** una captura en buena calidad de la referencia. Si querés llevarlo más lejos, Claude te prepara los vectores para Illustrator (Efecto → 3D y materiales → Inflar).

#### ¿Claude o Claude Code?

- **Claude (la app, como siempre):** para el día a día. Configurar marcas, tomar referencias, diseñar piezas, Figma. Corre en la nube: podés cerrar la ventana o pedirlo desde el celular.
- **Claude Code (app de escritorio → pestaña Code):** para el trabajo pesado en tu compu. Títulos 3D más rápidos con tu placa de video, tus tipografías instaladas, ejecutar los `.jsx` en Photoshop sin pasos manuales y muchas piezas de una.
- **Ojo:** Claude Code no lee tus Proyectos ni chats de Claude. Por eso existe la carpeta de diseños.

#### Carpeta de diseños (el puente con Claude Code)

Una carpeta en tu compu con todo lo de cada marca, que Claude va actualizando:

```
Claude Diseño/
├── CLAUDE.md              reglas generales (valen para todas las marcas)
└── BRAVA/
    ├── CLAUDE.md          reglas fijas de la marca
    ├── brand.md           colores, tipografías, tono, links de la marca
    ├── historial.md       todo lo que se fue agregando, con fecha
    ├── pendientes-code.md trabajos para hacer con Claude Code
    ├── logos/  fuentes/  fotos/  estilos/  3d/
    ├── referencias/       fuentes.md (lo aprendido de cada link), instagram/, web/, cliente/
    └── piezas/2026-11_campaña/   PNG, PSD, .jsx
```

- **Desde Claude (app de escritorio con la carpeta conectada):** "creá la carpeta de diseños", "nueva marca: X", "agregá esto a la carpeta", "dejale esto a Claude Code". Sin carpeta conectada, te entrega un .zip para descomprimir.
- **Desde Claude Code:** abrí la carpeta de la marca y pedí, por ejemplo, "hacé los pendientes". Ya tiene todo el contexto.
- **Instagram en Claude Code:** instalá la extensión **Claude in Chrome** y escribí `/chrome` dentro de la sesión.

### Comandos

Normalmente las skills se activan solas. Si querés asegurarte de que use una, empezá el mensaje con su comando (escribí `/` y elegilo de la lista).

| Comando | Qué hace | Ejemplo |
| --- | --- | --- |
| `/design-with-claude:brand-setup` | Configura una marca (colores, tipografías, logo, tono, links) a partir de archivos, su web o su Instagram, o guarda un estilo aprobado | `/design-with-claude:brand-setup Configurá la marca de "Raíz" con su web raizflores.com y su Instagram @raiz.flores.` |
| `/design-with-claude:design-piece` | Diseña una pieza a partir de un pedido corto y entrega PNG + PSD + `.jsx`, o la arma en Figma | `/design-with-claude:design-piece Historia para Raíz: "LLEGARON LAS PEONÍAS". Usá la foto adjunta.` |
| `/design-with-claude:design-from-ideas` | Convierte una idea (textura, época, artista, sensación) en una dirección de diseño, espera tu OK y diseña | `/design-with-claude:design-from-ideas Historia inspirada en los carteles de cine de los 70.` |
| `/design-with-claude:render-3d` | Hace un título 3D (letras infladas, gotas, borde brillante) para la pieza | `/design-with-claude:render-3d "SPOOKY CLASS", letras crema con gotas sobre base roja, como el post adjunto.` |
| `/design-with-claude:design-folder` | Crea y actualiza la carpeta de diseños para Claude Code | `/design-with-claude:design-folder Creá la carpeta de diseños en Documentos y agregá BRAVA.` |

Del plugin **Marketing** (si lo tenés):

| Comando | Qué hace | Ejemplo |
| --- | --- | --- |
| `/marketing:campaign-plan` | Planifica una campaña o la semana de contenido | `/marketing:campaign-plan Semana de lanzamiento del drop del 11/11.` |
| `/marketing:draft-content` | Escribe los textos de una pieza con la voz de la marca | `/marketing:draft-content Textos para 3 historias del drop.` |
| `/marketing:brand-review` | Revisa que los textos respeten la voz de la marca | `/marketing:brand-review Revisá estos 3 títulos.` |

## Changelog

- **0.7.0** — Brand sources: every link of a brand (website, social accounts, brand manual, inspiration) in the design system and brand.md, plus `fuentes.md` notes with what was learned from each link and when, so sources are not analyzed again every time. Websites become an official source (exact fonts, colors and SVG logo read from the code).
- **0.6.0** — New `design-folder` skill: creates and keeps updated a folder per brand on your computer (CLAUDE.md, brand.md, history, styles, references, pieces, 3D configs, pending jobs for Claude Code), from requests like "add this to the design folder". Brand-setup, design-piece, render-3d and Instagram references now save into it when it exists.
- **0.5.0** — New `render-3d` skill: inflated 3D titles with drips and a glossy rim (2D silhouette → inflate → Blender render), with a tested recipe. Design-piece now ends deliveries with 1–2 concrete routes to get closer when something is approximate (Illustrator Inflate, Blender connector, Firefly, Adobe Fonts…).
- **0.4.0** — References from Instagram: give a brand's `@account` (or ask for "their latest post") and Claude reads the profile, latest posts and highlights in your browser, read-only and at a normal pace, skipping pinned posts; screenshots as a fallback.
- **0.3.4** — README: command tables (what each does + an example) in English and Spanish, including useful Marketing plugin commands.
- **0.3.3** — The Adobe companion plugin is now called **Adobe** in the directory; names updated.
- **0.3.2** — Full Spanish guide: install, companion plugins (and that they are only used when installed), how to use, what files you get, and the step-by-step Photoshop flow with the `.jsx` for editable text.
- **0.3.1** — Fix: `build_psd.py` wrote PSDs with width and height swapped (1920×1080); they are now 1080×1920. Regenerate PSDs made with earlier versions.
- **0.3.0** — Works together with the Marketing, Design and Adobe plugins and the Figma connector when installed: copy in the brand's voice, photo prep, critique before delivery, per-channel variants, and a joined-up flow from brand to saved style. Companion plugins are optional.
- **0.2.0** — Brand kit lives in Claude's Design System artifact when available (brand.md as fallback); `design-piece` reads fonts and logos from it, always ships the `.jsx` for editable text with a PSD, and flags low-resolution or third-party content in photos; stronger skill triggers (English and Spanish).
- **0.1.0** — First version: brand setup, piece design (PNG/PSD/jsx/Figma), design from ideas, Figma and Adobe connectors.

## License

MIT
