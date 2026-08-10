#!/usr/bin/env python3
"""
Regenerates every brand's "How Lightning Works" note.html in this directory
(examples/palette-catalog-lightning/<slug>/note.html) from the BRANDS list
below. Run it from anywhere: `python3 generate.py`.

To add a new brand to the palette catalog: add a dict to BRANDS with its
tokens (matching the structure of an existing entry), run this script, then
take a fresh preview.png screenshot of the new <slug>/note.html and add the
brand to index.html's swatch list. See SKILL.md's "Adding a new brand"
runbook for the full process, including everywhere else a new brand needs
to be wired in (SKILL.md's menu, README, the homepage index.html, etc).
"""
import os, string

OUT = os.path.dirname(os.path.abspath(__file__))

HANDWRITTEN = '"Bradley Hand", "Segoe Print", "Chalkboard SE", "Comic Sans MS", cursive'
BLUEPRINT_FONT = 'ui-monospace, "SF Mono", Menlo, "Segoe UI", sans-serif'

# Each brand: slug, name, light tokens, dark tokens (or None if single-theme),
# font, card_style: "border" | "tint" | "thin", shadow_style: "offset" | "glow",
# background: "ruled" | "plain" | "gradient", single_accent: bool
BRANDS = [
    dict(slug="field-notes", name="Field Notes", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="ruled", single_accent=False, single_theme=False,
         light=dict(paper="#f6f2e9", paper_line="#dcd3bf", ink="#1e2a38", ink_soft="#4a5b6b",
                    a1="#0f8b8d", a2="#e4572e", a3="#e8a33d", a4="#6a4c93", card_bg="#fffdf8", shadow="rgba(30,42,56,0.16)"),
         dark=dict(paper="#1b2027", paper_line="#323a45", ink="#eee7d8", ink_soft="#a9b4c0",
                   a1="#4fd1ce", a2="#ff8360", a3="#f2bd6c", a4="#b79ceb", card_bg="#232a33", shadow="rgba(0,0,0,0.45)")),

    dict(slug="chalkboard", name="Chalkboard", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="plain", single_accent=False, single_theme=True,
         light=dict(paper="#1c2b26", paper_line="#2c3f38", ink="#f4f1e8", ink_soft="#b9c4bd",
                    a1="#f6e05e", a2="#f6a5c0", a3="#7ec8e3", a4="#c7f0d8", card_bg="#22332d", shadow="rgba(0,0,0,0.5)"),
         dark=None),

    dict(slug="sticky-wall", name="Sticky Wall", font=HANDWRITTEN, card_style="tint", shadow_style="offset",
         background="plain", single_accent=False, single_theme=False,
         light=dict(paper="#f4f5f7", paper_line="#e3e5ea", ink="#24272b", ink_soft="#5b606a",
                    a1="#fff275", a2="#ff8fab", a3="#8ecae6", a4="#b9fbc0", card_bg="#ffffff", shadow="rgba(0,0,0,0.18)"),
         dark=dict(paper="#1a1b1e", paper_line="#2a2c30", ink="#eceef0", ink_soft="#a3a7ad",
                   a1="#d8c94a", a2="#d97a92", a3="#6fa8c4", a4="#8fd3a0", card_bg="#232427", shadow="rgba(0,0,0,0.5)")),

    dict(slug="ink-and-marker", name="Ink & Marker", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="plain", single_accent=True, single_theme=False,
         light=dict(paper="#ffffff", paper_line="#eeeeee", ink="#111111", ink_soft="#55555a",
                    a1="#ff4500", a2="#ff4500", a3="#ff4500", a4="#ff4500", card_bg="#ffffff", shadow="rgba(0,0,0,0.12)"),
         dark=dict(paper="#0c0c0d", paper_line="#1c1c1e", ink="#f2f2f2", ink_soft="#a0a0a5",
                   a1="#ff6a3d", a2="#ff6a3d", a3="#ff6a3d", a4="#ff6a3d", card_bg="#17171a", shadow="rgba(0,0,0,0.5)")),

    dict(slug="midnight-notebook", name="Midnight Notebook", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="plain", single_accent=False, single_theme=True,
         light=dict(paper="#0b1830", paper_line="#1a2b4a", ink="#f0ead6", ink_soft="#9fb0c8",
                    a1="#e8b04b", a2="#5fd4d6", a3="#c98bd6", a4="#7ea8e0", card_bg="#101f3d", shadow="rgba(0,0,0,0.5)"),
         dark=None),

    dict(slug="bmc-helix", name="BMC Helix", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="ruled", single_accent=False, single_theme=False,
         light=dict(paper="#f7f8fd", paper_line="#dde3f0", ink="#052140", ink_soft="#4d6178",
                    a1="#4040d9", a2="#ff5a4d", a3="#914796", a4="#264580", card_bg="#fffffe", shadow="rgba(5,33,64,0.16)"),
         dark=dict(paper="#071a2c", paper_line="#16304a", ink="#eaf1fb", ink_soft="#9fb2c8",
                   a1="#8f8fff", a2="#ff8a7d", a3="#d68fda", a4="#7fa0d6", card_bg="#0d2038", shadow="rgba(0,0,0,0.45)")),

    dict(slug="terracotta-studio", name="Terracotta Studio", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="ruled", single_accent=False, single_theme=False,
         light=dict(paper="#faf3ec", paper_line="#ecdfd0", ink="#3a2a20", ink_soft="#7a6455",
                    a1="#c1502e", a2="#7c8c5a", a3="#d1a039", a4="#9c6b4f", card_bg="#fffaf4", shadow="rgba(58,42,32,0.18)"),
         dark=dict(paper="#241d18", paper_line="#362c24", ink="#f2e6d8", ink_soft="#b9a894",
                   a1="#e8734e", a2="#9db178", a3="#e8bd5c", a4="#c08a6a", card_bg="#2e2620", shadow="rgba(0,0,0,0.5)")),

    dict(slug="botanical-press", name="Botanical Press", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="ruled", single_accent=False, single_theme=False,
         light=dict(paper="#eef0e4", paper_line="#dbe0cc", ink="#223324", ink_soft="#5c6b53",
                    a1="#c98a93", a2="#a98b3e", a3="#4f6b52", a4="#8a9a6b", card_bg="#f7f8f0", shadow="rgba(34,51,36,0.16)"),
         dark=dict(paper="#1a231b", paper_line="#29352a", ink="#e7ecdd", ink_soft="#a9b8a0",
                   a1="#d99aa3", a2="#d1ab5e", a3="#7c9a7e", a4="#a7b98c", card_bg="#212b22", shadow="rgba(0,0,0,0.5)")),

    dict(slug="neon-arcade", name="Neon Arcade", font=HANDWRITTEN, card_style="border", shadow_style="glow",
         background="plain", single_accent=False, single_theme=True,
         light=dict(paper="#0a0a12", paper_line="#16162a", ink="#f5f5ff", ink_soft="#9a9ac0",
                    a1="#ff2fd0", a2="#2ff0ff", a3="#d6ff2f", a4="#7a5cff", card_bg="#131324", shadow="rgba(0,0,0,0.6)"),
         dark=None),

    dict(slug="newsprint", name="Newsprint", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="plain", single_accent=True, single_theme=False,
         light=dict(paper="#f2ede1", paper_line="#ded5c2", ink="#1a1a1a", ink_soft="#55524a",
                    a1="#b0281f", a2="#b0281f", a3="#b0281f", a4="#b0281f", card_bg="#faf7ef", shadow="rgba(0,0,0,0.15)"),
         dark=dict(paper="#1c1a16", paper_line="#2c2924", ink="#ece7da", ink_soft="#a39d8d",
                   a1="#e0473c", a2="#e0473c", a3="#e0473c", a4="#e0473c", card_bg="#24211c", shadow="rgba(0,0,0,0.5)")),

    dict(slug="pastel-lab", name="Pastel Lab", font=HANDWRITTEN, card_style="thin", shadow_style="offset",
         background="plain", single_accent=False, single_theme=False,
         light=dict(paper="#fbfbfd", paper_line="#ecedf3", ink="#2a2d3a", ink_soft="#6b7080",
                    a1="#b8a4e3", a2="#9fd8c4", a3="#a8cbef", a4="#f3b8a0", card_bg="#ffffff", shadow="rgba(30,32,45,0.10)"),
         dark=dict(paper="#191a22", paper_line="#262835", ink="#eceefb", ink_soft="#a7abc2",
                   a1="#c9b8ee", a2="#a9e6d2", a3="#b9d9f5", a4="#f6c8b3", card_bg="#21232f", shadow="rgba(0,0,0,0.5)")),

    dict(slug="blueprint", name="Blueprint", font=BLUEPRINT_FONT, card_style="thin", shadow_style="offset",
         background="plain", single_accent=False, single_theme=True,
         light=dict(paper="#163a63", paper_line="#1f4a7a", ink="#eaf3fb", ink_soft="#9fc2df",
                    a1="#7fd4e8", a2="#ffffff", a3="#bfe3ef", a4="#4fa8c9", card_bg="#123054", shadow="rgba(0,0,0,0.4)"),
         dark=None),

    dict(slug="sunset-deck", name="Sunset Deck", font=HANDWRITTEN, card_style="border", shadow_style="offset",
         background="gradient", gradient="linear-gradient(180deg, #241633 0%, #6a3a52 55%, #b5603f 100%)",
         single_accent=False, single_theme=True,
         light=dict(paper="#3b2249", paper_line="#4a2f5c", ink="#fbeee0", ink_soft="#d9c2d0",
                    a1="#ff8a5b", a2="#e2b33b", a3="#c15b7c", a4="#8a6bb0", card_bg="#4a2f5c", shadow="rgba(0,0,0,0.35)"),
         dark=None),

    dict(slug="night-flight", name="Night Flight", font=HANDWRITTEN, card_style="thin", shadow_style="offset",
         background="gradient",
         gradient="linear-gradient(180deg, #131a4d 0%, #2b2d76 22%, #5b3f8f 45%, #9a5a94 68%, #c98a9d 85%, #dba7ab 100%)",
         grain=True, single_accent=False, single_theme=True,
         light=dict(paper="#1c2350", paper_line="rgba(246,236,217,0.14)", ink="#f6ecd9", ink_soft="#cdbcd6",
                    a1="#d1425a", a2="#f2c14e", a3="#5fd6c8", a4="#8b95d9", card_bg="#1c2350", shadow="rgba(0,0,0,0.45)"),
         dark=None),
]

STEPS = [
    ("1", "accent-1", "the setup", "Charge Separation",
     "Inside a storm cloud, ice and hail collide over and over, knocking electrons loose. Negative charge sinks to the cloud's base; positive charge piles up near the top and on the ground below.",
     "opposite charges, building tension"),
    ("2", "accent-2", "reaching down", "Stepped Leader",
     "An invisible, forked channel of negative charge zigzags downward in tiny, fast steps — feeling out a path toward the ground, branching as it goes.",
     "invisible to the eye, still traveling"),
    ("3", "accent-3", "reaching up", "Upward Streamer",
     "Sensing it coming, positive charge rises up to meet it — from trees, buildings, towers, even people standing in the open.",
     "the ground answers back"),
    ("4", "accent-4", "contact", "Return Stroke",
     "The instant they connect, a massive surge of current rushes back up that path at roughly a third the speed of light. This is the bright flash you actually see.",
     "~100 million volts, in microseconds"),
    ("5", "accent-1", "the aftermath", "Thunder",
     "The stroke heats the air along its path to about 30,000 K — five times the surface of the Sun — and that air explosively expands. We hear the shockwave as thunder, arriving late because sound is much slower than light.",
     "count the seconds to guess the distance"),
]

def brand_css(b):
    L, D = b["light"], b["dark"]
    def tokens(t):
        return f"""--paper: {t['paper']};
    --paper-line: {t['paper_line']};
    --ink: {t['ink']};
    --ink-soft: {t['ink_soft']};
    --accent-1: {t['a1']};
    --accent-2: {t['a2']};
    --accent-3: {t['a3']};
    --accent-4: {t['a4']};
    --card-bg: {t['card_bg']};
    --shadow: {t['shadow']};"""
    css = f":root {{\n    {tokens(L)}\n  }}\n"
    if not b["single_theme"] and D:
        css += f"""  :root[data-theme="dark"] {{
    {tokens(D)}
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      {tokens(D)}
    }}
  }}
"""
    return css

def background_css(b):
    if b["background"] == "ruled":
        return """background:
      repeating-linear-gradient(0deg, transparent, transparent 34px, var(--paper-line) 35px),
      var(--paper);"""
    if b["background"] == "gradient":
        return f"background: {b.get('gradient', 'linear-gradient(180deg, #241633 0%, #6a3a52 55%, #b5603f 100%)')};"
    return "background: var(--paper);"

def grain_css(b):
    if not b.get("grain"):
        return ""
    return """body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    opacity: 0.16;
    mix-blend-mode: overlay;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
    background-size: 180px 180px;
  }"""

def card_css(b):
    if b["card_style"] == "tint":
        return """.card {
    background: color-mix(in srgb, var(--card-color, var(--accent-1)) 22%, var(--card-bg));
    border: 2px solid var(--card-color, var(--accent-1));
    border-radius: 12px;
    padding: 16px 18px 18px;
    box-shadow: 5px 7px 0 var(--shadow);
    transform: rotate(var(--tilt, -0.6deg));
  }"""
    if b["card_style"] == "thin":
        return """.card {
    background: var(--card-bg);
    border: 1.5px solid var(--ink);
    border-radius: 10px;
    padding: 16px 18px 18px;
    box-shadow: 2px 3px 0 var(--shadow);
  }
  .card .accent-fill { background: color-mix(in srgb, var(--card-color, var(--accent-1)) 30%, transparent); border-radius: 8px; padding: 2px 8px; display: inline-block; }"""
    # default "border"
    shadow_rule = "box-shadow: 4px 6px 0 var(--shadow);" if b["shadow_style"] == "offset" else \
                  "box-shadow: 0 0 14px var(--card-color, var(--accent-1)), 0 0 2px var(--card-color, var(--accent-1)) inset;"
    return f""".card {{
    background: var(--card-bg);
    border: 2.5px solid var(--card-color, var(--accent-1));
    border-radius: 14px 16px 15px 14px / 16px 14px 17px 13px;
    padding: 18px 20px 20px;
    {shadow_rule}
    transform: rotate(var(--tilt, -0.6deg));
  }}"""

def underline_glow(b):
    if b["shadow_style"] == "glow":
        return "filter: drop-shadow(0 0 6px var(--accent-2));"
    return ""

TEMPLATE = string.Template("""<meta charset="utf-8">
<title>How Lightning Works — $brand_name</title>
<style>
  $brand_css
  * { box-sizing: border-box; }
  html, body { height: 100%; }
  body {
    margin: 0;
    min-height: 100%;
    position: relative;
    $background_css
    color: var(--ink);
    font-family: $font;
    padding: 32px 20px 48px;
  }
  $grain_css
  .sheet { max-width: 1080px; margin: 0 auto; position: relative; z-index: 1; }
  .label {
    font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
    text-transform: uppercase; letter-spacing: 0.16em; font-size: 0.66rem; font-weight: 700;
    color: var(--ink-soft); text-align: center;
  }
  h1 { font-size: clamp(2rem, 4.2vw, 3rem); text-align: center; margin: 6px 0 4px; text-wrap: balance; }
  .underline-svg { display: block; margin: -4px auto 26px; width: min(460px, 76%); $underline_glow }
  .intro {
    max-width: 640px; margin: 0 auto 34px; text-align: center;
    font-size: 1.08rem; color: var(--ink-soft); line-height: 1.5;
  }
  .intro b { color: var(--accent-2); }
  .row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 26px; margin-bottom: 26px; }
  .row.two { grid-template-columns: repeat(2, 1fr); max-width: 720px; margin-left: auto; margin-right: auto; }
  $card_css
  .card .num {
    font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
    font-weight: 800; font-size: 0.68rem; letter-spacing: 0.08em; text-transform: uppercase;
    color: var(--card-color, var(--accent-1)); display: flex; align-items: center; gap: 6px; margin-bottom: 6px;
  }
  .card .num .dot {
    width: 20px; height: 20px; border-radius: 50%;
    background: var(--card-color, var(--accent-1)); color: var(--card-bg);
    display: inline-flex; align-items: center; justify-content: center; font-size: 0.66rem; font-family: inherit;
  }
  .card h3 { margin: 0 0 6px; font-size: 1.22rem; color: var(--ink); }
  .card p { margin: 0; font-size: 0.98rem; line-height: 1.42; color: var(--ink-soft); }
  .card .egg { margin-top: 10px; font-size: 0.86rem; color: var(--card-color, var(--accent-1)); font-weight: 700; }
  .footer-banner {
    margin-top: 8px; text-align: center; border: 2.5px solid var(--accent-3);
    border-radius: 40px; padding: 14px 24px; background: var(--card-bg);
    box-shadow: 4px 6px 0 var(--shadow); font-size: 1.05rem;
  }
  .footer-banner .accent { color: var(--accent-3); font-weight: 700; }
  @media (max-width: 860px) { .row, .row.two { grid-template-columns: 1fr; } }
</style>

<div class="sheet">
  <div class="label">a field note on</div>
  <h1>How Lightning Works</h1>
  <svg class="underline-svg" viewBox="0 0 460 20" preserveAspectRatio="none">
    <path d="M4 12 C 110 3, 260 18, 456 8" fill="none" stroke="var(--accent-2)" stroke-width="4" stroke-linecap="round"/>
  </svg>

  <p class="intro">
    By the time you see the flash, the sky has already spent a fraction of a second
    <b>deciding exactly where lightning is going to strike</b>.
  </p>

  <div class="row">
    $card0
    $card1
    $card2
  </div>
  <div class="row two">
    $card3
    $card4
  </div>

  <div class="footer-banner">
    ✎ Thunder is just the <span class="accent">sound of the flash</span> — arriving late because light beats sound to your eyes first.
  </div>
</div>
""")

CARD_TEMPLATE = string.Template("""<div class="card" style="--card-color: var(--$accent); --tilt: $tilt;">
      <div class="num"><span class="dot">$num</span> $tag</div>
      <h3>$title</h3>
      <p>$body</p>
      <div class="egg">$egg</div>
    </div>""")

TILTS = ["-1.1deg", "0.9deg", "-0.7deg", "0.8deg", "-0.5deg"]

def render_brand(b):
    cards = []
    for i, (num, accent, tag, title, body, egg) in enumerate(STEPS):
        cards.append(CARD_TEMPLATE.substitute(accent=accent, tilt=TILTS[i], num=num, tag=tag, title=title, body=body, egg=egg))
    html = TEMPLATE.substitute(
        brand_name=b["name"],
        brand_css=brand_css(b),
        background_css=background_css(b),
        grain_css=grain_css(b),
        font=b["font"],
        underline_glow=underline_glow(b),
        card_css=card_css(b),
        card0=cards[0], card1=cards[1], card2=cards[2], card3=cards[3], card4=cards[4],
    )
    return html

for b in BRANDS:
    html = render_brand(b)
    brand_dir = os.path.join(OUT, b["slug"])
    os.makedirs(brand_dir, exist_ok=True)
    path = os.path.join(brand_dir, "note.html")
    with open(path, "w") as f:
        f.write(html)
    print("wrote", path)
