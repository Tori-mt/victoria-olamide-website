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
from content import testimonials, LIBRARY
from luna import widget_html as luna_widget, write_kb as luna_write_kb
SIGNUP = "https://opptiq.victoriaolamide.com/signup"
DASHIE = "https://opptiq.victoriaolamide.com/?support=open"
CREATAWS = "https://creataws.victoriaolamide.com"

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "index.html"
CAL = "https://calendly.com/hello-victoriaolamide/30min"
MAIL = "mailto:hello@victoriaolamide.com?subject=Hello%20Victoria"

CASES = [
    ("01", "United States", "I'll Tip", "A new feature had to land fast. I led the go-to-market: positioning, launch messaging and rollout. The SOP I wrote became the team's standard.", "5,000+", "sign-ups in 48 hours, ~46% paid"),
    ("02", "Germany", "Viewon.AI", "A year leading product marketing and market entry for an AI platform, with the partnerships that gave it credibility.", "45%", "adoption growth in one quarter"),
    ("03", "Nigeria", "Endow", "A creator platform entering a new market with fewer than 50 users. Positioning plus community-led acquisition.", "~600", "users in two weeks"),
    ("04", "Edtech", "Utiva", "A time-boxed event with a 72-hour window to fill the room. It became a repeat engagement.", "2,000+", "attendees in 72 hours"),
    ("05", "My product", "Opptiq", "An AI product I specified, built, priced and launched. Two LinkedIn posts, no ads.", "260+", "organic users in 2+ weeks, with paying users"),
    ("06", "Founders &amp; startups", "Client portfolio", "Product marketing, monetisation and AI-enabled growth systems for founders, across a distributed team.", "15+", "launches &amp; experiments"),
]

AGENTS = [
    ("sales", "AI Sales Agents", "Qualify leads, follow up and update your CRM.", "sales"),
    ("support", "AI Support Agents", "Answer customers from their own account data, with human handoff.", "support"),
    ("voice", "AI Voice Agents", "Answer every call, qualify callers and book appointments.", "voice"),
    ("ops", "AI Operations Agents", "Email, scheduling, docs and data, handled across your tools.", "ops"),
]
LIB = {name: (what, stack) for _c, name, what, stack, _l in LIBRARY}

FAQ = [
    ('What is Opptiq?', 'Opptiq is your AI career guide. You tell us about your work, and in minutes you get a personal report showing where AI fits into your skills, the problems you could solve, new ways to earn in dollars globally, and real remote jobs paying thousands of dollars for those skills right now.<br><br>Then Opptiq finds those jobs for you, tailors your CV, cover letter and portfolio to each one, and tracks every application, with a 60-day plan of small daily tasks so you lock in and land your dream role. Get your free analysis today. For more questions, ask Luna below.<span class="ans-cta"><a class="btn btn-gold btn-s" href="https://opptiq.victoriaolamide.com" target="_blank" rel="noopener">Try Opptiq</a><a class="btn btn-line btn-s" href="https://opptiq.victoriaolamide.com/signup" target="_blank" rel="noopener">Subscribe to Opptiq freebies</a></span>'),
    ('I have a question. Who can I ask?', "Ask Luna, my AI assistant. Tap <b>Ask Luna</b> at the bottom of this page for an instant answer about my work, AI agents or Opptiq. If it's personal, Luna will pass you straight to me."),
    ('Can you build AI agents for my business?', 'Yes. I build AI sales, customer support, voice and operations agents around how your business actually works, and connect them to the tools you already use. We start with a strategy call to find the one thing worth automating first.'),
    ('What does an AI product marketer actually do?', "I make AI products easy to understand and easy to choose: customer insight, positioning, launch, adoption and conversion. It's the work behind 5,000+ sign-ups in 48 hours at I'll Tip and 45% adoption growth at Viewon.AI. <a href=\"/portfolio/work\">See the results in my portfolio</a>."),
    ('Are you open to full-time roles?', 'Yes. I\'m open to AI product marketing roles with US and UK startups, working remotely from Lagos across US and European time zones. <a href="/portfolio/resume">Read my résumé</a>.'),
    ('Do you work with creators?', "Yes. Book a call and I'll show you how to turn your content into paying customers. <a href=\"https://calendly.com/hello-victoriaolamide/30min\" target=\"_blank\" rel=\"noopener\">Book a strategy call</a>."),
    ('Can you speak at my event?', 'I\'d love to. I speak on positioning, building with AI and earning beyond brand deals. <a href="mailto:hello@victoriaolamide.com?subject=Speaking%20invitation">Send an invitation</a>.'),
    ('How do we start?', "Have a look at my portfolio, then book a strategy call. Tell me what you're trying to solve and you'll leave with a clear next step, whether or not we work together."),
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
        f'<article class="case rv"><div class="top"><span>Project {n}</span><b>{where}</b></div><h3>{name}</h3><p>{body}</p>'
        f'<div class="result"><small>Result</small><b>{big}</b><span>{small}</span></div></article>'
        for n, where, name, body, big, small in CASES
    )
    agents = "".join(
        f'<a class="agent rv" href="/portfolio/ai-systems?show={tag}#library">{scene(s)}<div><h3>{t}</h3><p>{d}</p>'
        f'<span class="see">See what I\'ve built &rarr;</span></div></a>'
        for s, t, d, tag in AGENTS
    )
    faq = "".join(
        f'<details class="rv"><summary>{q}</summary><div class="ans">{a}</div></details>'
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
    <a class="brand" href="/" data-home>{nav_logo}Victoria Olamide</a>
    <button class="menu" aria-expanded="false" aria-controls="links">Menu</button>
    <ul class="links" id="links">
      <li><a href="#cases">Results</a></li>
      <li><a href="#agents">AI Agents</a></li>
      <li><a href="#events">Events</a></li>
      <li><a href="#opptiq">Opptiq</a></li>
      <li><a href="#creataws">Creataws</a></li>
      <li><a href="#creators">Social Media Conversion System</a></li>
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
      <h1>Victoria<br />Olamide.</h1>
      <div class="roles"><span>Founder, Creataws</span><span>Built Opptiq</span></div>
      <p class="lead">I take products to market, build the AI agents that keep them growing, and turn attention into paying customers.</p>
      <div class="row">
        <a class="btn btn-gold shine breathe" href="/portfolio">View my portfolio to work with me &rarr;</a>
        <a class="btn btn-line" href="{CAL}" target="_blank" rel="noopener">Book a strategy call</a>
      </div>
      <span class="open"><i></i>Open to AI product marketing roles with US and UK startups</span>
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
      <div class="stat"><b>~600</b><span>users in two weeks, from under 50</span></div>
      <div class="stat"><b>2,000+</b><span>event attendees in 72 hours</span></div>
      <div class="stat"><b>260+</b><span>organic users on Opptiq, with paying customers</span></div>
      <div class="stat"><b>5+</b><span>strategic partnerships secured</span></div>
    </div>
  </div>
</section>

<section class="sec dark" id="cases">
  <div class="wrap">
    <div class="split rv">
      <div><span class="eyebrow">My work</span><h2>My work, and what it <em class="s">achieved.</em></h2></div>
      <p>Six projects: the challenge, what I did, and the result. You'll find the full details in my portfolio.</p>
    </div>
    <div class="cases">{cases}</div>
    <div class="row rv" style="margin-top:2rem"><a class="btn btn-gold pulse" href="/portfolio/work">See all my work &rarr;</a></div>
  </div>
</section>

<section class="sec white" id="testimonials">
  <div class="wrap">
    <div class="head center rv">
      <span class="eyebrow">Testimonials</span>
      <h2>Testimonials from colleagues and <em class="s">clients.</em></h2>
    </div>
    <div class="rv">{testimonials()}</div>
  </div>
</section>

<section class="sec dark" id="agents">
  <div class="wrap">
    <div class="split rv">
      <div><span class="eyebrow">AI agents I build</span><h2>Agents that sell, support, operate and <em class="s">convert.</em></h2></div>
      <p>Built around how your business actually works. Tap any card to see the ones I've already built.</p>
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
        <div class="row rv" style="margin-top:1.6rem"><a class="btn btn-gold pulse ring" href="mailto:hello@victoriaolamide.com?subject=Partnership">Partner with me &rarr;</a></div>
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

<section class="sec opptiq-band" id="opptiq">
  <div class="wrap opq">
    <div class="opq-copy rv">
      <span class="eyebrow">My AI product</span>
      <h2>Try the Opptiq app <em class="s">today.</em></h2>
      <p class="opq-lead">Opptiq is your AI career guide. Tell it about your work and in minutes you get a personal report on where AI fits your skills, and how to earn remotely in dollars globally with them.</p>
      <ul class="opq-list">
        <li><b>Your AI career report in minutes</b><span>Where AI fits your skills and the problems you could solve.</span></li>
        <li><b>Real remote jobs, found for you</b><span>Roles paying thousands of dollars for the skills you already have.</span></li>
        <li><b>Your CV, cover letter and a 60-day plan</b><span>Tailored to each job, with small daily tasks so you land the role.</span></li>
      </ul>
      <p class="opq-proof"><b>260+</b> organic users in 2+ weeks, with paying users.</p>
      <div class="row">
        <a class="btn btn-gold pulse" href="https://opptiq.victoriaolamide.com/signup" target="_blank" rel="noopener">Get your free analysis &rarr;</a>
        <a class="btn btn-line" href="https://opptiq.victoriaolamide.com" target="_blank" rel="noopener" data-install>Install the app</a>
      </div>
    </div>
    <div class="opq-phone rv" aria-hidden="true">
      <div class="phone"><span class="notch"></span><img src="/site/img/opptiq-phone.jpg" alt="" width="640" height="1280" loading="lazy" /></div>
    </div>
  </div>
</section>

<section class="sec dark" id="creataws">
  <div class="wrap cw">
    <div class="cw-copy rv">
      <span class="eyebrow">My company</span>
      <h2>Creataws: strategy <em class="s">plus the build.</em></h2>
      <p class="cw-lead">Creataws is my full-cycle go-to-market and AI growth firm for products the market can't ignore. We help startups, scale-ups and companies launch, win the right customers and keep growing with AI.</p>
      <ul class="opq-list">
        <li><b>Go-to-market, launches and positioning</b><span>The plan and the story that turn day one into momentum.</span></li>
        <li><b>Content systems that convert</b><span>Months of posts, ready before day one, across five platforms.</span></li>
        <li><b>AI agents and AI products</b><span>Sales, support, voice and operations agents, plus 25 AI systems built.</span></li>
      </ul>
      <div class="row">
        <a class="btn btn-gold pulse" href="https://creataws.victoriaolamide.com" target="_blank" rel="noopener">Visit Creataws &rarr;</a>
        <a class="btn btn-line" href="https://creataws.victoriaolamide.com/ai-systems" target="_blank" rel="noopener">See the AI systems</a>
      </div>
    </div>
    <a class="cw-shot rv" href="https://creataws.victoriaolamide.com" target="_blank" rel="noopener" aria-label="Open the Creataws website">
      <span class="cw-bar"><i></i><i></i><i></i><em>creataws.victoriaolamide.com</em></span>
      <img src="/site/img/creataws-site.jpg" alt="The Creataws website homepage: Strategy plus the build." width="1200" height="750" loading="lazy" />
    </a>
  </div>
</section>

<section class="sec cream" id="creators">
  <div class="wrap creators">
    <div class="rv">
      <span class="eyebrow">Content &amp; creators</span>
      <h2>Product marketing for <em class="s">creators.</em></h2>
      <p>Book a call with me to build a content system that saves you stress and converts followers into paying customers, without you lifting a finger every day.</p>
      <div class="row" style="margin-top:1.3rem"><a class="btn btn-gold pulse" href="{CAL}" target="_blank" rel="noopener">Book a strategy call &rarr;</a></div>
      <div class="socials">
        <a href="https://www.instagram.com/victoriaolamide__" target="_blank" rel="noopener">Instagram</a>
        <a href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://x.com/vickieolamide" target="_blank" rel="noopener">X</a>
        <a href="https://www.tiktok.com/@victoriaolamide_" target="_blank" rel="noopener">TikTok</a>
        <a href="https://www.facebook.com/olamide.victoria.31" target="_blank" rel="noopener">Facebook</a>
      </div>
    </div>
    <div class="fan rv">
      <img src="/portfolio/img/car-sell.jpg" alt="Carousel: Sell what you're already doing for free" loading="lazy" />
      <img src="/portfolio/img/car-teach.jpg" alt="Carousel: Teach it. People will pay to skip your mistakes" loading="lazy" />
      <img src="/site/img/car-wednesday.jpg" alt="Post: Monday me, 5am gym and deep work. Wednesday me, just let me reach Friday" loading="lazy" />
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


<section class="sec white" id="faq">
  <div class="wrap">
    <div class="head center rv">
      <span class="eyebrow">FAQ</span>
      <h2>Frequently asked <em class="s">questions.</em></h2>
      <p>Still curious? Ask Luna at the bottom of the page.</p>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>

</main>

<footer class="foot">
  <div class="wrap">
    <div class="fcols">
      <div class="fbrand">
        <a class="brand" href="/" data-home>{foot_logo}Victoria Olamide</a>
        <p>AI product marketing, go-to-market and AI agents.</p>
        <a class="fmail" href="{MAIL}">hello@victoriaolamide.com</a>
      </div>
      <div><h4>Explore</h4><ul>
        <li><a href="/portfolio">Portfolio</a></li>
        <li><a href="https://opptiq.victoriaolamide.com" target="_blank" rel="noopener">Opptiq</a></li>
        <li><a href="/portfolio/ai-systems">AI Agents</a></li>
        <li><a href="/portfolio/ai-systems#library">AI Library</a></li>
        <li><a href="#faq">FAQ</a></li>
      </ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="/portfolio/about">About me</a></li>
        <li><a href="{CREATAWS}" target="_blank" rel="noopener">Creataws</a></li>
        <li><a href="{MAIL}" data-contact>Contact me</a></li>
        <li><a href="{CAL}" target="_blank" rel="noopener">Book a strategy call</a></li>
      </ul></div>
      <div><h4>Follow</h4><ul>
        <li><a href="https://www.linkedin.com/in/victoria-olamide" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="https://x.com/vickieolamide" target="_blank" rel="noopener">X / Twitter</a></li>
        <li><a href="https://www.instagram.com/victoriaolamide__" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="https://www.tiktok.com/@victoriaolamide_" target="_blank" rel="noopener">TikTok</a></li>
        <li><a href="https://www.facebook.com/olamide.victoria.31" target="_blank" rel="noopener">Facebook</a></li>
      </ul></div>
    </div>
    <div class="fbottom">
      <p>The Victoria Olamide brand and all associated products, including Opptiq, are owned and operated by Creataws Ltd.</p>
      <p class="small"><span>Open to AI product marketing roles with US and UK startups.</span><span>&copy; 2026 Creataws Ltd. All rights reserved.</span></p>
    </div>
  </div>
</footer>
<dialog class="contact install" id="install" aria-labelledby="install-title">
  <div class="cform">
    <button class="cx" type="button" data-close-install aria-label="Close">&times;</button>
    <span class="eyebrow">Install the app</span>
    <h3 id="install-title">Put Opptiq on your home screen</h3>
    <p class="csub">It installs straight from your browser in a few seconds. No app store needed.</p>
    <ol class="steps-ol">
      <li><b>iPhone or iPad:</b> open Opptiq in Safari, tap <b>Share</b>, then <b>Add to Home Screen</b>.</li>
      <li><b>Android:</b> open Opptiq in Chrome and tap <b>Install app</b> (or menu, then <b>Add to Home screen</b>).</li>
      <li><b>Computer:</b> open Opptiq and click <b>Add to Desktop</b> at the top.</li>
    </ol>
    <a class="btn btn-gold" href="https://opptiq.victoriaolamide.com" target="_blank" rel="noopener">Open Opptiq &rarr;</a>
  </div>
</dialog>
<dialog class="contact" id="contact" aria-labelledby="contact-title">
  <form class="cform" method="dialog" novalidate>
    <button class="cx" type="button" data-close aria-label="Close">&times;</button>
    <span class="eyebrow">Contact me</span>
    <h3 id="contact-title">Send me a message</h3>
    <p class="csub">It goes straight to my inbox, and I'll reply to your email.</p>
    <label>Your name<input name="name" required maxlength="120" autocomplete="name" /></label>
    <label>Your email<input name="email" type="email" required maxlength="200" autocomplete="email" /></label>
    <label>Your message<textarea name="message" required rows="5" maxlength="5000"></textarea></label>
    <label class="hp" aria-hidden="true">Company<input name="company" tabindex="-1" autocomplete="off" /></label>
    <button class="btn btn-gold" type="submit">Send message &rarr;</button>
    <p class="cstatus" role="status" aria-live="polite"></p>
  </form>
</dialog>
{luna_widget()}
<script src="/site/site.js?v={v}" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    luna_write_kb(ROOT.parent / "api")
    OUT.write_text(page(), encoding="utf-8")
    print("built", OUT)
