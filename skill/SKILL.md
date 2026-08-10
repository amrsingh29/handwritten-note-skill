---
name: handwritten-note
description: Turn any concept, capability, or topic into a simple visual explainer rendered as a single self-contained HTML page — a "hand-drawn note" or clean diagram, published as an Artifact. Use this whenever the user asks to "explain X simply," "make this easy to understand," "create a visual explainer," "make a one-pager," "sketch out how X works," or references a "handwritten note," "field note," or similar note-style diagram for a concept — even if they don't name the skill directly. Also use when the user asks to explain something "like I'm five," wants a shareable/printable explanation of a process, system, or idea, or explicitly names a brand for the output (e.g. "explain this in BMC Helix style"). Do not use for long-form documents, code generation, or requests that are really asking for a slide deck (use frontend-slides for multi-slide decks) or a written report.
---

# Handwritten Note

Turn a topic into a single-page visual explainer. This skill has two independent decisions to make before writing any code: **which layout best fits the shape of the content**, and **which visual brand to render it in**. Get both right and the note does the explaining almost by itself — a topic forced into the wrong shape (e.g. a comparison crammed into a linear flow) reads worse than plain text would have.

## Step 1 — Understand the topic well enough to simplify it

Before touching layout or color, write the actual content: a short thesis line, and the handful of chunks (steps, branches, contrasts, milestones, layers — whatever the topic actually has) that carry the explanation. Real content beats generic content — use concrete examples, not placeholders. If the topic is genuinely complex, resist cramming everything in: a note that explains 80% of the idea clearly beats one that explains 100% of it densely. 4-6 content chunks is the sweet spot for any layout below; more than that and the page stops being simple.

## Step 2 — Pick the layout template

Choose based on the actual shape of the content, not habit. Read `references/layouts.md` for the full structural spec (HTML/CSS skeleton, when to use it, and worked examples) of whichever template you pick:

| Content shape | Template |
|---|---|
| A happens, then B, then C — a process with a clear start and end | **Flow / Steps** |
| The same process repeats — output feeds back into input | **Cycle / Loop** |
| One central idea with several related-but-independent facets | **Hub & Spoke** |
| Two things being directly contrasted (old vs new, A vs B) | **Comparison** |
| Events across time, with dates or ordered eras | **Timeline** |
| Things that sit on top of each other structurally (architecture, protocol stacks) | **Layered / Stack** |

If a topic could fit two templates, pick the one that makes the *reader's* job easier, not the one with more visual novelty. Most "how X works" conceptual explainers are Flow or Hub & Spoke — don't reach for something exotic just for variety.

## Step 3 — Choose the visual brand

**Always ask the user which brand to use before building**, unless they already named one in their request (e.g. "explain this in BMC Helix style," "use the chalkboard one"). This is a deliberate exception to building without back-and-forth — brand is a matter of taste and context (client-facing vs personal notes vs playful vs corporate), not something to infer silently. Use AskUserQuestion or a plain question listing the options from `references/brands.md`:

- **Field Notes** — warm cream paper, handwritten font, warm multi-color rotation. Personal, journal-like.
- **Chalkboard** — dark board background, chalk-white ink, pastel chalk accents. Classroom feel.
- **Sticky Wall** — bright background, real sticky-note-colored cards. Workshop/sprint feel.
- **Ink & Marker** — stark white, bold black lettering, one loud accent color. Punchy, minimal.
- **Midnight Notebook** — dark navy default background, gold/cyan ink. Premium, technical.
- **BMC Helix** — same hand-drawn styling and layout mechanics as Field Notes, but recolored with the BMC Helix brand palette (see `references/brands.md` for exact tokens and usage rules). Use this whenever the user says "Helix," "BMC," or names the company brand.

Read `references/brands.md` for the exact color tokens, font stacks, and any usage constraints (e.g. BMC Helix's "orange is accent-only, never dominant" rule) for whichever brand is chosen.

## Step 4 — Build it

Combine the layout skeleton from `references/layouts.md` with the color tokens from `references/brands.md` into one self-contained HTML file:

- Use CSS custom properties on `:root` for every color so brand-swapping later is a token change, not a rewrite.
- Support both light and dark viewer themes: redefine tokens under `@media (prefers-color-scheme: dark)` and under `:root[data-theme="dark"]` / `:root[data-theme="light"]` — the exception is a brand that deliberately commits to one look (e.g. Chalkboard's dark board *is* the brand, not a light/dark toggle).
- Keep hand-drawn brands (Field Notes, Chalkboard, Sticky Wall, Ink & Marker, Midnight Notebook, BMC Helix) on a handwritten font stack: `"Bradley Hand", "Segoe Print", "Chalkboard SE", "Comic Sans MS", cursive`. Small utility labels (numbered badges, eyebrow text) can use a clean sans stack for legibility even within a handwritten brand — see the worked examples.
- Write real copy for the topic at hand: a title, a one-line thesis under it, and content per the chunks decided in Step 1. Avoid lorem ipsum or placeholder text anywhere.
- Publish the result as an Artifact (load the `artifact-design` skill's fundamentals for theme/CSP/responsiveness basics if unsure, but the visual direction itself comes from this skill, not from generic artifact defaults).

## Step 5 — Check it before calling it done

Reread the page as if you were the intended reader, not the author: does the thesis line alone tell someone what this note is about? Does each chunk stand on its own without needing the others read first? Is there any card whose text got cut or overflowed at typical viewport widths? Fix before showing the user.

## Step 6 — Save the output as a new example

Every note this skill produces becomes a reference example, so save it into the repo rather than leaving it only as a published Artifact:

1. Make a new folder at `examples/<topic-slug>-<brand-slug>/` in the `handwritten-note-skill` repo (e.g. `examples/ai-agent-components-field-notes/`), using kebab-case derived from the topic and chosen brand.
2. Copy the final HTML file into that folder as `note.html`.
3. Capture a PNG of the rendered result: open the HTML (or the published Artifact URL) in the Browser pane and take a screenshot, saving it into the same folder as `preview.png`. This gives the example a thumbnail that's readable without opening the HTML.
4. If asked to sync to GitHub, commit both files together with a message naming the topic and brand (e.g. `feat: add AI agent components example (Field Notes)`), and push.

Don't create the folder speculatively before the note is finished — only once Step 5's check has passed and the user has seen the result, so examples/ only accumulates notes that actually worked.

## Adding a new brand or layout later

Both reference files are meant to grow. If the user asks for a new brand ("make one that looks like X") or a new layout, add it to the relevant reference file the same way the existing entries are structured — named tokens/skeleton plus a one-line "when to use this" note — rather than improvising it inline each time. That keeps future notes in that brand/layout consistent with this one.
