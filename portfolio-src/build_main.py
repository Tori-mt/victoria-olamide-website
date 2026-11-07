"""Build the main website (victoriaolamide.com) into ../index.html.

Static HTML, no framework. Reuses the animated scenes from scenes.py.
Run:  python portfolio-src/build_main.py   (then npm run build)
"""
import re
import time
from pathlib import Path

from scenes import render
from logo import monogram

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "index.html"
CAL = "https://calendly.com/hello-victoriaolamide/30min"
MAIL = "mailto:hello@victoriaolamide.com?subject=Hello%20Victoria"

RESULTS = [
    ("01", "Professional network &amp; hiring · United States", "I'll Tip", "5,000+ sign-ups. 48 hours.",
     "Led the go-to-market campaign and rollout of a new product feature: positioning, launch messaging and campaign strategy. The SOP behind it became the team's standard launch process.",
     [("5,000+", "Sign-ups in 48h"), ("~46%", "Paid conversion")]),
    ("02", "AI platform · Germany", "Viewon.AI", "45% adoption. One quarter.",
     "Led product marketing and market entry across Product, Marketing and Operations, built the adoption tracking and secured the partnerships that gave a young AI product credibility.",
     [("45%", "Q1 adoption growth"), ("5+", "Strategic partnerships")]),
    ("03", "Creator platform · Nigeria", "Endow", "Under 50 to ~600 users. Two weeks.",
     "Coordinated launch and go-to-market for a creator platform entering Nigeria, combining positioning, community-led acquisition and influencer activation.",
     [("~600", "Users in 2 weeks"), ("~12x", "User growth")]),
    ("04", "Edtech · Event growth", "Utiva", "2,000+ attendees. 72 hours.",
     "Led marketing and audience acquisition for a time-boxed event. The result turned into a repeat engagement.",
     [("2,000+", "Attendees"), ("72h", "Window")]),
    ("05", "AI product · Built &amp; launched by me", "Opptiq", "260+ organic users. Paying customers.",
     "An AI opportunity intelligence platform I specified, built, priced and launched. Two LinkedIn posts, no ads, and it is already converting users into paying customers.",
     [("260+", "Organic users"), ("0", "Ad spend")]),
    ("06", "Founders &amp; startups · Consulting", "Client portfolio", "15+ launches and growth experiments.",
     "Product marketing, monetisation and AI-enabled growth systems for founders, run across a distributed team.",
     [("15+", "Launches &amp; experiments"), ("Global", "US, UK, Europe, Asia")]),
]

AGENTS = [
    ("sales", "AI Sales Agents", "Qualify leads, follow up and update your CRM, built with ElevenLabs."),
    ("support", "AI Support Agents", "Answer customers from their own account data, with human handoff."),
    ("voice", "AI Voice Agents", "Answer every call, qualify callers and book appointments."),
    ("ops", "AI Operations Agents", "Email, scheduling, docs and data, handled across your tools."),
]


def page() -> str:
    res_html = ""
    for n, k, name, head, body, ms in RESULTS:
        m = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in ms)
        res_html += f"""
      <article class="res rv">
        <span class="n">{n}</span>
        <div><span class="k">{k}</span><h3><small>{name}</small>{head}</h3><p>{body}</p></div>
        <div class="m">{m}</div>
      </article>"""

    counter = {"n": 0}

    def scene(name):
        counter["n"] += 1
        svg = render(name)
        sfx = f"-m{counter['n']}"
        svg = re.sub(r'id="([^"]+)"', lambda k: f'id="{k.group(1)}{sfx}"', svg)
        svg = re.sub(r"url\(#([^)]+)\)", lambda k: f"url(#{k.group(1)}{sfx})", svg)
        svg = re.sub(r'href="#([^"]+)"', lambda k: f'href="#{k.group(1)}{sfx}"', svg)
        return svg

    agents_html = "".join(
        f'<a class="agent rv" href="/portfolio/ai-systems">{scene(s)}<div><h3>{t}</h3><p>{d}</p></div></a>'
        for s, t, d in AGENTS
    )
    v = str(int(time.time()))

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Victoria Olamide | AI Product Marketing, Go-to-Market &amp; AI Agents</title>
<meta name="description" content="Victoria Olamide is an AI product marketer, go-to-market strategist and founder of Creataws. 5,000+ sign-ups in 48 hours, 45% adoption growth, and Opptiq, an AI product with 260+ organic users and paying customers." />
<link rel="canonical" href="https://victoriaolamide.com/" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Victoria Olamide | AI Product Marketing, GTM &amp; AI Agents" />
<meta property="og:description" content="Building products, go-to-market systems and AI agents that drive revenue." />
<meta property="og:url" content="https://victoriaolamide.com/" />
<meta property="og:image" content="https://victoriaolamide.com/site/img/og-main.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="theme-color" content="#120d06" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Manrope:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&family=Fraunces:ital,opsz,wght@1,9..144,500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/site/site.css?v={v}" />
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav" id="top">
  <div class="wrap">
    <a class="brand" href="/">{monogram(38, ring="#fbf7ef", v="#fbf7ef", bg="#120d06", uid="mainnav")}Victoria Olamide</a>
    <button class="menu" aria-expanded="false" aria-controls="links">Menu</button>
    <ul class="links" id="links">
      <li><a href="#results">Results</a></li>
      <li><a href="#agents">AI Agents</a></li>
      <li><a href="#events">Events</a></li>
      <li><a href="#speaking">Speaking</a></li>
      <li><a href="#creators">Creators</a></li>
      <li><a href="/portfolio">Portfolio</a></li>
      <li class="cta"><a class="btn btn-gold btn-s" href="{CAL}" target="_blank" rel="noopener">Book a strategy call</a></li>
    </ul>
  </div>
</header>

<main id="main">
<section class="hero">
  <div class="hero-img"><img src="/site/img/hero.jpg" alt="Victoria Olamide in a chocolate suit, leaning on a desk and smiling" width="884" height="1080" fetchpriority="high" /></div>
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">AI product marketing · Go-to-market · AI agents</span>
      <h1>Victoria<span class="l2">Olamide<span class="dot">.</span></span></h1>
      <div class="roles"><span>Founder, Creataws</span><span>Builder of Opptiq</span><span>Lawyer turned marketer</span></div>
      <p class="hero-lead">I take products to market, build the AI agents that keep them growing, and turn attention into paying customers.</p>
      <div class="hero-cta">
        <a class="btn btn-gold" href="{CAL}" target="_blank" rel="noopener">Book a strategy call &rarr;</a>
        <a class="btn btn-line" href="/portfolio">View my portfolio &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="practice">
  <div class="wrap">
    <div class="practice">
      <div class="rv">
        <span class="eyebrow">My practice</span>
        <h2 class="big-h" style="margin-top:1rem">Building products, go-to-market and <span class="s">AI.</span></h2>
      </div>
      <div class="copy rv">
        <p>Victoria Olamide is an AI product marketer, go-to-market strategist, product builder and founder of Creataws.</p>
        <p>She takes products from early ideas to paying customers: customer insight, positioning, launch, acquisition and conversion, for teams across the US, UK, Europe, Africa and Asia.</p>
        <p>She builds too. Opptiq and Audint are AI products she specified, built and launched herself, and she designs AI sales, support, voice and operations agents for businesses that want to grow without growing headcount.</p>
      </div>
    </div>
    <div class="stats rv">
      <div class="stat"><b>5,000+</b><span>Sign-ups in 48 hours</span></div>
      <div class="stat"><b>~46%</b><span>Paid conversion</span></div>
      <div class="stat"><b>45%</b><span>Adoption growth in one quarter</span></div>
      <div class="stat"><b>260+</b><span>Organic users on my AI product</span></div>
      <div class="stat"><b>~600</b><span>Users in two weeks</span></div>
      <div class="stat"><b>2,000+</b><span>Event attendees in 72 hours</span></div>
      <div class="stat"><b>15+</b><span>Launches &amp; growth experiments</span></div>
      <div class="stat"><b>2</b><span>AI products built &amp; live</span></div>
    </div>
  </div>
</section>

<section class="sec alt" id="results">
  <div class="wrap">
    <div class="head rv">
      <span class="eyebrow">My selected results</span>
      <h2 class="big-h">My work. <span class="s">What it delivered.</span></h2>
    </div>
    <div class="results">{res_html}
    </div>
    <div class="hero-cta rv" style="margin-top:2.5rem"><a class="btn btn-line" href="/portfolio/work">See every case study in my portfolio &rarr;</a></div>
  </div>
</section>

<section class="sec" id="agents">
  <div class="wrap">
    <div class="head rv">
      <span class="eyebrow">AI agents I build</span>
      <h2 class="big-h">Agents that sell, support and <span class="s">operate.</span></h2>
      <p>Built around how your business actually works, by someone who also knows how to get customers to use them.</p>
    </div>
    <div class="agents">{agents_html}</div>
    <div class="hero-cta rv" style="margin-top:2.5rem">
      <a class="btn btn-gold" href="{CAL}" target="_blank" rel="noopener">Book a strategy call &rarr;</a>
      <a class="btn btn-line" href="/portfolio/ai-systems">How I build them &rarr;</a>
    </div>
  </div>
</section>

<section class="sec lightsec" id="events">
  <div class="wrap">
    <div class="head rv">
      <span class="eyebrow">Events &amp; partnerships</span>
      <h2 class="big-h">Building rooms that <span class="s">convert.</span></h2>
    </div>
    <div class="events">
      <div class="ev-list">
        <div class="ev rv"><i>01</i><div><span class="k">Host &amp; programme lead · Oct 2026</span><h3>Position and Build with Vickie 2.0</h3><p>A five-day live programme on positioning and building with AI for 24 participants, with three guest speakers. I designed the curriculum, led every session and demoed Opptiq live on day one.</p></div></div>
        <div class="ev rv"><i>02</i><div><span class="k">Partner · iHub Nairobi · 5 Nov 2026</span><h3>AI GTM Africa Nairobi</h3><p>Opptiq partnered with AI GTM Africa's Nairobi edition at iHub, alongside companies like Karrd, bringing AI career intelligence to founders and operators in East Africa.</p></div></div>
        <div class="ev rv"><i>03</i><div><span class="k">Founder · Ongoing</span><h3>The Opptiq community</h3><p>A growing community of professionals learning to add AI to the work they already do, with class recordings, a leaderboard and a 30-day action plan.</p></div></div>
      </div>
      <div class="ev-media rv">
        <figure><img src="/site/img/aigtm-backdrop.jpg" alt="AI GTM Africa Nairobi partner backdrop featuring the Opptiq logo" loading="lazy" width="1080" height="737" /><figcaption>AI GTM Africa Nairobi · Opptiq among the partners</figcaption></figure>
        <div class="row">
          <figure><img src="/site/img/aigtm-partner.jpg" alt="Meet our partner: Opptiq, AI GTM Africa Nairobi" loading="lazy" width="867" height="1080" /></figure>
          <figure><img src="/portfolio/img/carousel-opptiq.jpg" alt="Messages from Opptiq users" loading="lazy" width="1080" height="1350" /></figure>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="speaking">
  <div class="wrap">
    <div class="head rv">
      <span class="eyebrow">Speaking &amp; sessions</span>
      <h2 class="big-h">Ideas I teach <span class="s">live.</span></h2>
    </div>
    <div class="talks rv">
      <div class="talk"><i>01 / PBV 2.0</i><h3>Position before you build</h3><p>Why the products that win are the ones people understand in seconds, and how to find that one sentence before writing a line of code.</p></div>
      <div class="talk"><i>02 / LIVE DEMO</i><h3>From idea to AI product</h3><p>A live walkthrough of Opptiq: how a marketer specified, built and launched an AI product with AI tools, and what it took to get the first paying users.</p></div>
      <div class="talk"><i>03 / CREATORS</i><h3>Earn beyond brand deals</h3><p>How creators turn what they know into products, offers and income that don't depend on the next sponsorship.</p></div>
    </div>
    <div class="hero-cta rv" style="margin-top:2rem"><a class="btn btn-line" href="{MAIL.replace('Hello%20Victoria', 'Speaking%20invitation')}">Invite me to speak &rarr;</a></div>
  </div>
</section>

<section class="sec alt" id="creators">
  <div class="wrap creators">
    <div class="photo rv"><img src="/site/img/creator.jpg" alt="Victoria Olamide in a cream dress, celebrating" loading="lazy" width="810" height="1080" /></div>
    <div class="rv">
      <span class="eyebrow">Content &amp; creators</span>
      <h2 class="big-h" style="margin:1rem 0 1.25rem">Product marketing for <span class="s">creators.</span></h2>
      <p style="color:var(--t2);font-size:1.05rem">I teach creators and professionals how to position what they know, package it and get paid for it. Every week on Instagram, LinkedIn, X and TikTok: case files from real launches, objections answered, and the systems behind them.</p>
      <div class="strip">
        <img src="/portfolio/img/carousel-launch.jpg" alt="Carousel: launches I worked on and what moved the number" loading="lazy" />
        <img src="/portfolio/img/carousel-contour.jpg" alt="Carousel from the positioning series" loading="lazy" />
        <img src="/portfolio/img/carousel-opptiq.jpg" alt="Carousel: Opptiq social proof" loading="lazy" />
      </div>
      <div class="socials">
        <a href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://www.instagram.com/victoriaolamide__" target="_blank" rel="noopener">Instagram</a>
        <a href="https://x.com/vickieolamide" target="_blank" rel="noopener">X</a>
        <a href="https://www.tiktok.com/@victoriaolamide_" target="_blank" rel="noopener">TikTok</a>
      </div>
    </div>
  </div>
</section>

<section class="sec lightsec">
  <div class="wrap">
    <div class="head rv">
      <span class="eyebrow">How I work</span>
      <h2 class="big-h">Product. GTM. <span class="s">AI.</span></h2>
    </div>
    <div class="pillars">
      <div class="pillar rv"><i>01</i><h3>Product &amp; positioning</h3><p>I research customers, find the problem that matters and shape the one message that makes a product easy to choose, then carry it through launch and adoption.</p></div>
      <div class="pillar rv"><i>02</i><h3>Go-to-market</h3><p>Launch plans, acquisition, partnerships and conversion, measured until the number moves, and written into a playbook the team keeps.</p></div>
      <div class="pillar rv"><i>03</i><h3>AI implementation</h3><p>AI agents, products and automations built around real business needs, to cut manual work, speed up follow-up and help teams decide faster.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap why">
    <div class="rv">
      <span class="eyebrow">Why I do this</span>
      <h2 class="big-h" style="margin-top:1rem">Evidence first. <span class="s">Then the argument.</span></h2>
    </div>
    <div class="rv">
      <p>I trained as a lawyer at Obafemi Awolowo University and the Nigerian Law School. Law taught me to build a case from evidence, anticipate objections and make a call I can defend. That is most of product marketing.</p>
      <p>I founded Creataws because I kept seeing the same gap: businesses have powerful AI within reach, but struggle to connect it to the customers and problems that matter. So I build both sides, the go-to-market and the AI, and I measure everything by one thing: whether people pay.</p>
      <div class="hero-cta"><a class="btn btn-line" href="/portfolio/about">More about me &rarr;</a></div>
    </div>
  </div>
</section>

<section class="final">
  <div class="wrap">
    <span class="eyebrow">Work with Victoria</span>
    <h2>Let's build what<br />comes next.</h2>
    <p>Hiring for AI product marketing, need AI agents that drive revenue, or planning an event? Start with a call.</p>
    <div class="hero-cta" style="justify-content:center">
      <a class="btn btn-cream" href="{CAL}" target="_blank" rel="noopener">Book a strategy call &rarr;</a>
      <a class="btn btn-line" href="{MAIL}">Send an email &rarr;</a>
      <a class="btn btn-line" href="/portfolio">View my portfolio &rarr;</a>
      <a class="btn btn-line" href="/portfolio/Victoria-Olamide-CV.pdf" download>Download CV &darr;</a>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <span>&copy; 2026 Victoria Olamide &middot; Founder, Creataws Ltd</span>
    <nav aria-label="Footer">
      <a href="/portfolio">Portfolio</a>
      <a href="https://opptiq.victoriaolamide.com" target="_blank" rel="noopener">Opptiq</a>
      <a href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn</a>
      <a href="https://www.instagram.com/victoriaolamide__" target="_blank" rel="noopener">Instagram</a>
      <a href="https://victoriaolamide.nestuge.com" target="_blank" rel="noopener">Nestuge</a>
      <a href="{MAIL}">Send an email</a>
    </nav>
  </div>
</footer>
<script src="/site/site.js?v={v}" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    OUT.write_text(page(), encoding="utf-8")
    print("built", OUT)
