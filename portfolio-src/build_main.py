"""Build the main website (victoriaolamide.com) into ../index.html.

Static HTML, no framework. Reuses scenes.py (animated agent scenes),
logo.py (monogram) and content.py (LinkedIn testimonials).
Run:  python portfolio-src/build_main.py   (then npm run build)
"""
import re
import time
from pathlib import Path

from scenes import render
from logo import monogram
from content import testimonials

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "index.html"
CAL = "https://calendly.com/hello-victoriaolamide/30min"
MAIL = "mailto:hello@victoriaolamide.com?subject=Hello%20Victoria"

CASES = [
    ("01", "United States", "I'll Tip", "A new feature had to land fast. I led the go-to-market: positioning, launch messaging and rollout. The SOP I wrote became the team's standard.", "5,000+", "sign-ups in 48 hours, ~46% paid"),
    ("02", "Germany", "Viewon.AI", "A year leading product marketing and market entry for an AI platform, with the partnerships that gave it credibility.", "45%", "adoption growth in one quarter"),
    ("03", "Nigeria", "Endow", "A creator platform entering a new market with fewer than 50 users. Positioning plus community-led acquisition.", "~600", "users in two weeks"),
    ("04", "Edtech", "Utiva", "A time-boxed event with a 72-hour window to fill the room. It became a repeat engagement.", "2,000+", "attendees in 72 hours"),
    ("05", "My product", "Opptiq", "An AI product I specified, built, priced and launched. Two LinkedIn posts, no ads.", "260+", "organic users, paying customers"),
    ("06", "Founders &amp; startups", "Client portfolio", "Product marketing, monetisation and AI-enabled growth systems for founders, across a distributed team.", "15+", "launches &amp; experiments"),
]

AGENTS = [
    ("sales", "AI Sales Agents", "Qualify leads, follow up and update your CRM."),
    ("support", "AI Support Agents", "Answer customers from their own account data, with human handoff."),
    ("voice", "AI Voice Agents", "Answer every call, qualify callers and book appointments."),
    ("ops", "AI Operations Agents", "Email, scheduling, docs and data, handled across your tools."),
]

FAQ = [
    ("What is Opptiq?", "Opptiq is the AI opportunity intelligence platform I built. It shows people exactly where their existing expertise meets AI, backed by live job-market evidence, and gives them a personalised action plan. Your first two analyses are free. <a href=\"https://opptiq.victoriaolamide.com\" target=\"_blank\" rel=\"noopener\">Try Opptiq</a>."),
    ("Can you build AI agents for my business?", "Yes. I build AI sales, customer support, voice and operations agents around how your business actually works, and connect them to the tools you already use. We start with a strategy call to find the one bottleneck worth automating first. <a href=\"/portfolio/ai-systems\">See the agents I build</a>."),
    ("What does an AI product marketer actually do?", "I make AI products easy to understand and easy to choose: customer insight, positioning, launch, adoption and conversion. It is the work behind 5,000+ sign-ups in 48 hours at I'll Tip and 45% adoption growth at Viewon.AI."),
    ("Are you open to full-time roles?", "Yes. I'm open to product marketing roles with US and UK startups, working remotely from Lagos across US and European time zones. <a href=\"/portfolio/resume\">Read my résumé</a>."),
    ("Do you work with creators?", "Yes. Product marketing for creators is my content niche: positioning what you know, packaging it and getting paid for it beyond brand deals."),
    ("Can you speak at my event?", "I'd love to. I speak on positioning, building with AI and earning beyond brand deals. <a href=\"mailto:hello@victoriaolamide.com?subject=Speaking%20invitation\">Send an invitation</a>."),
    ("How do we start?", "Book a strategy call. Tell me the problem you're trying to solve, and you'll leave with a clear recommendation, whether or not we work together."),
]


def scene_factory():
    counter = {"n": 0}

    def scene(name):
        counter["n"] += 1
        svg = render(name)
        sfx = f"-m{counter['n']}"
        svg = re.sub(r'id="([^"]+)"', lambda k: f'id="{k.group(1)}{sfx}"', svg)
        svg = re.sub(r"url\(#([^)]+)\)", lambda k: f"url(#{k.group(1)}{sfx})", svg)
        svg = re.sub(r'href="#([^"]+)"', lambda k: f'href="#{k.group(1)}{sfx}"', svg)
        return svg
    return scene


def page() -> str:
    scene = scene_factory()
    cases = "".join(
        f'<article class="case rv"><div class="top"><span>Case file {n}</span><b>{where}</b></div><h3>{name}</h3><p>{body}</p>'
        f'<div class="verdict"><small>Verdict</small><b>{big}</b><span>{small}</span></div></article>'
        for n, where, name, body, big, small in CASES
    )
    agents = "".join(
        f'<a class="agent rv" href="/portfolio/ai-systems">{scene(s)}<div><h3>{t}</h3><p>{d}</p></div></a>' for s, t, d in AGENTS
    )
    faq = "".join(
        f'<details class="rv"><summary><i>Objection {i:02d}</i>{q}</summary><div class="ans">{a}</div></details>'
        for i, (q, a) in enumerate(FAQ, 1)
    )
    nav_logo = monogram(36, ring="#fbf7ef", v="#fbf7ef", bg="#1a1409", uid="mainnav")
    foot_logo = monogram(30, ring="#fbf7ef", v="#fbf7ef", bg="#1a1409", uid="mainfoot")
    v = str(int(time.time()))

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Victoria Olamide | AI Product Marketing, Go-to-Market &amp; AI Agents</title>
<meta name="description" content="Victoria Olamide takes products to market, builds the AI agents that keep them growing, and turns attention into paying customers. Founder of Creataws, builder of Opptiq." />
<link rel="canonical" href="https://victoriaolamide.com/" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Victoria Olamide | AI Product Marketing, GTM &amp; AI Agents" />
<meta property="og:description" content="I take products to market, build the AI agents that keep them growing, and turn attention into paying customers." />
<meta property="og:url" content="https://victoriaolamide.com/" />
<meta property="og:image" content="https://victoriaolamide.com/site/img/og-main.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="theme-color" content="#1a1409" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Manrope:wght@400;500;600;700&family=DM+Mono:wght@400;500&family=Fraunces:ital,opsz,wght@1,9..144,400;1,9..144,500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/site/site.css?v={v}" />
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="/">{nav_logo}Victoria Olamide</a>
    <button class="menu" aria-expanded="false" aria-controls="links">Menu</button>
    <ul class="links" id="links">
      <li><a href="#cases">Results</a></li>
      <li><a href="#agents">AI Agents</a></li>
      <li><a href="#events">Events</a></li>
      <li><a href="#creators">Creators</a></li>
      <li><a href="#faq">FAQ</a></li>
      <li><a href="/portfolio">Portfolio</a></li>
      <li class="cta"><a class="btn btn-gold btn-s" href="{CAL}" target="_blank" rel="noopener">Book a strategy call</a></li>
    </ul>
  </div>
</header>

<main id="main">
<section class="hero">
  <img class="hero-photo" src="/site/img/hero-cut.webp" alt="Victoria Olamide in a chocolate suit, smiling" width="884" height="850" fetchpriority="high" />
  <div class="wrap">
    <div class="hero-copy rv">
      <span class="eyebrow">AI product marketing · Go-to-market · AI agents</span>
      <h1>Victoria <em class="s">Olamide.</em></h1>
      <div class="roles"><span>Founder, Creataws</span><span>Built Opptiq</span></div>
      <p class="lead">I take products to market, build the AI agents that keep them growing, and turn attention into paying customers.</p>
      <div class="row">
        <a class="btn btn-gold" href="{CAL}" target="_blank" rel="noopener">Book a strategy call &rarr;</a>
        <a class="btn btn-line" href="/portfolio">View my portfolio</a>
      </div>
    </div>
    <div></div>
    <div class="proof rv">
      <div class="chip"><b>5,000+</b><span>sign-ups in 48 hours</span></div>
      <div class="chip"><b>45%</b><span>adoption growth in a quarter</span></div>
      <div class="chip"><b>260+</b><span>organic users on Opptiq, with paying customers</span></div>
    </div>
  </div>
</section>

<section class="sec cream" id="practice">
  <div class="wrap">
    <div class="practice">
      <div class="rv">
        <span class="eyebrow">My practice</span>
        <h2>Products, go-to-market and <em class="s">AI</em>, built to convert.</h2>
      </div>
      <div class="copy rv">
        <p class="big">I make good products easy to choose, then build the systems that keep people choosing them.</p>
        <p>I lead positioning, launches and growth for technology products, working with teams across the US, UK, Europe, Africa and Asia.</p>
        <p>I build, too. Opptiq and Audint are AI products I specified, built and launched myself, and I design AI agents for businesses that want to grow without growing headcount.</p>
      </div>
    </div>
    <div class="stats rv">
      <div class="stat"><b>5,000+</b><span>sign-ups in 48 hours</span></div>
      <div class="stat"><b>~46%</b><span>of them became paying customers</span></div>
      <div class="stat"><b>45%</b><span>adoption growth in one quarter</span></div>
      <div class="stat"><b>25</b><span>AI agents, automations and systems built</span></div>
    </div>
  </div>
</section>

<section class="sec dark" id="cases">
  <div class="wrap">
    <div class="split rv">
      <div><span class="eyebrow">The case files</span><h2>The work, and the <em class="s">verdict.</em></h2></div>
      <p>Every launch is a case: the brief, the argument I made to the market, and the number that came back. Full evidence lives in my portfolio.</p>
    </div>
    <div class="cases">{cases}</div>
    <div class="row rv" style="margin-top:2rem"><a class="btn btn-line" href="/portfolio/work">Open every case file &rarr;</a></div>
  </div>
</section>

<section class="sec cream" id="testimony">
  <div class="wrap">
    <div class="head center rv">
      <span class="eyebrow">Testimony</span>
      <h2>From colleagues and <em class="s">clients.</em></h2>
    </div>
    <div class="rv">{testimonials()}</div>
  </div>
</section>

<section class="sec dark" id="agents">
  <div class="wrap">
    <div class="split rv">
      <div><span class="eyebrow">AI agents I build</span><h2>Agents that sell, support and <em class="s">operate.</em></h2></div>
      <p>Built around how your business actually works, by someone who also knows how to get customers to use them.</p>
    </div>
    <div class="agents">{agents}</div>
    <div class="row rv" style="margin-top:2rem">
      <a class="btn btn-gold" href="{CAL}" target="_blank" rel="noopener">Book a strategy call &rarr;</a>
      <a class="btn btn-line" href="/portfolio/ai-systems#library">Browse my AI Library</a>
    </div>
  </div>
</section>

<section class="sec white" id="events">
  <div class="wrap">
    <div class="head rv">
      <span class="eyebrow">Events &amp; partnerships</span>
      <h2>Rooms I've built, and rooms I've <em class="s">joined.</em></h2>
    </div>
    <div class="events">
      <div>
        <div class="ev rv"><i>01</i><div><span class="k">Host &amp; programme lead · Oct 2026</span><h3>Position and Build with Vickie 2.0</h3><p>A five-day live programme on positioning and building with AI for 24 participants, with three guest speakers. I designed the curriculum, led every session and demoed Opptiq live on day one.</p></div></div>
        <div class="ev rv"><i>02</i><div><span class="k">Partner · iHub Nairobi · 5 Nov 2026</span><h3>AI GTM Africa Nairobi</h3><p>Opptiq partnered with AI GTM Africa's Nairobi edition at iHub, bringing AI career intelligence to founders and operators in East Africa.</p></div></div>
        <div class="ev rv"><i>03</i><div><span class="k">Founder · Ongoing</span><h3>The Opptiq community</h3><p>Professionals learning to add AI to the work they already do, with class recordings, a leaderboard and a 30-day action plan.</p></div></div>
      </div>
      <div class="ev-media rv">
        <figure><img src="/site/img/aigtm-backdrop.jpg" alt="AI GTM Africa Nairobi partner backdrop featuring the Opptiq logo" loading="lazy" width="1080" height="737" /><figcaption>AI GTM Africa Nairobi · Opptiq among the partners</figcaption></figure>
        <div class="pair">
          <figure><img src="/site/img/aigtm-partner.jpg" alt="Meet our partner: Opptiq" loading="lazy" width="867" height="1080" /></figure>
          <figure><img src="/portfolio/img/car-postcard.jpg" alt="Greetings from Nairobi: Opptiq has gone global" loading="lazy" width="1080" height="1350" /></figure>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec dark" id="speaking">
  <div class="wrap">
    <div class="split rv">
      <div><span class="eyebrow">Speaking &amp; sessions</span><h2>Ideas I teach <em class="s">live.</em></h2></div>
      <p>Practical sessions for founders, professionals and creators. Clear frameworks, real launches, no fluff.</p>
    </div>
    <div class="talks">
      <div class="talk rv"><i>01 · PBV 2.0</i><h3>Position before you build</h3><p>Why the products that win are the ones people understand in seconds, and how to find that one sentence first.</p></div>
      <div class="talk rv"><i>02 · Live demo</i><h3>From idea to AI product</h3><p>How a marketer specified, built and launched an AI product with AI tools, and what it took to get paying users.</p></div>
      <div class="talk rv"><i>03 · Creators</i><h3>Earn beyond brand deals</h3><p>How creators turn what they know into products, offers and income that don't depend on the next sponsorship.</p></div>
    </div>
    <div class="row rv" style="margin-top:2rem"><a class="btn btn-line" href="mailto:hello@victoriaolamide.com?subject=Speaking%20invitation">Invite me to speak &rarr;</a></div>
  </div>
</section>

<section class="sec cream" id="creators">
  <div class="wrap creators">
    <div class="rv">
      <span class="eyebrow">Content &amp; creators</span>
      <h2>Product marketing for <em class="s">creators.</em></h2>
      <p>I teach creators and professionals how to position what they know, package it and get paid for it. New series every week on Instagram, LinkedIn, X and TikTok.</p>
      <div class="socials">
        <a href="https://www.instagram.com/victoriaolamide__" target="_blank" rel="noopener">Instagram</a>
        <a href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://x.com/vickieolamide" target="_blank" rel="noopener">X</a>
        <a href="https://www.tiktok.com/@victoriaolamide_" target="_blank" rel="noopener">TikTok</a>
      </div>
    </div>
    <div class="fan rv">
      <img src="/portfolio/img/car-sell.jpg" alt="Carousel: Sell what you're already doing for free" loading="lazy" />
      <img src="/portfolio/img/car-teach.jpg" alt="Carousel: Teach it. People will pay to skip your mistakes" loading="lazy" />
      <img src="/site/img/car-wednesday.jpg" alt="Post: Monday me, 5am gym and deep work. Wednesday me, just let me reach Friday" loading="lazy" />
    </div>
  </div>
</section>

<section class="sec dark">
  <div class="wrap">
    <div class="head rv">
      <span class="eyebrow">How I work</span>
      <h2>Evidence first. <em class="s">Then the argument.</em></h2>
    </div>
    <div class="pillars">
      <div class="pillar rv"><i>01</i><h3>Product &amp; positioning</h3><p>I research customers, find the problem that matters and shape the one message that makes a product easy to choose.</p></div>
      <div class="pillar rv"><i>02</i><h3>Go-to-market</h3><p>Launch plans, acquisition, partnerships and conversion, measured until the number moves and written into a playbook.</p></div>
      <div class="pillar rv"><i>03</i><h3>AI implementation</h3><p>AI agents, products and automations built around real business needs, so teams move faster with less manual work.</p></div>
    </div>
  </div>
</section>

<section class="sec white" id="faq">
  <div class="wrap">
    <div class="head center rv">
      <span class="eyebrow">FAQ</span>
      <h2>Objections, <em class="s">answered.</em></h2>
      <p>The questions people ask before they book a call.</p>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="sec cream" style="padding-top:clamp(3rem,6vw,4.5rem)">
  <div class="wrap">
    <div class="closing rv">
      <div>
        <h2>Let's build what comes <em class="s">next.</em></h2>
        <p>Hiring for product marketing, need AI agents that drive revenue, or planning an event? Start with a call.</p>
      </div>
      <div class="row">
        <a class="btn btn-cream" href="{CAL}" target="_blank" rel="noopener">Book a strategy call &rarr;</a>
        <a class="btn btn-line" href="{MAIL}">Send an email</a>
        <a class="btn btn-line" href="/portfolio/Victoria-Olamide-CV.pdf" download>Download CV &darr;</a>
      </div>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <a class="brand" href="/">{foot_logo}<span>&copy; 2026 Victoria Olamide &middot; Founder, Creataws Ltd</span></a>
    <nav aria-label="Footer">
      <a href="/portfolio">Portfolio</a>
      <a href="https://opptiq.victoriaolamide.com" target="_blank" rel="noopener">Opptiq</a>
      <a href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn</a>
      <a href="https://www.instagram.com/victoriaolamide__" target="_blank" rel="noopener">Instagram</a>
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
