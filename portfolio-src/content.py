"""Shared portfolio content blocks: testimonials, tool logos, AI library.

Used by build.py via the page macros {{testimonials}}, {{tools}}, {{library}}
and {{library_count}}.
"""
from html import escape

# Real LinkedIn recommendations (public on Victoria's profile). "..." marks omitted text.
TESTIMONIALS = [
    ("sasan", "Sasan Ariatabar", "CEO &amp; Co-founder, Viewon.AI",
     "Working with Victoria was an absolute pleasure. She played a huge part in helping us introduce Viewon.AI to the Nigerian market, bringing clarity, structure, and creativity to every stage of the process. What stood out most was her ability to turn ideas into real, measurable results."),
    ("bosun", "Dr. Bosun Babalola", "CEO &amp; Founder, I'll Tip",
     "Victoria did a good job in creating visibility for her work with me on a project, her influence went a long way in generating user acquisition, she is definitely very creative and innovative in her approach and it generates good result."),
    ("elvis", "Elvis Odiase, MBA", "Founder, Data First Workplace&trade;",
     "I've had the pleasure of working with Victoria across multiple projects, and she consistently stands out as a results-oriented professional who truly delivers. She has a strong ability to drive projects forward with clarity and focus, ensuring that outcomes are aligned with goals."),
    ("toluwani", "Toluwani Abe", "Founder, MPC Limited",
     "Victoria is an exceptional individual... she ensures that all product features and strategic initiatives are meticulously aligned with regulatory requirements and internal policies... she has effectively managed cross-functional teams to ensure that all projects are executed smoothly and delivered on time."),
    ("ceyhan", "Ceyhan Teke", "Senior 3D Artist, client",
     "I had a great experience working with Victoria on my latest project. She showed so much dedication and passion to getting the job done. Her experience and exceptional performance really shows that she's great at what she does."),
]

TOOLS_TOP = [  # AI & building
    ("claude", "Claude Code"), ("chatgpt", "ChatGPT"), ("codex", "Codex"), ("gemini", "Gemini"),
    ("anthropic", "Claude API"), ("opencode", "OpenCode"), ("antigravity", "Antigravity"), ("vscode", "VS Code"),
    ("lovable", "Lovable"), ("elevenlabs", "ElevenLabs"), ("twilio", "Twilio"), ("n8n", "n8n"),
    ("ghl", "GoHighLevel"), ("firecrawl", "Firecrawl"), ("supabase", "Supabase"), ("vercel", "Vercel"),
    ("nextjs.svg", "Next.js"), ("github", "GitHub"),
]
TOOLS_BOTTOM = [  # growth, payments & operations
    ("apollo", "Apollo"), ("clay", "Clay"), ("aiark", "AI Ark"), ("notion", "Notion"), ("canva", "Canva"),
    ("meta", "Meta Business Suite"), ("gworkspace", "Google Workspace"), ("slack", "Slack"), ("resend", "Resend"),
    ("paystack", "Paystack"), ("stripe", "Stripe"), ("flutterwave", "Flutterwave"), (None, "REST APIs &amp; webhooks"),
]

CATS = [
    ("agents", "Agents &amp; chatbots"), ("research", "Research &amp; messaging"), ("content", "Content &amp; ads"),
    ("outreach", "Outreach"), ("automation", "Automation"), ("analytics", "Analytics"),
    ("operations", "Operations"), ("products", "AI products"),
]

# (category, name, what it does, stack, link)
LIBRARY = [
    ("agents", "AI Voice Agent", "Answers and places real phone calls, qualifies callers and books appointments, on a real phone number.", "ElevenLabs · Twilio", None),
    ("agents", "AI Sales Agent", "Talks to leads in a natural voice, qualifies them and hands warm prospects to a person.", "ElevenLabs", None),
    ("agents", "Dashie, website support chatbot", "Opptiq's support assistant on every page. Answers billing and report questions from the person's own account, gives AI answers grounded in approved content, accepts voice input and hands sensitive cases to a human. 80+ questions answered.", "Gemini · Supabase · Resend", "https://opptiq.victoriaolamide.com"),
    ("agents", "GoHighLevel chatbot", "A chatbot inside GoHighLevel that answers enquiries and captures leads straight into the CRM.", "GoHighLevel", None),
    ("agents", "AI Business Operations Agent", "Handles recurring operations work, from reporting and admin to coordination across tools.", "Claude Code · MCP", None),
    ("research", "Competitor Analysis Agent", "Researches competitors' positioning, pricing and messaging, then summarises the gaps worth owning.", "Claude · Firecrawl", None),
    ("research", "Product Messaging Assistant", "Turns customer insight into positioning statements, value propositions and launch messaging.", "Claude", None),
    ("research", "Lifecycle email system", "Opptiq's onboarding, campaign and support emails, with preferences, unsubscribes and delivery tracking handled.", "Resend · Supabase", None),
    ("content", "Social content management system", "Plans, renders and schedules carousels and posts across Instagram, Facebook, X and TikTok from short written briefs. Produced two months of content in advance that converted.", "Python · Claude Code · Meta Business Suite", None),
    ("content", "Meta Ads Strategy Agent", "Drafts audiences, angles and ad copy for Meta campaigns, ready for human approval.", "Claude · Meta", None),
    ("content", "Facebook Ads Automation", "Builds and manages Facebook ad drafts end to end, with approval required before anything goes live.", "Meta Business Suite", None),
    ("outreach", "Personalised cold email system", "Researches each prospect and sends a personalised email with tailored attachments, one prospect at a time.", "Apollo · Clay · Claude Code", None),
    ("outreach", "Outbound GTM System", "Finds, enriches and prioritises target accounts and contacts, then feeds them into personalised outreach.", "Apollo · Clay · AI Ark", None),
    ("automation", "GoHighLevel automation", "Pipelines, follow-ups and booking workflows automated inside GoHighLevel.", "GoHighLevel · n8n", None),
    ("automation", "Website &amp; full-funnel automation", "Landing page, sign-up, payment, onboarding emails and follow-up, connected into one flow.", "Next.js · Supabase · Paystack · Resend", None),
    ("analytics", "Marketing &amp; sales analytics dashboard", "One view of traffic, sign-ups, conversions and revenue, so decisions come from data.", "Supabase", None),
    ("analytics", "Meta ads attribution tracker", "Tracks visitors from Meta ads into Opptiq, so every sign-up and payment can be traced back to its ad.", "Supabase · Meta", None),
    ("operations", "Claude Code AI assistant", "My AI operator for Creataws: drafts outreach, prepares decks and emails, reads product data, ships code and keeps memory between sessions, with my approval on anything that publishes or spends.", "Claude Code · MCP", None),
    ("operations", "MCPs, APIs &amp; PC automation", "Connects AI to Gmail, Calendar, Drive, Supabase, Vercel, GitHub and the browser, plus file and desktop tasks.", "MCP · REST APIs", None),
    ("operations", "Google Workspace CLI", "Schedules meetings, sends invites and manages Drive files and Docs straight from the command line.", "Google Workspace", None),
    ("operations", "Marketing &amp; sales agent skills", "Reusable AI skills, like my carousel skill, that produce on-brand work the same way every time.", "Claude Code", None),
    ("products", "Learning management system", "Inside Opptiq: class recordings, a 30-day action plan, task tracking, scores, a leaderboard and a certificate.", "Next.js · Supabase", "https://opptiq.victoriaolamide.com"),
    ("products", "Opptiq career opportunity engine", "Shows people where AI fits their work, backed by live job-market evidence. 180+ analyses and 130+ action plans.", "Gemini · O*NET · job APIs", "https://opptiq.victoriaolamide.com"),
    ("products", "Audint audience intelligence engine", "Classifies thousands of audience conversations into 10 insight categories, every count backed by cited evidence.", "Gemini or Claude · Supabase", "https://audint.vercel.app"),
    ("products", "Websites &amp; landing pages with AI", "Opptiq, Audint, a church training tracker and this portfolio, specified, built and shipped with AI tools.", "Claude Code · Lovable · Vercel", None),
]


# Which library items each agent card on the main site opens (?show=<tag> on the AI Agents page).
FOCUS = {
    "sales": ("AI Sales Agents", "Agents that talk to leads, qualify them, follow up and keep your pipeline moving, so no lead goes cold.",
              ["AI Sales Agent", "Personalised cold email system", "Outbound GTM System", "GoHighLevel automation"]),
    "support": ("AI Support Agents", "Agents that answer customers instantly, from their own account data, and hand sensitive cases to a person.",
                ["Dashie, website support chatbot", "GoHighLevel chatbot", "Lifecycle email system"]),
    "voice": ("AI Voice Agents", "Agents that answer and place real phone calls, qualify callers and book appointments, day or night.",
              ["AI Voice Agent", "AI Sales Agent"]),
    "ops": ("AI Operations Agents", "Agents that handle email, scheduling, documents, data and reporting across the tools a team already uses.",
            ["AI Business Operations Agent", "Claude Code AI assistant", "MCPs, APIs &amp; PC automation", "Google Workspace CLI", "Marketing &amp; sales agent skills"]),
}


def _tags(name):
    return " ".join(k for k, (_t, _d, names) in FOCUS.items() if name in names)


def testimonials() -> str:
    slides = "".join(
        f'<figure class="tslide"><blockquote>{q}</blockquote>'
        f'<figcaption><img src="/portfolio/img/people/{img}.jpg" alt="{name}" width="64" height="64" loading="lazy" />'
        f'<b>{name}</b><span>{role}</span><small>LinkedIn recommendation</small></figcaption></figure>'
        for img, name, role, q in TESTIMONIALS
    )
    dots = "".join(f'<button class="tdot" aria-label="Show recommendation {i + 1}"></button>' for i in range(len(TESTIMONIALS)))
    return (f'<div class="tcar" data-carousel><div class="ttrack" tabindex="0" aria-label="Recommendations">{slides}</div>'
            f'<div class="tnav"><button class="tbtn prev" aria-label="Previous">&larr;</button><div class="tdots">{dots}</div>'
            f'<button class="tbtn next" aria-label="Next">&rarr;</button></div></div>')


def _row(items, cls):
    def chip(logo, label):
        if logo is None:
            ic = '<span class="tl-ico code">&lt;/&gt;</span>'
        else:
            src = logo if logo.endswith(".svg") else f"{logo}.png"
            ic = f'<img class="tl-ico" src="/portfolio/img/logos/{src}" alt="" width="22" height="22" loading="lazy" />'
        return f'<span class="tl">{ic}{label}</span>'
    group = "".join(chip(l, t) for l, t in items)
    return f'<div class="marquee {cls}"><div class="mtrack">{group}{group}</div></div>'


def tools() -> str:
    return _row(TOOLS_TOP, "left") + _row(TOOLS_BOTTOM, "right")


def library() -> str:
    counts = {k: sum(1 for c, *_ in LIBRARY if c == k) for k, _ in CATS}
    chips = f'<button class="lchip on" data-f="all">All systems ({len(LIBRARY)})</button>' + "".join(
        f'<button class="lchip" data-f="{k}">{label} ({counts[k]})</button>' for k, label in CATS if counts[k])
    labels = dict(CATS)
    rows = ""
    for i, (cat, name, what, stack, link) in enumerate(LIBRARY, 1):
        live = f'<a class="link" href="{link}" target="_blank" rel="noopener">See it live &nearr;</a>' if link else ""
        rows += (f'<details class="lrow" data-c="{cat}" data-t="{_tags(name)}"><summary><span class="ln">{i:02d}</span><span class="lt">{name}</span>'
                 f'<span class="lcat">{labels[cat]}</span><span class="lplus" aria-hidden="true"></span></summary>'
                 f'<div class="lbody"><p>{what}</p><div class="lmeta"><span class="metric">{escape(stack, quote=False)}</span>{live}</div></div></details>')
    focus = "".join(
        f'<div class="lfocus" data-focus="{k}" hidden><span class="eyebrow">You opened</span><h3>{t}</h3><p>{d}</p>'
        f'<p class="lfn">Here are the {len(n)} I have built. <button type="button" class="lall">Show all {len(LIBRARY)} systems</button></p></div>'
        for k, (t, d, n) in FOCUS.items()
    )
    return (f'<div class="lib" data-library>{focus}<div class="lchips" role="group" aria-label="Filter by type">{chips}</div>'
            f'<div class="lrows">{rows}</div></div>')


def library_count() -> str:
    return str(len(LIBRARY))
