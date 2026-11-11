# Brand sources: links and what was learned from each

Two parts that always go together:

1. **Sources list** — every link of the brand, kept with the brand (Design System README, and brand.md for Claude Code).
2. **Source notes** — what was learned from each link (`fuentes.md`), so Claude does not analyze the same source again every time.

## 1. Sources list

Record every link the user gives, in two groups:

| Group | Examples | Weight |
| --- | --- | --- |
| **Brand (authoritative)** | Website, Instagram, TikTok, LinkedIn, brand manual, Linktree | These define the brand. If two disagree, say so and ask which one rules. |
| **Inspiration** | Accounts or sites the user or client likes, Pinterest/Behance boards, competitors | Ideas only: take the idea, never copy the piece. |

Where:
- **Design System artifact:** a "Sources" section in its README with both groups (name, link, one line of what it is).
- **brand.md:** the same list under "## Sources", so Claude Code (which cannot read artifacts or chats) has it too.
- **Design folder:** also in the brand's `referencias/fuentes.md` (below).

When the user says "add this link", "agregá esta web", "sumá su TikTok", add it to the list in all places that exist and say where.

## 2. Source notes (`fuentes.md`)

One block per link, newest checks first:

```
## <name> — <link> — <brand | inspiration>
Checked: YYYY-MM-DD (how: website code / browser / Instagram opened posts / screenshots)
- Fonts: exact names if read from code; "approximate" if from images
- Colors: HEX (exact from code, or estimated)
- Logo/assets: what exists and where it was saved
- Design rules seen: layout, type hierarchy, photo treatment, recurring elements
- Tone: how the brand talks there
- Campaigns or changes: what is current
- Recheck: when (e.g. "if the site is redesigned" / "every 2-3 months" / "each new campaign")
```

Rules:
- **Use the notes first.** When asked for inspiration or references from a listed source, read its block. If it was checked recently enough for the task (same campaign, under ~4 weeks for social, ~3 months for a website), use it without browsing again, and say so in one line.
- **Recheck when:** the note is old, the user asks ("check if it changed", "fijate si cambió"), or the task is about something new (a campaign launched after the last check). Then update the block and its date.
- **Instagram:** fewer visits means less risk for the account, so lean on the notes; follow `instagram-references.md` when browsing.
- Without a design folder, keep the notes in the Design System README under "Source notes", or in brand.md.

## Reading a website

1. **Read as text** (web fetch) for copy, tone, services and structure.
2. **Open it in the browser** (built-in browser or Claude in Chrome) for the visual look; take a screenshot of the home and one inner page.
3. **Read the page's code** for exact values: `font-family` declarations and `@font-face` names, CSS color values and variables (`--color-…`), and the logo (`<svg>` or the logo image URL).
4. Save the logo SVG and useful high-resolution photos to the brand's folders (logos/, fotos/) when there is a design folder.

Cautions:
- **Web fonts are usually licensed for the web only.** Record the exact name; activate it in Adobe Fonts or ask the client for the files. Do not design with the font file taken from the site.
- **Photos and logos belong to the client:** fine for the client's own pieces; confirm with the user if in doubt.
- **Websites go stale:** if the site disagrees with recent social posts, point it out and ask which one rules.
- Read only; never submit forms or log in on the brand's site.
