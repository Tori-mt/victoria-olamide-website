"""Animated SVG scenes for the portfolio (brand chocolate + gold).

Each scene is an inline SVG with SMIL animations, so it needs no JavaScript.
Use in a page body as  {{scene:NAME}}  ; build.py swaps in the SVG.
"""

GOLD = "#f0a020"
SOFT = "#f6c86a"
CREAM = "#fbf7ef"
DIM = "rgba(251,247,239,.38)"

ICONS = {
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c1-3.5 3.5-5.5 6.5-5.5s5.5 2 6.5 5.5"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.5c2 .8 3.2 2.6 3.8 5.5"/>',
    "megaphone": '<path d="M3 10v4h3l6 4V6L6 10z"/><path d="M15.5 9a4 4 0 0 1 0 6M18.5 6a8 8 0 0 1 0 12"/>',
    "check": '<path d="M5 12.5l4.2 4.2L19 7"/>',
    "card": '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M7 15h4"/>',
    "ticket": '<path d="M4 7h16v3a2 2 0 0 0 0 4v3H4v-3a2 2 0 0 0 0-4z"/><path d="M14 7v10" stroke-dasharray="2 2"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>',
    "flask": '<path d="M9 3h6M10 3v6l-5.5 9.5A1.8 1.8 0 0 0 6 21h12a1.8 1.8 0 0 0 1.5-2.5L14 9V3"/><path d="M7.5 15h9"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18.5h2"/>',
    "handset": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    "missed": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/><path d="M15 3l6 6M21 3l-6 6"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M9 15.5l2 2 4-4"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    "bot": '<rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 4.5V8M9.5 13h.01M14.5 13h.01M2.5 13v2M21.5 13v2"/><circle cx="12" cy="3.5" r="1"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "file": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 13h6M9 17h4"/>',
    "db": '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "chart": '<path d="M4 20V11M10 20V5M16 20v-7M3 20h18"/>',
    "play": '<path d="M8 5v14l11-7z"/>',
    "spark": '<path d="M12 3l1.8 5.4L19 10l-5.2 1.6L12 17l-1.8-5.4L5 10l5.2-1.6z"/>',
    "wave": '<path d="M3 12h2M7 8v8M11 5v14M15 8v8M19 10v4M21 12h0"/>',
    "code": '<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>',
}


def icon(name, x, y, size=26, color=CREAM, sw=1.7):
    s = size / 24
    return (f'<g transform="translate({x - size / 2:.1f},{y - size / 2:.1f}) scale({s:.3f})" fill="none" '
            f'stroke="{color}" stroke-width="{sw / s:.2f}" stroke-linecap="round" stroke-linejoin="round">'
            f'{ICONS[name]}</g>')


def node(x, y, r, ic, glow=False, size=None, color=CREAM, ring=GOLD):
    out = ""
    if glow:
        out += (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{GOLD}" stroke-opacity=".5">'
                f'<animate attributeName="r" values="{r};{r + 16}" dur="2.4s" repeatCount="indefinite"/>'
                f'<animate attributeName="stroke-opacity" values=".55;0" dur="2.4s" repeatCount="indefinite"/></circle>')
    out += (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#241a0b" stroke="{ring}" stroke-width="1.4"/>'
            + icon(ic, x, y, size or r * 1.05, color))
    return out


def label(x, y, text, anchor="middle", color=DIM, size=9):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="DM Mono, monospace" '
            f'font-size="{size}" letter-spacing="1.6" fill="{color}">{text}</text>')


def flow(pid, d, n=3, dur=2.4, r=2.6, color=GOLD, line=True):
    out = ""
    if line:
        out += (f'<path id="{pid}" d="{d}" fill="none" stroke="{GOLD}" stroke-opacity=".28" '
                f'stroke-width="1.2" stroke-dasharray="3 5"><animate attributeName="stroke-dashoffset" '
                f'values="16;0" dur="1s" repeatCount="indefinite"/></path>')
    else:
        out += f'<path id="{pid}" d="{d}" fill="none" stroke="none"/>'
    for i in range(n):
        out += (f'<circle r="{r}" fill="{color}"><animateMotion dur="{dur}s" begin="{-i * dur / n:.2f}s" '
                f'repeatCount="indefinite"><mpath href="#{pid}"/></animateMotion>'
                f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.15;.85;1" dur="{dur}s" '
                f'begin="{-i * dur / n:.2f}s" repeatCount="indefinite"/></circle>')
    return out


def pop(inner, begin, cycle=4.0, hold=0.8):
    """Fade an element in at `begin` within a repeating cycle, keep it, fade out at the end."""
    a = begin / cycle
    b = min(a + 0.08, 0.9)
    c = hold
    return (f'<g opacity="0">{inner}<animate attributeName="opacity" values="0;0;1;1;0" '
            f'keyTimes="0;{a:.3f};{b:.3f};{c:.3f};1" dur="{cycle}s" repeatCount="indefinite"/></g>')


def frame(name, inner):
    return (
        f'<svg class="scene" viewBox="0 0 400 250" role="img" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        f'<defs><radialGradient id="bg-{name}" cx="50%" cy="45%" r="70%">'
        f'<stop offset="0" stop-color="#5a3a12"/><stop offset=".55" stop-color="#241a0b"/><stop offset="1" stop-color="#1a1409"/></radialGradient>'
        f'<pattern id="dots-{name}" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r=".8" fill="{CREAM}" fill-opacity=".09"/></pattern></defs>'
        f'<rect width="400" height="250" fill="url(#bg-{name})"/><rect width="400" height="250" fill="url(#dots-{name})"/>'
        f'{inner}</svg>'
    )


def badge(x, y, w, text, fill=GOLD, color="#1a1409"):
    return (f'<rect x="{x - w / 2}" y="{y - 11}" width="{w}" height="22" rx="11" fill="{fill}"/>'
            f'<text x="{x}" y="{y + 3.5}" text-anchor="middle" font-family="DM Mono, monospace" font-size="9.5" '
            f'font-weight="500" letter-spacing="1.4" fill="{color}">{text}</text>')


# ---------------------------------------------------------------- scenes

def s_launch():
    n = "launch"
    g = node(70, 120, 30, "megaphone", glow=True)
    g += flow(f"{n}-a", "M100 120 C150 120 160 120 200 120", n=4, dur=1.6)
    # funnel
    g += ('<path d="M190 82h64l-22 34v26l-20 10v-36z" fill="#2b2010" stroke="#f0a020" stroke-width="1.4" stroke-linejoin="round"/>')
    for i, (x, y) in enumerate([(205, 70), (222, 62), (239, 70)]):
        g += pop(icon("user", x, y, 14, SOFT), 0.3 * i, cycle=3.2, hold=0.85)
    g += flow(f"{n}-b", "M222 152 C240 175 290 175 312 150", n=2, dur=1.8)
    g += node(330, 120, 30, "card", ring=GOLD)
    g += pop(f'<circle cx="352" cy="96" r="10" fill="{GOLD}"/>' + icon("check", 352, 96, 13, "#1a1409", 2.4), 1.6, cycle=3.2, hold=0.9)
    g += label(70, 178, "LAUNCH") + label(222, 192, "SIGN-UPS") + label(330, 178, "PAID")
    return frame(n, g)


def s_community():
    n = "community"
    cx, cy = 200, 118
    import math
    pts = [(cx + 105 * math.cos(a), cy + 72 * math.sin(a)) for a in [i * math.pi / 4 + .3 for i in range(8)]]
    g = ""
    for i, (x, y) in enumerate(pts):
        g += pop(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{GOLD}" stroke-opacity=".35" stroke-dasharray="3 4"/>'
                 + node(round(x), round(y), 14, "user", size=14, ring="rgba(240,160,32,.7)"), 0.35 * i, cycle=4.4, hold=0.88)
    g += node(cx, cy, 30, "users", glow=True, size=30)
    g += label(cx, 236, "CREATORS · COMMUNITY · USERS")
    return frame(n, g)


def s_event():
    n = "event"
    g = ('<g transform="translate(34 70)"><path d="M0 0h120v38a14 14 0 0 0 0 28v38H0V66a14 14 0 0 0 0-28z" fill="#2b2010" stroke="#f0a020" stroke-width="1.4"/>'
         '<path d="M86 6v92" stroke="#f0a020" stroke-opacity=".5" stroke-dasharray="3 4"/></g>')
    g += icon("ticket", 80, 106, 30, SOFT) + label(94, 196, "REGISTER")
    # clock with sweeping hand
    g += (f'<circle cx="200" cy="58" r="20" fill="#241a0b" stroke="{GOLD}" stroke-width="1.4"/>'
          f'<line x1="200" y1="58" x2="200" y2="44" stroke="{CREAM}" stroke-width="1.8" stroke-linecap="round">'
          f'<animateTransform attributeName="transform" type="rotate" from="0 200 58" to="360 200 58" dur="3s" repeatCount="indefinite"/></line>')
    g += label(200, 96, "COUNTDOWN")
    g += flow(f"{n}-a", "M182 118 C210 118 220 118 236 118", n=3, dur=1.4)
    # seats filling
    k = 0
    for r in range(4):
        for c in range(6):
            x, y = 250 + c * 20, 86 + r * 22
            g += f'<rect x="{x}" y="{y}" width="14" height="14" rx="4" fill="none" stroke="{CREAM}" stroke-opacity=".22"/>'
            g += pop(f'<rect x="{x}" y="{y}" width="14" height="14" rx="4" fill="{GOLD}"/>', 0.12 * k, cycle=4.2, hold=0.9)
            k += 1
    g += label(306, 196, "ATTEND")
    return frame(n, g)


def s_expansion():
    n = "expansion"
    g = (f'<g opacity=".9">{icon("globe", 140, 122, 150, "rgba(246,200,106,.55)", 1.1)}</g>')
    pins = [(98, 92), (168, 80), (150, 150), (196, 128)]
    arcs = ["M98 92 Q130 50 168 80", "M168 80 Q205 95 196 128", "M196 128 Q180 165 150 150"]
    for i, d in enumerate(arcs):
        g += flow(f"{n}-{i}", d, n=1, dur=2.2)
    for i, (x, y) in enumerate(pins):
        g += pop(f'<circle cx="{x}" cy="{y}" r="5" fill="{GOLD}"/><circle cx="{x}" cy="{y}" r="9" fill="none" stroke="{GOLD}" stroke-opacity=".5"/>', 0.4 * i, cycle=3.6, hold=0.92)
    # adoption bars
    for i, h in enumerate([34, 52, 72, 98]):
        x = 262 + i * 26
        g += (f'<rect x="{x}" y="{190 - h}" width="16" height="{h}" rx="3" fill="url(#bar-{n})">'
              f'<animate attributeName="height" values="0;{h};{h}" keyTimes="0;.4;1" dur="3.6s" begin="{i * .2}s" repeatCount="indefinite"/>'
              f'<animate attributeName="y" values="190;{190 - h};{190 - h}" keyTimes="0;.4;1" dur="3.6s" begin="{i * .2}s" repeatCount="indefinite"/></rect>')
    g = g.replace("</svg>", "")
    g = f'<defs><linearGradient id="bar-{n}" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#d9781a"/><stop offset="1" stop-color="{SOFT}"/></linearGradient></defs>' + g
    g += f'<line x1="254" y1="190" x2="370" y2="190" stroke="{CREAM}" stroke-opacity=".25"/>'
    g += label(140, 226, "MARKET ENTRY · PARTNERS") + label(313, 214, "ADOPTION")
    return frame(n, g)


def s_experiments():
    n = "experiments"
    g = ""
    for i, x in enumerate([92, 200, 308]):
        win = i == 1
        body = (f'<rect x="{x - 44}" y="70" width="88" height="104" rx="12" fill="#2b2010" stroke="{GOLD if win else "rgba(251,247,239,.25)"}" stroke-width="1.4"/>'
                f'<text x="{x}" y="96" text-anchor="middle" font-family="Syne, sans-serif" font-weight="700" font-size="18" fill="{SOFT if win else DIM}">{"ABC"[i]}</text>'
                f'<rect x="{x - 28}" y="112" width="56" height="5" rx="2.5" fill="{CREAM}" fill-opacity=".18"/>'
                f'<rect x="{x - 28}" y="124" width="40" height="5" rx="2.5" fill="{CREAM}" fill-opacity=".12"/>')
        if win:
            body = (f'<g>{body}<animateTransform attributeName="transform" type="translate" values="0 0;0 -12;0 -12;0 0" '
                    f'keyTimes="0;.3;.8;1" dur="3.4s" repeatCount="indefinite"/></g>')
            body += pop(f'<circle cx="{x + 38}" cy="66" r="11" fill="{GOLD}"/>' + icon("check", x + 38, 66, 14, "#1a1409", 2.4), 1.1, cycle=3.4, hold=0.8)
        g += body
    g += icon("flask", 200, 205, 22, SOFT)
    g += label(92, 205, "TEST") + label(308, 205, "SCALE")
    return frame(n, g)


def s_cohort():
    n = "cohort"
    days = ["MON", "TUE", "WED", "THU", "FRI"]
    g = ""
    for i, d in enumerate(days):
        x = 60 + i * 70
        g += f'<rect x="{x - 26}" y="58" width="52" height="58" rx="10" fill="#2b2010" stroke="rgba(251,247,239,.22)"/>'
        g += label(x, 78, d, color=DIM)
        g += pop(f'<rect x="{x - 26}" y="58" width="52" height="58" rx="10" fill="none" stroke="{GOLD}" stroke-width="1.6"/>'
                 + icon("play", x, 98, 16, GOLD), 0.55 * i, cycle=4.0, hold=0.92)
    for i in range(7):
        x = 110 + i * 30
        g += pop(node(x, 170, 12, "user", size=13, ring="rgba(240,160,32,.6)"), 0.2 + 0.18 * i, cycle=4.0, hold=0.92)
    g += label(200, 220, "LIVE COHORT · GUEST SPEAKERS")
    return frame(n, g)


def s_sales():
    n = "sales"
    g = node(70, 112, 28, "user")
    g += label(70, 166, "LEAD")
    # voice waveform bars
    for i in range(9):
        x = 130 + i * 10
        h = [10, 22, 34, 18, 40, 26, 14, 30, 12][i]
        g += (f'<rect x="{x}" y="{112 - h / 2}" width="5" height="{h}" rx="2.5" fill="{GOLD}">'
              f'<animate attributeName="height" values="{h};{h * .35:.0f};{h}" dur="{0.8 + (i % 3) * .25:.2f}s" repeatCount="indefinite"/>'
              f'<animate attributeName="y" values="{112 - h / 2};{112 - h * .175:.0f};{112 - h / 2}" dur="{0.8 + (i % 3) * .25:.2f}s" repeatCount="indefinite"/></rect>')
    g += node(260, 112, 28, "bot", glow=True)
    g += label(195, 166, "AI SALES CALL")
    g += flow(f"{n}-a", "M290 112 C310 112 314 112 326 112", n=2, dur=1.2)
    g += f'<rect x="328" y="84" width="54" height="56" rx="9" fill="#2b2010" stroke="{GOLD}" stroke-width="1.3"/>'
    for i in range(3):
        g += pop(f'<rect x="336" y="{94 + i * 14}" width="38" height="7" rx="3.5" fill="{SOFT if i == 0 else "rgba(251,247,239,.25)"}"/>', 0.4 + 0.35 * i, cycle=3.4, hold=0.9)
    g += pop(badge(330, 196, 92, "QUALIFIED"), 1.5, cycle=3.4, hold=0.9)
    g += label(355, 160, "CRM")
    return frame(n, g)


def s_support():
    n = "support"
    g = f'<rect x="110" y="34" width="180" height="182" rx="16" fill="#2b2010" stroke="{GOLD}" stroke-width="1.3"/>'
    g += f'<rect x="110" y="34" width="180" height="34" rx="16" fill="#3a2a12"/><rect x="110" y="52" width="180" height="16" fill="#3a2a12"/>'
    g += node(132, 51, 10, "bot", size=13) + label(150, 55, "ASK DASHIE", anchor="start", color=SOFT, size=8.5)
    bubbles = [(128, 82, 104, False), (168, 112, 104, True), (128, 142, 120, False)]
    for i, (x, y, w, me) in enumerate(bubbles):
        fill = GOLD if me else "rgba(251,247,239,.14)"
        g += pop(f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="11" fill="{fill}"/>'
                 f'<rect x="{x + 12}" y="{y + 9}" width="{w - 40}" height="4" rx="2" fill="{"#1a1409" if me else CREAM}" fill-opacity=".55"/>',
                 0.7 * i, cycle=4.6, hold=0.9)
    # typing dots
    for i in range(3):
        g += (f'<circle cx="{140 + i * 9}" cy="186" r="3" fill="{SOFT}"><animate attributeName="opacity" values=".2;1;.2" dur="1s" begin="{i * .2}s" repeatCount="indefinite"/></circle>')
    g += pop(badge(322, 186, 84, "RESOLVED"), 2.6, cycle=4.6, hold=0.9)
    g += node(60, 125, 22, "user") + label(60, 165, "CUSTOMER")
    g += flow(f"{n}-a", "M84 125 C96 125 100 125 110 125", n=1, dur=1.2)
    return frame(n, g)


def s_voice():
    n = "voice"
    g = pop(node(70, 120, 22, "missed", ring="rgba(251,247,239,.4)") + label(70, 162, "MISSED"), 0, cycle=3.6, hold=0.95)
    g += flow(f"{n}-a", "M95 120 C130 120 140 120 168 120", n=2, dur=1.3)
    # phone with rings
    for i in range(3):
        g += (f'<circle cx="200" cy="120" r="40" fill="none" stroke="{GOLD}" stroke-opacity=".5">'
              f'<animate attributeName="r" values="40;84" dur="2.4s" begin="{i * .8}s" repeatCount="indefinite"/>'
              f'<animate attributeName="stroke-opacity" values=".5;0" dur="2.4s" begin="{i * .8}s" repeatCount="indefinite"/></circle>')
    g += f'<rect x="176" y="70" width="48" height="100" rx="12" fill="#2b2010" stroke="{GOLD}" stroke-width="1.5"/>'
    g += icon("wave", 200, 116, 26, SOFT) + f'<rect x="192" y="160" width="16" height="3" rx="1.5" fill="{CREAM}" fill-opacity=".4"/>'
    g += flow(f"{n}-b", "M232 120 C260 120 270 120 300 120", n=2, dur=1.3)
    g += pop(node(330, 120, 22, "calendar", ring=GOLD) + label(330, 162, "BOOKED"), 1.4, cycle=3.6, hold=0.95)
    g += label(200, 206, "ANSWERED IN SECONDS")
    return frame(n, g)


def s_ops():
    n = "ops"
    cx, cy = 200, 122
    g = (f'<ellipse cx="{cx}" cy="{cy}" rx="140" ry="78" fill="none" stroke="{GOLD}" stroke-opacity=".22" stroke-dasharray="3 6"/>')
    sats = [("mail", 70, 100, "EMAIL"), ("calendar", 150, 48, "CALENDAR"), ("file", 262, 50, "DOCS"), ("db", 334, 104, "DATA"), ("chart", 300, 186, "REPORTS"), ("code", 104, 184, "CODE")]
    for i, (ic, x, y, lab) in enumerate(sats):
        g += flow(f"{n}-{i}", f"M{x} {y} L{cx} {cy}", n=1, dur=1.8 + i * .15, line=True)
    for ic, x, y, lab in sats:
        g += node(x, y, 18, ic, size=17, ring="rgba(240,160,32,.75)")
    g += node(cx, cy, 32, "bot", glow=True, size=32)
    g += label(cx, 238, "ONE AGENT · MANY TOOLS")
    return frame(n, g)


def s_engine():
    n = "engine"
    g = ""
    layers = [("db", "DATA"), ("bot", "AI MODEL"), ("check", "EVIDENCE"), ("file", "REPORT")]
    for i, (ic, lab) in enumerate(layers):
        y = 46 + i * 46
        g += f'<rect x="120" y="{y}" width="160" height="34" rx="10" fill="#2b2010" stroke="rgba(240,160,32,.55)"/>'
        g += icon(ic, 144, y + 17, 16, SOFT) + label(166, y + 21, lab, anchor="start", color=CREAM, size=9)
        g += pop(f'<rect x="120" y="{y}" width="160" height="34" rx="10" fill="none" stroke="{GOLD}" stroke-width="1.8"/>', 0.6 * i, cycle=3.2, hold=0.85)
    g += (f'<rect x="112" y="40" width="176" height="3" rx="1.5" fill="{GOLD}" opacity=".8">'
          f'<animate attributeName="y" values="40;214;40" dur="3.2s" repeatCount="indefinite"/></rect>')
    g += flow(f"{n}-a", "M40 125 C70 125 90 125 116 125", n=3, dur=1.4)
    g += flow(f"{n}-b", "M284 125 C310 125 330 125 360 125", n=3, dur=1.4)
    g += label(50, 150, "INPUT") + label(350, 150, "INSIGHT")
    return frame(n, g)


SCENES = {
    "launch": s_launch, "community": s_community, "event": s_event, "expansion": s_expansion,
    "experiments": s_experiments, "cohort": s_cohort, "sales": s_sales, "support": s_support,
    "voice": s_voice, "ops": s_ops, "engine": s_engine,
}


def render(name: str) -> str:
    return SCENES[name]()
