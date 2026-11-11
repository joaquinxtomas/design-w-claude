# Claude Diseño — reglas generales

Esta carpeta guarda el contexto de cada marca. Cada subcarpeta es una marca, con su propio CLAUDE.md, brand.md, estilos y piezas. Trabajá siempre dentro de la carpeta de la marca que corresponda.

## Cómo trabajar
- Respondé en español rioplatense (voseo), corto y concreto.
- Antes de diseñar, leé `brand.md`, `CLAUDE.md` y `estilos/` de la marca. No pidas de nuevo lo que ya está en la carpeta.
- Entregá siempre PNG + PSD con capas + `.jsx` de texto editable, salvo que se pida otra cosa.
- Formatos por defecto: historia 1080×1920 (250 px libres arriba y abajo), post 1080×1350.
- Guardá cada entrega en `piezas/AAAA-MM_<campaña>/` y anotá una línea en `historial.md`.
- Mismo grosor de letra en todo un título: nunca afines o engroses letras sueltas.
- Usá el plugin design-with-claude (brand-setup, design-piece, design-from-ideas, render-3d, design-folder).

## Cuando trabajás en esta computadora (Claude Code)
- **Tipografías:** usá las instaladas o las de `fuentes/`; nada de aproximaciones si la real está.
- **3D:** usá la skill render-3d con Blender local y GPU (Cycles con OptiX/CUDA/Metal si está disponible). Revisá las configs que ya funcionaron en `3d/`.
- **Photoshop:** después de generar PSD + `.jsx`, ejecutá el script en Photoshop (macOS: `osascript -e 'tell application id "com.adobe.Photoshop" to do javascript file "<ruta.jsx>"'`; Windows: abrí Photoshop con el `.jsx`). Guardá la copia `_editable`.
- **Instagram (Claude in Chrome):** abrí cada publicación (nunca la grilla) y guardá la imagen original en `referencias/instagram/AAAA-MM-DD_<tema>.jpg`. Solo mirar, pocas publicaciones, ritmo normal; si Instagram muestra un aviso, pará.
- **Pendientes:** si te piden "hacé los pendientes", resolvé `pendientes-code.md` de arriba hacia abajo y tachá cada tarea al terminar.

## Herramientas y técnicas
- (se completa a medida que se adoptan: conectores, plugins, recetas que funcionaron)
