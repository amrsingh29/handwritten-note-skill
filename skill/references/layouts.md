# Layout templates

Each template below has: when to use it, the structural skeleton, and any layout-specific rules. Colors come from `brands.md` — these skeletons use the same `--accent-1..4`, `--ink`, `--paper`, `--card-bg` tokens so any brand drops in cleanly. Two fully worked examples of the Flow template exist in `examples/` at the repo root (Field Notes and BMC Helix variants of a vector-database explainer) — read one if you want to see the pattern in full HTML/CSS rather than skeleton form.

---

## Flow / Steps

**When**: content is a sequence with a clear start and end — "A happens, which causes B, which produces C." Most "how does X work" conceptual explainers land here.

**Skeleton**: rows of 2-3 cards, each card = one step, connected by an arrow (horizontal SVG path between cards in a row, vertical between rows). Optional sidebar for a "why it matters" callout that doesn't belong in the sequence itself. Optional footer banner restating the thesis in one line.

```
[title + one-line thesis]
[row: card 1 → arrow → card 2 → arrow → card 3]
[vertical arrow]
[row: card 4 → arrow → card 5 → arrow → card 6]
[optional sidebar alongside the flow column]
[footer banner: the "aha" restated]
```

Each card: small numbered badge, bold short label (what happens), 1-2 sentence explanation, optional monospace "example" tag showing a concrete instance. Cards get independent slight rotation (`--tilt`, roughly ±1deg) in hand-drawn brands for the sticky-note feel; keep them axis-aligned in Ink & Marker (its minimalism doesn't want wobble).

Cap at 6 steps. If the real process has more, group into phases and show 4-6 phase-cards rather than every micro-step.

---

## Cycle / Loop

**When**: the process repeats — the output of the last step feeds back into the first, or the whole thing is meant to run continuously (feedback loops, iterative methodologies, monitoring loops).

**Skeleton**: same card style as Flow, but arranged around a circle or in a ring, with the connecting arrows curving and the last arrow looping back to the first card rather than terminating. A small looping-arrow glyph or label ("...and it starts again") at the closing arrow makes the repetition explicit rather than implied.

```
        [card 1]
   ↗               ↘
[card 4]         [card 2]
   ↖               ↙
        [card 3]
  (arrow from 4 loops back to 1)
```

For a 4-6 step cycle, a literal circular CSS/SVG layout works; for simpler tastes, a horizontal row with the final arrow curving back over the top to point at card 1 reads just as clearly and is easier to keep responsive on mobile (circular layouts often need to collapse to a vertical list on narrow screens — plan that fallback).

Put a short label at the center or below the ring naming what's constant across iterations (e.g. "the loop that never stops" or the invariant the cycle preserves) — this is the payoff of choosing Cycle over Flow, don't skip it.

**Geometry, if drawing a literal circle with SVG arcs**: anchor the four (or however many) stage cards at symmetric cardinal points on the circle — e.g. in a `viewBox="0 0 100 100"`, top `(50,10)`, right `(90,50)`, bottom `(50,90)`, left `(10,50)` — and connect them with plain `A` (arc) commands between those exact points: `M50,10 A40,40 0 0,1 90,50` and so on around. Asymmetric or hand-tuned bezier curves between mismatched points are what caused a real bug during testing — the loop-back arrow drifted outside the container and overlapped the header text. Give the wrapping container generous top/bottom margin (not just internal padding) before adding cards, since cards are positioned with `transform: translate()` and can extend outside the container's own box — overlap with the title or footer above/below is easy to miss until you actually render it.

---

## Hub & Spoke

**When**: one core concept has several related but mutually independent facets — "here's what makes up X" or "here's everything that influences X" — where the children don't have a sequence relationship to each other.

**Skeleton**: a central card/circle holding the core concept, with 3-6 spoke cards arranged around it, each connected to the center by a short line (not to each other).

```
              [spoke A]
[spoke D]                  [spoke B]
        \        |        /
         \       |       /
          [ CENTER CONCEPT ]
         /       |       \
        /        |        \
[spoke C]                  [spoke E]
```

The center card should be visually heavier (larger, bolder border or the strongest accent) than the spokes — it's the thing everything relates back to. Spokes can each carry a different accent color from the rotation to keep them visually distinct from one another, since — unlike Flow — their order doesn't matter and color-coding replaces numbering. On narrow viewports, collapse to a bulleted list under the center card rather than trying to preserve the radial geometry.

---

## Comparison / Before-After

**When**: two things are being directly contrasted — old approach vs new, option A vs option B, myth vs reality.

**Skeleton**: two columns of equal weight, mirrored structure (same row-for-row aspects compared on each side), with a clear divider and small labels heading each column.

```
[title]
[   LEFT LABEL   ]  |  [   RIGHT LABEL   ]
[ aspect 1: value ]  |  [ aspect 1: value ]
[ aspect 2: value ]  |  [ aspect 2: value ]
[ aspect 3: value ]  |  [ aspect 3: value ]
[ verdict / takeaway spanning both columns ]
```

Give each column its own accent (e.g. `--accent-2` for "before"/A, `--accent-1` for "after"/B) applied consistently down that whole column — border color, label color — so the eye tracks "everything orange is the old way" without rereading labels each row. This is the one template where a brand may need a token beyond its usual four accents for one column's background tint (BMC Helix's Sky/Lilac tints are there for exactly this); don't force it into the existing four if it muddies the two-column read. Stack to a single column with a divider rule between sides on narrow viewports, not side-by-side-shrunk.

---

## Timeline

**When**: events unfold across real time — history, a roadmap, an evolution of a technology or idea — and the dates/order themselves carry information the reader needs (unlike Flow, where steps are logical, not chronological).

**Skeleton**: a single spine (horizontal on wide screens, vertical on narrow) with milestone markers along it, each with a date/era label and a short card of what happened.

```
●───────────●───────────●───────────●
2019        2021        2023        2025
[card]      [card]      [card]      [card]
```

Vary marker size or add a highlight ring on the single most important milestone (the turning point) rather than treating every point as equal weight — a timeline where every event looks the same importance fails to communicate which one actually mattered. Alternate cards above/below the spine if there are more than 4 milestones to avoid a single overlong row.

**Grid geometry, if using CSS Grid for the alternating above/below layout**: don't make the spine line itself a full-width grid item (e.g. `grid-column: 1 / -1`) inside the same grid that holds the cards and dots. A grid item spanning every column occupies that entire row in the auto-placement algorithm, so sibling items relying on auto-placement (rather than an explicit `grid-column`) get pushed into implicit extra rows/columns to find free space — in a real build this made every dot cluster in the wrong place instead of spreading one-per-milestone along the spine. Pull the spine line out of the grid entirely: give it `position: absolute` inside a `position: relative` wrapper around the grid, so it draws as a visual line behind the content without participating in grid placement at all.

---

## Layered / Stack

**When**: the topic is about things sitting on top of / built upon each other structurally — network protocol stacks, system architecture, "layers of abstraction" concepts (physical → data link → ... → application, or storage → API → UI).

**Skeleton**: horizontal bands stacked vertically, bottom band = foundation, top band = what the user-facing layer actually is. Each band spans the full width; thickness can vary to suggest relative "size" of concern if relevant (e.g. a thick data layer under a thin presentation layer).

```
[ TOP LAYER — what the user sees        ]
[ MIDDLE LAYER — what does the work     ]
[ MIDDLE LAYER 2                        ]
[ FOUNDATION — what everything sits on  ]
        (small arrows or "built on" labels between bands)
```

Label each band with both its name and a one-line "what lives here" so the stack reads top-to-bottom as a story, not just a labeled diagram. Use a consistent left-edge accent stripe per band (rotating through the brand's accents bottom-to-top) rather than fully coloring each band — full-color bands stacked tend to look like a flag rather than a diagram.

---

## Zoom Levels

**When**: the topic has real depth and different readers want different amounts of it — a "give me the 10-second version" crowd and a "no really, explain the mechanism" crowd both showing up for the same topic. Unlike the other templates, this one isn't about the shape of the content's parts — it's about depth of explanation of the *same* idea, told three times at increasing resolution.

**Skeleton**: three stacked (or tabbed) sections, each explaining the whole topic at a different zoom level, each visually "denser" than the last — more words, more specifics, maybe a small diagram only at the deepest level.

```
[ 🔭 THE 10-SECOND VERSION — one sentence, plain language           ]
[ 🔬 THE 1-MINUTE VERSION  — a short paragraph, the actual mechanism ]
[ 🧪 THE DEEP-DIVE          — the real detail: numbers, caveats,     ]
[                             the thing experts would argue about    ]
```

Each level should stand alone — a reader who stops after level 1 got a complete (if shallow) answer, not a teaser. Visually distinguish the levels by more than just position: increasing card size/padding, a progressively "busier" background texture, or an increasing accent-color intensity all signal "more depth" without needing the reader to read a label. Cap at three levels — a fourth makes the reader wonder why they didn't just read a Wikipedia article. This template pairs unusually well with topics that have real scientific or technical depth (physics, medicine, cryptography) where the 10-second version is necessarily a simplification worth being honest about.

---

## Matrix / Quadrant

**When**: the topic is genuinely two-dimensional — two independent factors combine to put things (or advice) into one of four buckets. Look for content that's actually organized around two named axes already (growth vs. share, urgency vs. importance, effort vs. impact) rather than forcing an arbitrary split — if the topic doesn't have a real second axis, this becomes decoration, not explanation. A giveaway that a topic fits: the standard explanation of it already uses words like "axis," "high/low," or names its four buckets (the BCG matrix's Stars/Cash Cows/Question Marks/Dogs is the canonical example).

**Skeleton**: a 2×2 grid with labeled axes on the outer edges (what each axis measures, plus which direction is "more") and one card per quadrant.

```
                    ← low X            high X →
              ┌───────────────────┬───────────────────┐
  high Y  ↑   │   Quadrant TL      │   Quadrant TR      │
              ├───────────────────┼───────────────────┤
              │   Quadrant BL      │   Quadrant BR      │
              └───────────────────┴───────────────────┘
                    Y-axis label runs along the left edge
```

Each quadrant card needs: a name (the framework's own term for that bucket, if it has one — don't invent generic labels when "Cash Cow" already exists), a one-line description of what lands there, and the action or takeaway that follows from being in that quadrant — a quadrant that only describes but never prescribes wastes the format. Resist coloring all four quadrants differently just because there are four of them; a brand with a single-accent rule (like Ink & Marker) should keep the grid in the brand's neutral ink and use the accent only for the buckets' names, not backgrounds — the axes and borders are doing the organizing, not color. On narrow viewports, collapse to a single column stack (still one card per quadrant, in reading order) rather than trying to shrink the grid, since axis labels stop being legible below a certain width.

---

## Decision Tree / Branching

**When**: the reader has a real choice to make and the right answer depends on their specific situation — "which X should I use," "should I do A or B," troubleshooting flows. The giveaway that a topic fits: someone would naturally answer with "it depends — do you...?" rather than a single explanation. If there's only one path through the content, this is Flow, not a tree.

**Skeleton**: a question node at top, branching into two (or more) labeled paths, each leading either to another question (going deeper) or a leaf card with a concrete recommendation. Nest recursively — each level's "continue" branch contains the next question-and-branches unit.

```
                [ QUESTION 1: is it X? ]
                 /                    \
            [NO]                    [YES]
              |                        |
        [Leaf: do A]          [ QUESTION 2: is it Y? ]
                                /                    \
                            [NO]                    [YES]
                              |                        |
                        [Leaf: do B]            [Leaf: do C]
```

Every leaf must be an actual recommendation ("use this: ___"), not just a restated condition — a decision tree that only classifies but never advises wastes the format the same way a Matrix quadrant that never prescribes does. Label every branch with the actual answer that leads there ("no," "exact facts," "a lot") rather than generic "path A / path B" — the labels are what let a reader jump straight to their branch without reading the others.

**Two things that go wrong if you're not careful, learned from a real build:**

1. **Connector line geometry.** If you draw the horizontal "this question splits into two answers" bar with a pseudo-element or fixed percentage offsets, its endpoints must land exactly on each branch's true center — not an arbitrary inset guess. Compute the line's `left`/`right` insets from the actual column math (e.g. two equal `1fr` columns means each column's center sits at 25% and 75% of the container, so the connecting line should span `left: 25%; right: 25%`, not something like `12.5%/87.5%` picked by eye) so the line's ends land exactly where the vertical drop into each branch actually is. A line that overshoots or undershoots the branch it's supposedly connecting to is immediately noticeable even to a casual reader.
2. **Depth vs. width.** Each level of nesting halves the horizontal space available to what's below it (since branches keep splitting into two within the same container). Past 3 questions deep, leaf cards get squeezed narrow and their text turns tall and cramped compared to shallower leaves. Cap real decision trees at 3 questions (4 levels of leaves) for this format, and give leaf cards a `min-width` so they resist shrinking below a readable point — if a topic genuinely needs more than 3 questions, it's a sign to either cut a question or reconsider whether Decision Tree is really the right shape for it.

---

## Glossary / Field Guide

**When**: the topic is really a set of terms someone needs defined before anything else about the subject makes sense — jargon that keeps coming up in conversation, the vocabulary of a field, or named specimens of a category (cloud types, logical fallacies, plant families). The giveaway: the content doesn't have an order, a hierarchy, or a relationship between items — each entry is fully independent and could be read in any sequence, which is what separates this from Hub & Spoke (which has a central concept the entries relate back to).

**Skeleton**: a uniform grid of small "specimen" cards, each with an icon, the term, and a one- or two-sentence definition in plain language.

```
[icon] SPECIMEN 01     [icon] SPECIMEN 02     [icon] SPECIMEN 03     [icon] SPECIMEN 04
Term                    Term                    Term                    Term
one-line definition     one-line definition     one-line definition     one-line definition

[icon] SPECIMEN 05     [icon] SPECIMEN 06     [icon] SPECIMEN 07     [icon] SPECIMEN 08
Term                    Term                    Term                    Term
one-line definition     one-line definition     one-line definition     one-line definition
```

Keep every definition genuinely plain-language — the whole point of a field guide is translating jargon into something a newcomer can read once and retain, so a definition that itself uses undefined jargon defeats the format. 6-8 terms is the sweet spot for one page; more than that and it stops being a quick reference and starts being a dictionary, which argues for trimming to the terms that actually come up most, not covering everything exhaustively. Give each card a distinct icon (an emoji is fine) rather than reusing the same one throughout — the icon is a memory hook, and identical icons across all cards waste that. A brand with a single-accent rule can still rotate the *icon* per card even while keeping a single border/text accent, since the icon carries the visual variety instead of color.
