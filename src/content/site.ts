/* ============================================================
   CONTENT. All site copy lives here. Edit to change the site.
   ============================================================ */

export const site = {
  brand: {
    name: "Victoria Olamide",
    positioning:
      "Product Marketing Strategist · Go-to-Market · Agentic AI & Growth",
    url: "https://victoriaolamide.com",
    email: "hello@victoriaolamide.com",
    linkedin: {
      label: "LinkedIn",
      url: "https://www.linkedin.com/in/victoria-olamide",
    },
  },
} as const;

export const navigation = {
  links: [
    { label: "Work", href: "#work" },
    { label: "About", href: "#about" },
    { label: "Expertise", href: "#expertise" },
    { label: "FAQ", href: "#faq" },
  ],
  cta: { label: "Work With Me", href: "mailto:hello@victoriaolamide.com" },
} as const;

export const hero = {
  eyebrow: "Product Marketing · Go-to-Market · Agentic AI",
  name: "Victoria Olamide.",
  tags: ["Product Marketing Strategist", "Go-to-Market · Agentic AI & Growth"],
} as const;

export const results = {
  index: "01",
  eyebrow: "Results",
  title: "What the work delivered.",
  intro:
    "Growth is only real when it can be measured. These figures come from product and go-to-market work I have led or executed.",
  stats: [
    {
      value: 5000,
      prefix: "",
      suffix: "+",
      label: "sign-ups generated\nwithin 24 hours",
    },
    {
      value: 64,
      prefix: "~",
      suffix: "%",
      label: "of launch sign-ups\nbecame paid users",
    },
    {
      value: 45,
      prefix: "",
      suffix: "%",
      label: "Q1 adoption growth\nfor a product",
    },
    {
      value: 5,
      prefix: "",
      suffix: "+",
      label: "partnerships secured\nthrough market expansion",
    },
  ],
} as const;

export const work = {
  index: "02",
  eyebrow: "Selected work",
  title: ["The work. ", "What it delivered."],
  intro:
    "Four engagements where product marketing, go-to-market and growth thinking turned strategy into measurable outcomes.",
  cases: [
    {
      num: "01",
      client: "I'll Tip",
      industry: "Consumer fintech",
      role: "Product Marketing Execution",
      problem:
        "A consumer product entering a competitive market needed to turn attention into sign-ups, fast.",
      done: "Led product marketing and go-to-market execution for the launch.",
      outcome: "5,000+",
      outcomeNote: "sign-ups in 24 hours",
      metrics: ["5,000+ sign-ups (24h)", "~64% paid users"],
    },
    {
      num: "02",
      client: "ViewOn.AI",
      industry: "AI platform",
      role: "Product Marketing · Market Expansion",
      problem:
        "An AI platform needed to grow adoption and expand into new market segments.",
      done: "Shaped positioning and activation, aligned product, sales and marketing around one growth motion, and drove expansion through partnerships.",
      outcome: "45%",
      outcomeNote: "Q1 adoption growth",
      metrics: ["45% Q1 adoption growth", "5+ partnerships"],
    },
    {
      num: "03",
      client: "Endow",
      industry: "Creator platform, Nigeria",
      role: "Product Marketing Execution Partner",
      problem:
        "A creator-focused platform entering the Nigerian market needed to turn a fresh launch into real early usage, fast.",
      done: "Coordinated the product launch and go-to-market execution, combining positioning, community-led acquisition and influencer activation to drive adoption.",
      outcome: "600+",
      outcomeNote: "users in 2 weeks",
      metrics: ["Fewer than 50 to 600+ users in 2 weeks", "Community-led acquisition"],
    },
    {
      num: "04",
      client: "Utiva",
      industry: "Event marketing",
      role: "Product Marketing · Event Growth",
      problem:
        "A time-boxed event needed to convert outreach into real attendance inside a 72-hour window.",
      done: "Led marketing and audience acquisition for the event. The relationship became a repeat engagement.",
      outcome: "2,000+",
      outcomeNote: "attendees in 72 hours",
      metrics: ["2,000+ event attendees (72h)", "Repeat client engagement"],
    },
  ],
  cta: "Discuss a similar problem",
} as const;

export const expertise = {
  index: "03",
  eyebrow: "Expertise",
  title: "What I do.",
  intro:
    "Five disciplines, one objective: measurable business growth.",
  items: [
    {
      num: "01",
      title: "Product Marketing",
      description: "Positioning, customer insight, product messaging, adoption and market strategy.",
    },
    {
      num: "02",
      title: "Go-to-Market",
      description: "Launch strategy, acquisition, demand generation and commercial execution.",
    },
    {
      num: "03",
      title: "Agentic AI",
      description: "Designing and building AI-powered systems and workflows that solve business problems.",
    },
    {
      num: "04",
      title: "Growth",
      description: "Improving acquisition, conversion, adoption and retention: the outcomes that matter.",
    },
    {
      num: "05",
      title: "AI-Enabled Business Systems",
      description: "Connecting strategy, automation and intelligent workflows to improve execution.",
    },
  ],
} as const;

export const about = {
  eyebrow: "About",
  headlineTop: "I build AI-powered systems",
  headlineGold: "for business growth.",
  paragraphs: [
    "Victoria Olamide is a Product Marketing & Growth Strategist helping ambitious founders turn great products into businesses people understand, trust, and choose.",
    "With 5+ years across product marketing, project management, brand strategy, and business growth, she works at the intersection of AI, positioning, go-to-market strategy, and digital visibility.",
    "Her approach goes beyond making a product look good. She helps founders uncover what their market actually cares about, sharpen their positioning, communicate their value clearly, and build growth systems that turn attention into adoption, demand, and revenue.",
    "Through her work with technology-driven brands and startups, Victoria has helped businesses translate complex ideas into compelling market narratives and actionable growth strategies.",
  ],
} as const;

export const faq = {
  index: "04",
  eyebrow: "FAQ",
  title: "Questions before you reach out.",
  intro: "The things most people ask before they message me. If yours is not here, LinkedIn is the fastest way to reach me.",
  items: [
    {
      q: "What do you actually do?",
      a: "I combine product marketing, go-to-market strategy and Agentic AI to help businesses grow. In practice that means positioning, launch execution, and AI-enabled systems that improve acquisition, conversion, adoption or operations.",
    },
    {
      q: "What kind of businesses do you work with?",
      a: "Founders and startups, product teams, growth teams, executives, and businesses adopting AI, generally anyone with a product that needs positioning, a launch that needs to land, or a workflow that needs to move faster.",
    },
    {
      q: "Is this an AI consultancy?",
      a: "No. AI is not the product I sell. It is a tool I use to solve product marketing and go-to-market problems. The strategy comes first, the system gets built around it.",
    },
    {
      q: "Do you build the AI systems yourself, or only advise?",
      a: "I design and build them, pointed at a specific commercial or operational problem: growth, go-to-market, operations, or customer and product systems. The tools are implementation details. The business problem is the point.",
    },
    {
      q: "What does working together look like?",
      a: "The same four steps every time: understand the business problem, apply the right strategy, build the system, measure the outcome. No step gets skipped.",
    },
    {
      q: "How do I start a conversation?",
      a: "LinkedIn is the quickest way to reach me, or email if you prefer. Either way, tell me the business problem you are trying to solve and we will take it from there.",
    },
  ],
  cta: { label: "Connect on LinkedIn", href: "https://www.linkedin.com/in/victoria-olamide" },
} as const;

export const social = {
  linkedin: { label: "LinkedIn", url: "https://www.linkedin.com/in/victoria-olamide" },
  instagram: { label: "Instagram", url: "https://www.instagram.com/victoriaolamide__" },
  x: { label: "X", url: "https://x.com/vickieolamide" },
  tiktok: { label: "TikTok", url: "https://www.tiktok.com/@victoriaolamide_" },
  facebook: { label: "Facebook", url: "https://www.facebook.com/olamide.victoria.31" },
  nestuge: { label: "Nestuge", url: "https://victoriaolamide.nestuge.com" },
} as const;

export const footer = {
  name: "Victoria Olamide",
  positioning: "Product Marketing Strategist · Go-to-Market · Agentic AI & Growth",
  eyebrow: "Let's connect",
  cta: { label: "Connect on LinkedIn", href: "https://www.linkedin.com/in/victoria-olamide" },
  copyright: "© 2026 Victoria Olamide",
  note: "Product marketing. Go-to-market. Agentic AI. Built for growth.",
} as const;