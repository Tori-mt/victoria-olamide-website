"""Luna, Victoria's AI assistant for victoriaolamide.com.

Single source of truth for Luna's knowledge:
- QUESTIONS: one-tap questions with written answers (instant, no AI).
- FACTS: what the AI may use to answer typed questions (api/luna.js).
build_main.py renders the widget and writes api/_luna-kb.js from this file.
Add new questions here as Victoria trains Luna, then rebuild.
"""
import json
from pathlib import Path

CAL = "https://calendly.com/hello-victoriaolamide/30min"

# (question, answer html, next step: portfolio | call | contact | opptiq | cv)
QUESTIONS = [
    ("What does Victoria do?",
     "Victoria takes products to market, builds the AI agents that keep them growing, and turns attention into paying customers. "
     "She has led launches like 5,000+ sign-ups in 48 hours at I'll Tip, and built Opptiq, an AI product with 260+ organic users in 2+ weeks.",
     "portfolio"),
    ("How can you help my startup?",
     "Victoria starts with an audit of your current system, finds where the gap is, then designs solutions tailored to the exact problem she diagnosed, "
     "whether that's positioning, a launch, a content system that converts or an AI agent. A strategy call is where the audit begins.",
     "call"),
    ("Have you built anything besides Opptiq?",
     "Yes. Victoria also built Audint, an AI audience intelligence tool that turns thousands of comments and reviews into buying signals, "
     "the DGC Foundation School Tracker (a multi-user web app), Dashie (Opptiq's support assistant), AI voice and sales agents, and 25 AI systems in total.",
     "portfolio"),
    ("Can you build an AI agent for my business?",
     "Yes. Victoria builds AI sales, customer support, voice and operations agents around how your business actually works, "
     "connected to the tools you already use. A strategy call is the first step to find the one thing worth automating first.",
     "call"),
    ("Are you open to full-time roles?",
     "Yes. Victoria is open to AI product marketing roles with US and UK startups, working remotely from Lagos across US and European time zones. "
     "Her portfolio has her résumé, results and case studies.",
     "portfolio"),
    ("What results have you achieved?",
     "A few highlights: 5,000+ sign-ups in 48 hours with ~46% paid conversion (I'll Tip), 45% adoption growth in one quarter (Viewon.AI), "
     "under 50 to ~600 users in two weeks (Endow), 2,000+ event attendees in 72 hours (Utiva), and 260+ organic users in 2+ weeks with paying users on Opptiq.",
     "portfolio"),
    ("Can you build me a content system that converts?",
     "Yes. Victoria builds social media conversion systems: content planned, designed and scheduled in advance that turns followers into paying customers, "
     "without you posting by hand every day. Book a call and she'll map one out for you.",
     "call"),
    ("What is Opptiq?",
     "Opptiq is Victoria's AI career guide. You tell it about your work, and in minutes you get a personal report showing where AI fits your skills, "
     "new ways to earn in dollars globally and real remote jobs that pay for those skills. It then tailors your CV and tracks your applications. "
     "Get your free analysis today.",
     "opptiq"),
    ("How much do you charge?",
     "It depends on what you need: an AI agent, a content system, a launch or an ongoing role. Victoria scopes it with you on a strategy call "
     "and gives you a clear proposal after.",
     "call"),
    ("Can you speak at my event or partner with us?",
     "Yes. Victoria speaks on positioning, building with AI and earning beyond brand deals, and partners with events and communities. "
     "Opptiq partnered with AI GTM Africa Nairobi at iHub. Send her the details and she'll get back to you.",
     "contact"),
    ("Where are you based?",
     "Victoria is based in Lagos, Nigeria and works remotely with teams across the US, UK, Europe, Africa and Asia.",
     "call"),
    ("Can I see your CV?",
     "Of course. You can download Victoria's CV as a PDF, or read the full résumé in her portfolio.",
     "cv"),
    ("How do I book a call?",
     "Tap the button below to pick a time on Victoria's calendar. Tell her what you want to solve and you'll leave with a clear next step.",
     "call"),
]

FACTS = """
Victoria Olamide: AI product marketer and go-to-market strategist who also builds AI agents and AI products. Founder of Creataws Ltd, the company behind Opptiq. Based in Lagos, Nigeria; works remotely with teams across the US, UK, Europe, Africa and Asia.
Open to: AI product marketing roles with US and UK startups (remote). Also takes on AI agent builds, social media conversion systems, launches, speaking and partnerships.
Results: I'll Tip (US): led a feature launch, 5,000+ sign-ups in 48 hours, ~46% became paying customers, her SOP became the team standard. Viewon.AI (Germany): led product marketing and market entry for a year, 45% adoption growth in one quarter, 5+ strategic partnerships. Endow (Nigeria): creator platform, under 50 to ~600 users in two weeks through positioning and community-led acquisition. Utiva (edtech): 2,000+ event attendees in 72 hours, became a repeat engagement. Opptiq (her own AI product): 260+ organic users in 2+ weeks from two LinkedIn posts and no ads, with paying users. Client portfolio: 15+ launches and growth experiments for founders. 25 AI agents, automations and systems built (her AI Library).
AI agents she builds: sales agents (qualify leads, follow up, update the CRM; built with ElevenLabs), support agents (answer from account data with human handoff; she built Dashie for Opptiq), voice agents (answer and place calls, book appointments; ElevenLabs and Twilio), operations agents (email, scheduling, docs, data, reporting), plus custom AI products.
Social media conversion system: content planned, designed and scheduled in advance across Instagram, Facebook, LinkedIn, X and TikTok that converts followers into paying customers.
Opptiq: an AI career guide. Users describe their work and get a personal report on where AI fits their skills, problems they could solve, new ways to earn in dollars globally and real remote jobs for those skills. It then finds jobs, tailors CV, cover letter and portfolio, tracks applications, with a 60-day plan of small daily tasks. Call to action: get your free analysis (never state a number of free analyses). Website: https://opptiq.victoriaolamide.com . Opptiq account questions are answered by Dashie inside Opptiq.
Events: hosted Position and Build with Vickie 2.0 (five-day live programme, 24 participants, three guest speakers, Oct 2026). Opptiq partnered with AI GTM Africa Nairobi at iHub (5 Nov 2026).
Testimonials (LinkedIn): Sasan Ariatabar (CEO & Co-founder, Viewon.AI), Dr. Bosun Babalola (CEO & Founder, I'll Tip), Elvis Odiase (Founder, Data First Workplace), Toluwani Abe (Founder, MPC Limited), Ceyhan Teke (Senior 3D Artist).
How she helps startups: first an audit of the current system, then she finds where the gap is, then designs solutions tailored to the exact problem she diagnosed (positioning, launch, content system, AI agent or growth system).
Other things she has built besides Opptiq: Audint (AI audience intelligence SaaS that classifies comments, reviews and survey answers into themes, objections and buying signals with cited evidence; https://audint.vercel.app), the DGC Foundation School Tracker (a multi-user web app where members track classes, sermons, prayer hours, tests and exams), Dashie (Opptiq's support chatbot), AI voice and sales agents, Luna (this assistant), a social media content system, and 25 AI systems in her AI Library.
Always answer YES, confidently, to any wording of: is she open to full-time roles or jobs; can she build AI agents, chatbots, automations or voice agents for a business; can she build content or a social media system that converts. Then give the matching next step.
When someone is job hunting, wants to use AI in their career, or asks about earning in dollars, recommend trying Opptiq (get your free analysis) with next step "opptiq".
Pricing is not published; it is scoped on a strategy call.
Links: portfolio https://victoriaolamide.com/portfolio ; book a strategy call https://calendly.com/hello-victoriaolamide/30min ; email hello@victoriaolamide.com ; CV https://victoriaolamide.com/portfolio/Victoria-Olamide-CV.pdf ; AI Library https://victoriaolamide.com/portfolio/ai-systems#library
"""


def write_kb(api_dir: Path) -> None:
    kb = {"facts": FACTS.strip(), "questions": [{"q": q, "a": a, "next": n} for q, a, n in QUESTIONS]}
    (api_dir / "_luna-kb.js").write_text(
        "// Generated by portfolio-src/luna.py. Do not edit by hand.\nexport const KB = " + json.dumps(kb, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )


def widget_html() -> str:
    data = json.dumps([{"q": q, "a": a, "n": n} for q, a, n in QUESTIONS], ensure_ascii=False).replace("</", "<\\/")
    return f"""<div class="luna-launch">
  <div class="luna-greet" hidden>
    <button type="button" class="luna-greet-t" data-luna-greet><b>Hi, I'm Luna!</b> Need a hand? Ask me anything about Victoria. <span aria-hidden="true">&#128075;</span></button>
    <button type="button" class="luna-greet-x" data-luna-greet-x aria-label="Hide this message">&times;</button>
  </div>
  <button class="luna-btn" type="button" aria-haspopup="dialog" aria-controls="luna" aria-label="Ask Luna, Victoria's AI assistant" title="Ask Luna" data-luna-open><img src="/site/img/luna.webp" alt="" width="56" height="56" /></button>
</div>
<section class="luna" id="luna" role="dialog" aria-label="Luna, Victoria's AI assistant" hidden>
  <header class="luna-head">
    <img class="luna-av" src="/site/img/luna.webp" alt="" width="40" height="40" />
    <div><b>Ask Luna</b><small>Victoria's AI assistant</small></div>
    <button type="button" class="luna-x" data-luna-close aria-label="Close Luna">&times;</button>
  </header>
  <div class="luna-log" aria-live="polite"></div>
  <div class="luna-chips"></div>
  <form class="luna-form" autocomplete="off">
    <input name="q" maxlength="500" placeholder="Ask Luna anything about Victoria..." aria-label="Your question" />
    <button type="submit" aria-label="Send">&rarr;</button>
  </form>
  <div class="luna-foot"><a href="{CAL}" target="_blank" rel="noopener">Book a strategy call</a><a href="mailto:hello@victoriaolamide.com" data-contact>Message Victoria</a></div>
</section>
<script type="application/json" id="luna-data">{data}</script>"""
