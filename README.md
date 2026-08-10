# Handwritten Note Skill

A Claude Code skill that turns any topic or concept into a simple, visual explainer —
rendered as a modern "hand-drawn note" style page (or other layouts), auto-selecting
the best layout template for the topic's shape.

## Status

Skill implemented. See `skill/SKILL.md` for the workflow, `skill/references/layouts.md`
for the six layout templates, and `skill/references/brands.md` for the six visual brands.

## Layout templates (planned)

- **Flow / Steps** — linear process, numbered cards connected by arrows
- **Cycle / Loop** — process that repeats, arrows loop back to the start
- **Hub & Spoke** — one core concept with related ideas branching out
- **Comparison / Before-After** — two things contrasted directly
- **Timeline** — chronological milestones
- **Layered / Stack** — things that sit on top of each other (architecture-style)

The skill auto-picks the layout based on the topic's shape.

## Visual brand options (planned)

The skill asks which brand to use each time (not auto-picked):

- **Field Notes** — warm cream paper, handwritten font, teal/coral/gold/plum rotation
- **Chalkboard** — dark board, chalk-white ink, pastel chalk accents
- **Sticky Wall** — sticky-note colored cards on a light background
- **Ink & Marker** — stark white, bold black lettering, single loud accent
- **Midnight Notebook** — dark navy background, gold/cyan ink
- **BMC Helix** — hand-drawn styling/layout, recolored with the BMC Helix brand
  palette (Orange `#FF5A4D`, Midnight `#052140`, Electric Blue `#4040D9`,
  Plum `#914796`, Medium Blue `#264580`, Sky `#EDFBFF`, Cloud `#F7F8FD`)

## Directory structure

```
handwritten-note-skill/
├── README.md
├── skill/
│   ├── SKILL.md              # workflow: pick layout, pick brand, build, check
│   └── references/
│       ├── layouts.md        # 6 layout template skeletons
│       └── brands.md         # 6 visual brand token sets
└── examples/                 # reference outputs (Flow template, two brands)
```
