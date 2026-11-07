"""Build the static portfolio pages into public/portfolio/.

Each page body lives in portfolio-src/pages/<slug>.html. Its first lines are
front matter:  title: ... / desc: ... / nav: ...  then a line with ---.
Run:  python portfolio-src/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "public" / "portfolio"
SITE = "https://victoriaolamide.com"

PAGES = {
    "home": "",
    "resume": "resume",
    "work": "work",
    "achievements": "achievements",
    "ai-systems": "ai-systems",
    "about": "about",
}
NAV = [
    ("home", "Home", "/portfolio"),
    ("resume", "Résumé", "/portfolio/resume"),
    ("work", "My Work", "/portfolio/work"),
    ("ai-systems", "AI Systems", "/portfolio/ai-systems"),
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
      <span class="brand-mark">VO</span><span class="brand-name">Victoria Olamide</span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav-links"><span>Menu</span></button>
    <ul class="nav-links" id="nav-links">
{nav}
      <li class="nav-cta"><a class="btn btn-dark btn-s" href="mailto:hello@victoriaolamide.com?subject=Let%27s%20talk">Let's talk <span class="arrow">&rarr;</span></a></li>
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
    <p>Open to senior product marketing, go-to-market leadership and AI product roles with remote-first teams worldwide, plus selected advisory and founding-team conversations.</p>
    <div class="cta-row">
      <a class="btn btn-cream" href="mailto:hello@victoriaolamide.com?subject=Let%27s%20talk">Email me <span class="arrow">&rarr;</span></a>
      <a class="btn btn-line" href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn &nearr;</a>
      <a class="btn btn-line" href="/portfolio/Victoria-Olamide-CV.pdf" download>Download CV &darr;</a>
    </div>
  </div>
</section>
</main>
<footer class="foot">
  <div class="wrap">
    <span>&copy; 2026 Victoria Olamide &middot; Lagos, Nigeria &middot; Working remotely worldwide</span>
    <nav aria-label="Footer">
      <a href="/">Main website</a>
      <a href="https://opptiq.victoriaolamide.com" target="_blank" rel="noopener">Opptiq</a>
      <a href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn</a>
      <a href="mailto:hello@victoriaolamide.com">hello@victoriaolamide.com</a>
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
        path = f"/portfolio/{sub}".rstrip("/")
        html = LAYOUT.format(
            title=meta["title"], desc=meta["desc"], url=SITE + path, site=SITE,
            nav=nav, body=body.strip(), v=v,
            cta_eyebrow=meta.get("cta", "Let's work together"),
        )
        target = OUT / sub / "index.html" if sub else OUT / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print("built", target.relative_to(OUT.parent.parent))


if __name__ == "__main__":
    main()
