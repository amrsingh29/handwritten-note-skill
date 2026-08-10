# Brand palettes

Each brand is a full token set (light + dark), not just an accent swap. Apply these as CSS custom properties on `:root`, redefined under `@media (prefers-color-scheme: dark)` and `:root[data-theme="dark"|"light"]` per `SKILL.md`.

Token names used consistently across brands:

- `--paper` / `--paper-line` — page background and its ruled-line tint
- `--ink` / `--ink-soft` — primary text / secondary (softer) text
- `--card-bg` — card background
- `--shadow` — card drop-shadow color
- Four accent slots, named per-brand below, cycled across content chunks (card borders, numbered badges, sidebar/banner borders)

---

## Field Notes

Warm, personal, journal-like. The default when the user has no brand preference and hasn't asked for something bolder.

```css
:root {
  --paper: #f6f2e9;
  --paper-line: #dcd3bf;
  --ink: #1e2a38;
  --ink-soft: #4a5b6b;
  --accent-1: #0f8b8d; /* teal */
  --accent-2: #e4572e; /* coral */
  --accent-3: #e8a33d; /* gold */
  --accent-4: #6a4c93; /* plum */
  --card-bg: #fffdf8;
  --shadow: rgba(30, 42, 56, 0.16);
}
:root[data-theme="dark"] {
  --paper: #1b2027; --paper-line: #323a45;
  --ink: #eee7d8; --ink-soft: #a9b4c0;
  --accent-1: #4fd1ce; --accent-2: #ff8360;
  --accent-3: #f2bd6c; --accent-4: #b79ceb;
  --card-bg: #232a33; --shadow: rgba(0,0,0,0.45);
}
```

Font: handwritten stack. Body copy warm and conversational.

---

## Chalkboard

Classroom feel. Single-theme by design — the dark board *is* the brand, don't add a light variant.

```css
:root {
  --paper: #1c2b26;
  --paper-line: #2c3f38;
  --ink: #f4f1e8;
  --ink-soft: #b9c4bd;
  --accent-1: #f6e05e; /* chalk yellow */
  --accent-2: #f6a5c0; /* chalk pink */
  --accent-3: #7ec8e3; /* chalk blue */
  --accent-4: #c7f0d8; /* chalk mint */
  --card-bg: #22332d;
  --shadow: rgba(0, 0, 0, 0.5);
}
```

Add a very subtle grain/noise texture (SVG feTurbulence at low opacity) behind content to sell the chalk-dust feel. Card borders can look like chalk strokes (slightly irregular dasharray) rather than clean lines.

---

## Sticky Wall

Workshop / sprint-retro feel. Cards are colored like actual sticky notes, not just outlined.

```css
:root {
  --paper: #f4f5f7;
  --paper-line: #e3e5ea;
  --ink: #24272b;
  --ink-soft: #5b606a;
  --accent-1: #fff275; /* yellow note */
  --accent-2: #ff8fab; /* pink note */
  --accent-3: #8ecae6; /* blue note */
  --accent-4: #b9fbc0; /* green note */
  --card-bg: #ffffff; /* overridden per-card: card bg = accent, tinted */
  --shadow: rgba(0, 0, 0, 0.18);
}
:root[data-theme="dark"] {
  --paper: #1a1b1e; --paper-line: #2a2c30;
  --ink: #eceef0; --ink-soft: #a3a7ad;
  --accent-1: #d8c94a; --accent-2: #d97a92;
  --accent-3: #6fa8c4; --accent-4: #8fd3a0;
  --card-bg: #232427; --shadow: rgba(0,0,0,0.5);
}
```

Difference from other brands: each card's `background` is set to its accent color at ~85% opacity over `--card-bg` (not just the border), with a slight rotation and a heavier shadow to read as "stuck to a wall."

---

## Ink & Marker

Punchy, minimal. Exactly one accent — resist adding more even when there are many content chunks; differentiate chunks with numbering/weight instead of color.

```css
:root {
  --paper: #ffffff;
  --paper-line: #eeeeee;
  --ink: #111111;
  --ink-soft: #55555a;
  --accent-1: #ff4500; /* the one accent — use for ALL emphasis */
  --card-bg: #ffffff;
  --shadow: rgba(0, 0, 0, 0.12);
}
:root[data-theme="dark"] {
  --paper: #0c0c0d; --paper-line: #1c1c1e;
  --ink: #f2f2f2; --ink-soft: #a0a0a5;
  --accent-1: #ff6a3d;
  --card-bg: #17171a; --shadow: rgba(0,0,0,0.5);
}
```

Card borders bold (3px+) black/white, not colored. The accent appears only on: the underline rule, one keyword per section, and CTA-style banners.

---

## Midnight Notebook

Premium, technical. Dark is the *default* ground (not just the dark-mode variant) — light mode should still feel closer to a deep-navy notebook than to Field Notes' cream paper.

```css
:root {
  --paper: #0b1830;
  --paper-line: #1a2b4a;
  --ink: #f0ead6; /* warm off-white, like a fountain pen page */
  --ink-soft: #9fb0c8;
  --accent-1: #e8b04b; /* gold ink */
  --accent-2: #5fd4d6; /* soft cyan */
  --accent-3: #c98bd6; /* soft violet */
  --accent-4: #7ea8e0; /* soft blue */
  --card-bg: #101f3d;
  --shadow: rgba(0, 0, 0, 0.5);
}
:root[data-theme="light"] {
  --paper: #14264a; --paper-line: #22355c;
  --ink: #f5efdf; --ink-soft: #b7c4da;
  --card-bg: #16294f;
}
```

Font can lean slightly more elegant within the handwritten stack constraint (still cursive fallback), thin gold rule lines under headings.

---

## BMC Helix

Same hand-drawn styling and layout mechanics as Field Notes (rotated cards, wobble-arrow connectors, handwritten font) — only the palette changes. Use whenever the user names "Helix," "BMC," or asks for the company brand. Do not switch to a clean corporate sans typeface for this brand unless the user explicitly asks for a non-hand-drawn treatment — that was tried once and rejected in favor of keeping the hand-drawn feel with brand colors substituted in.

Sourced from the BMC Helix brand guide's core + extended palette:

```css
:root {
  --paper: #f7f8fd;       /* Cloud */
  --paper-line: #dde3f0;
  --ink: #052140;         /* Midnight */
  --ink-soft: #4d6178;
  --accent-1: #4040d9;    /* Electric Blue */
  --accent-2: #ff5a4d;    /* Helix Orange */
  --accent-3: #914796;    /* Plum */
  --accent-4: #264580;    /* Medium Blue */
  --card-bg: #fffffe;
  --shadow: rgba(5, 33, 64, 0.16);
}
:root[data-theme="dark"] {
  --paper: #071a2c; --paper-line: #16304a;
  --ink: #eaf1fb; --ink-soft: #9fb2c8;
  --accent-1: #8f8fff; --accent-2: #ff8a7d;
  --accent-3: #d68fda; --accent-4: #7fa0d6;
  --card-bg: #0d2038; --shadow: rgba(0,0,0,0.45);
}
```

Brand guide rules to respect (these came from the actual BMC Helix brand book, not house style — don't relax them for convenience):

- **Orange (`accent-2`) is an accent only** — use it for the underline rule, a highlighted phrase, and a couple of card borders in rotation, never as a dominant background or majority of the palette.
- **Midnight (`--ink`) carries most of the text weight** — it's the "instead of black" color for this brand.
- **No more than 3 brand colors together in one layout** at a time (the accent rotation across 4-6 cards is fine since each card only shows one accent, but don't introduce a 5th distinct hue beyond the 4 accents + ink/paper).
- Sky (`#edfbff`) and Lilac (`#758ce5`) are available as additional light-tint options if a layout needs a fifth tone for balance (e.g. Comparison template's two-column backgrounds) — pull from `references/layouts.md`'s Comparison spec for that case.
