# Companion plugins: how everything fits together

This plugin is the glue. It owns the brand, the saved styles, the piece and the Photoshop delivery. Other plugins do specialized parts better; use them whenever they are installed in the session. Never require them: if one is missing, do that step yourself and, at most once per conversation, mention in one line which plugin would help.

Find them by looking at the available skills (names and descriptions). Names change between versions, so match by purpose, not by exact name.

| Plugin | Look for skills about | Use it for | When in the flow |
| --- | --- | --- | --- |
| Marketing (Anthropic) | brand voice, brand review, drafting content, campaign planning | Writing or tightening the copy of a piece in the brand's voice; checking copy against the voice; planning a week or a campaign of pieces | Before designing (copy), and when planning batches |
| Design (Anthropic) | design critique, accessibility review | Reviewing the finished piece (hierarchy, contrast, legibility) before delivering | After the review checklist, before delivery |
| Adobe for creativity (plugin or connector) | batch photo editing, background removal, resizing, social variations, fonts | Preparing photos (match color across a set, remove backgrounds, expand to vertical); finding licensed fonts; producing per-channel versions after approval | Before designing (photos, fonts) and after approval (variants) |
| Figma (connector or plugin) | writing to the canvas, design systems | Building the piece natively in the user's Figma file when they work in Figma | Delivery |
| Anthropic design skills | theme-factory, canvas-design, algorithmic-art | Palettes and font pairings, exploratory pieces, original textures | Direction and sketching |

## The joined-up flow

1. **Brand** (brand-setup): design system + voice. If Marketing is installed, use its brand-voice skill to write the voice section, so copy and design share one source.
2. **Plan** (optional): for a week or a campaign, use Marketing's campaign planning to list pieces with goal, copy and date, then confirm the list with the user.
3. **Copy**: if the user did not give final text, draft it with Marketing's voice skill (short, on-brand), and get approval. Text in quotes from the user is never rewritten.
4. **Photos**: with Adobe, match, clean and resize the photos before composing.
5. **Design** (design-piece or design-from-ideas): compose, review with the checklist, then run Design's critique if installed and fix what it finds.
6. **Deliver**: PNG + PSD + .jsx, or a Figma frame.
7. **Multiply**: after approval, with Adobe, create the other formats (post, Reel cover, banners).
8. **Save**: store the approved style in the brand (brand-setup).

Tell the user in one short line which companion was used at each step ("copy checked with your brand voice, photos matched with Adobe"), so they learn what is available.
