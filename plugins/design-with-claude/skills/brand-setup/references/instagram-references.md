# References from Instagram

Use this when the user gives an Instagram account (`@brand`, a profile link or a post link) as the source of a brand's references, or asks to take the design of a brand's latest post(s) for a new campaign.

## Before starting

- Check the brand's source notes first (`fuentes.md`, see `sources.md`): if this account was checked recently enough for the task, use the notes instead of browsing again.

- A browser is needed: the built-in browser of the Claude desktop app or Claude in Chrome. Load that browser's skill before the first step. With no browser available, go straight to "Fallback".
- Work with the user's own Instagram session in that browser. Logged out, Instagram shows very little; if a login wall appears, ask the user to sign in themselves (never type credentials).
- Say in one line before starting: Claude only looks, at a normal pace, a handful of posts, and opening highlights shows the brand that their account viewed them.

## Account safety rules (always)

Instagram's terms forbid collecting information in automated ways, and accounts that look automated can be restricted. Keep the activity indistinguishable from a person browsing:

- **Read only.** Never like, follow, comment, reply to stories, send messages, save posts or change anything on the account.
- **Few items.** At most about 12 grid posts, 3 carousels and 2 highlights per brand per request. If more is needed, ask the user first.
- **Normal pace.** Open things one at a time, as a person would; no rapid loops, no endless scrolling, no repeated reloads.
- **No bulk download.** Do not fetch Instagram's internal APIs or download images in batches; look at the page and take screenshots or zooms of what matters.
- **Stop on any warning.** If Instagram shows "suspected automated behavior", a challenge or an action block, stop immediately, tell the user, and switch to "Fallback".

## Steps

1. Open the profile (`https://www.instagram.com/<handle>/`). Note bio, profile photo/logo and highlight names.
2. Look at the grid (one screenshot, one or two scrolls). Identify recurring layouts, colors, type styles and photo treatment.
3. **Latest post(s):** pinned posts appear first and are often old. Skip any post with a pin icon, open the first non-pinned one and confirm its date ("1 h", "3 days") before calling it the latest. Walk through every image of a carousel.
4. **Stories:** stories expire in 24 h, so use highlights. Pause the viewer, then step through a few slides with the arrows; zoom on text to read type and copy.
5. Close viewers and leave the tab as it was.

## What to extract

Describe concretely, at 1080 px width:

- **Logo:** shape, versions (light/dark), where it sits.
- **Colors:** 4 to 6 approximate HEX values, labeled as estimated from screenshots.
- **Type:** style of each role (headline, body, accent): serif/sans/script, weight, case, tracking. Name similar fonts, never claim the exact one from an image.
- **Layout patterns:** margins, alignment, overlays or veils on photos, buttons/pills, recurring calls to action.
- **Campaign system (when it is a campaign):** its own colors, key visual, repeatable elements (frames, boxes, taglines), and how it differs from the base brand.
- **Tone:** formal or casual, voseo/tú, emojis, language mix, punctuation habits; quote the caption only briefly.

## Record it

- Update the account's block in the source notes (`fuentes.md`) with today's date and what was learned.

- With a design folder: save the opened posts' images in `referencias/instagram/YYYY-MM-DD_<topic>.jpg` (on the user's computer, Claude Code can save the original full-resolution file; otherwise capture the opened post at 1:1 in tiles and stitch them) and add what was learned to `referencias/instagram/notas.md`.

- Add the findings to the brand's design system (or brand.md) marked "source: Instagram (approximate)". Ask for the real logo, font files and photos; they always beat screenshots.
- A campaign becomes a **saved style** (e.g. "BRAVA Sessions") so later pieces take one line.
- Use the screenshots only as reference. Do not reuse the brand's photos or artwork inside new pieces unless the user provides the files or confirms the brand owns them and wants them reused.

## Fallback (no browser, logged out or warning)

Ask the user for 3 to 5 screenshots of posts or highlight stories, or post links. Analyze those the same way.
