"""Build the static portfolio pages into public/portfolio/.

Each page body lives in portfolio-src/pages/<slug>.html. Its first lines are
front matter:  title: ... / desc: ... / nav: ...  then a line with ---.
Run:  python portfolio-src/build.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from logo import monogram

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "public" / "portfolio"
SITE = "https://victoriaolamide.com"
CALENDLY = "https://calendly.com/hello-victoriaolamide/30min"

PAGES = {
    "product-marketing": "product-marketing",
    "resume": "resume",
    "work": "work",
    "achievements": "achievements",
    "ai-systems": "ai-systems",
    "about": "about",
}
NAV = [
    ("product-marketing", "Home", "/portfolio/product-marketing"),
    ("resume", "Résumé", "/portfolio/resume"),
    ("work", "My Work", "/portfolio/work"),
    ("ai-systems", "AI Agents", "/portfolio/ai-systems"),
    ("achievements", "Key Achievements", "/portfolio/achievements"),
    ("about", "About", "/portfolio/about"),
]

LAYOUT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="author" content="Victoria Olamide" />
<link rel="canonical" href="{url}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{site}/portfolio/img/og-portfolio.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="theme-color" content="#1a1409" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Manrope:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&family=Fraunces:ital,opsz,wght@0,9..144,400;1,9..144,400;1,9..144,500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/portfolio/assets/portfolio.css?v={v}" />
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="/portfolio" aria-label="Victoria Olamide portfolio home">
      {logo}<span class="brand-name">Victoria Olamide</span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav-links"><span>Menu</span></button>
    <ul class="nav-links" id="nav-links">
{nav}
      <li class="nav-cta"><a class="btn btn-dark btn-s" href="{cal}" target="_blank" rel="noopener">Book a call <span class="arrow">&rarr;</span></a></li>
    </ul>
  </div>
</header>
<main id="main">
{body}
<section class="cta-band">
  <div class="contour"></div>
  <div class="wrap cta-inner">
    <span class="eyebrow">{cta_eyebrow}</span>
    <h2>Let's build what comes <em class="s">next.</em></h2>
    <p>Open to product marketing roles with US and UK startups, and to building AI agents for businesses that want to grow.</p>
    <div class="cta-row">
      <a class="btn btn-cream" href="{cal}" target="_blank" rel="noopener">Book a strategy call <span class="arrow">&rarr;</span></a>
      <a class="btn btn-line" href="mailto:hello@victoriaolamide.com?subject=Hello%20Victoria">Send an email &rarr;</a>
      <a class="btn btn-line" href="/portfolio/Victoria-Olamide-CV.pdf" download>Download CV &darr;</a>
    </div>
  </div>
</section>
</main>
<footer class="foot">
  <div class="wrap">
    <span>&copy; 2026 Victoria Olamide &middot; Founder, Creataws Ltd (Opptiq) &middot; Open to roles with US and UK startups</span>
    <nav aria-label="Footer">
      <a href="/">Main website</a>
      <a href="https://opptiq.victoriaolamide.com" target="_blank" rel="noopener">Opptiq</a>
      <a href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn</a>
      <a href="mailto:hello@victoriaolamide.com?subject=Hello%20Victoria">Send an email</a>
    </nav>
  </div>
</footer>
<script src="/portfolio/assets/portfolio.js?v={v}" defer></script>
</body>
</html>
"""


def main() -> None:
    import time
    v = str(int(time.time()))
    for slug, sub in PAGES.items():
        raw = (ROOT / "pages" / f"{slug}.html").read_text(encoding="utf-8")
        head, body = raw.split("\n---\n", 1)
        meta = dict(line.split(": ", 1) for line in head.strip().splitlines())
        cur = ' aria-current="page"'
        nav = "\n".join(
            f'      <li><a href="{href}"{cur if key == slug else ""}>{label}</a></li>'
            for key, label, href in NAV
        )
        import re
        from scenes import render
        from scenes import icon as _icon, GOLD as _GOLD
        counter = {"n": 0}

        def _scene(m):
            counter["n"] += 1
            svg = render(m.group(1))
            sfx = f"-u{counter['n']}"
            svg = re.sub(r'id="([^"]+)"', lambda k: f'id="{k.group(1)}{sfx}"', svg)
            svg = re.sub(r'url\(#([^)]+)\)', lambda k: f'url(#{k.group(1)}{sfx})', svg)
            svg = re.sub(r'href="#([^"]+)"', lambda k: f'href="#{k.group(1)}{sfx}"', svg)
            return svg

        body = re.sub(r"\{\{scene:([a-z]+)\}\}", _scene, body)
        body = re.sub(r"\{\{icon:([a-z]+)\}\}", lambda m: '<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true">' + _icon(m.group(1), 12, 12, 24, _GOLD) + "</svg>", body)
        body = body.replace("{{calendly}}", CALENDLY)
        import content as _c
        for key in ("testimonials", "tools", "library", "library_count"):
            body = body.replace("{{" + key + "}}", getattr(_c, key)())
        path = f"/portfolio/{sub}".rstrip("/")
        html = LAYOUT.format(
            title=meta["title"], desc=meta["desc"], url=SITE + path, site=SITE,
            nav=nav, body=body.strip(), v=v, cal=CALENDLY, logo=monogram(38, uid='nav'),
            cta_eyebrow=meta.get("cta", "Let's work together"),
        )
        target = OUT / sub / "index.html" if sub else OUT / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print("built", target.relative_to(OUT.parent.parent))


def build_hub() -> None:
    import time
    raw = (ROOT / "pages" / "hub.html").read_text(encoding="utf-8")
    html = raw.replace("{{logo}}", monogram(76, uid="hub")).replace("{{calendly}}", CALENDLY).replace("{{v}}", str(int(time.time())))
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print("built public/portfolio/index.html (hub)")


if __name__ == "__main__":
    main()
    build_hub()
