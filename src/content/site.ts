/* ============================================================
   CONTENT — all site copy lives here. Edit to change the site.
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
    { label: "Solutions", href: "#solutions" },
    { label: "Expertise", href: "#expertise" },
    { label: "Insights", href: "#insights" },
    { label: "Contact", href: "#contact" },
  ],
  cta: { label: "Work With Me", href: "#work-with-me" },
} as const;

export const hero = {
  eyebrow: "Product Marketing · Go-to-Market · Agentic AI",
  headlineTop: "I build AI-powered systems",
  headlineGold: "for business growth.",
  positioning: "Product Marketing · Go-to-Market · Agentic AI & Growth",
  supporting:
    "Product marketing and go-to-market thinking, applied with modern AI — to solve acquisition, conversion, adoption and operational problems with measurable outcomes.",
  narrative: ["Strategy", "System", "Execution", "Outcome"],
  primaryCta: { label: "Work With Me", href: "#work-with-me" },
  secondaryCta: { label: "View My Work", href: "#work" },
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
    "Two engagements where product marketing, go-to-market and growth thinking turned strategy into measurable outcomes.",
  cases: [
    {
      num: "01",
      client: "I'll Tip",
      industry: "Consumer fintech",
      role: "Product Marketing Execution",
      problem:
        "A consumer product entering a competitive market needed to turn attention into sign-ups — fast.",
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
  ],
  cta: "Discuss a similar problem",
} as const;

export const solutions = {
  index: "03",
  eyebrow: "Agentic AI · Solutions",
  title: ["AI built around ", "business problems."],
  intro:
    "AI is not the product story. Business improvement is. I design and build AI-enabled systems that sit inside how a company already operates — each one pointed at a specific commercial or operational problem.",
  areas: [
    {
      num: "01",
      title: "Growth Systems",
      description: "AI-enabled systems that help businesses acquire, nurture and convert users.",
    },
    {
      num: "02",
      title: "GTM Systems",
      description: "Workflows that sharpen research, positioning, launch execution and lead generation.",
    },
    {
      num: "03",
      title: "Operations",
      description: "Agentic workflows that remove repetitive manual work and improve execution speed.",
    },
    {
      num: "04",
      title: "Customer & Product Systems",
      description: "AI-enabled capabilities supporting adoption, customer experience, research and retention.",
    },
    {
      num: "05",
      title: "Custom Solutions",
      description: "Purpose-built Agentic AI systems designed around a specific operational or commercial problem.",
    },
  ],
  note: "The tools are implementation details. The business problem is the point.",
} as const;

export const expertise = {
  index: "04",
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
      description: "Improving acquisition, conversion, adoption and retention — the outcomes that matter.",
    },
    {
      num: "05",
      title: "AI-Enabled Business Systems",
      description: "Connecting strategy, automation and intelligent workflows to improve execution.",
    },
  ],
} as const;

export const about = {
  index: "05",
  eyebrow: "About",
  title: ["Product thinking. ", "GTM execution. ", "AI systems."],
  paragraphs: [
    "I am a product marketing and go-to-market professional whose work now sits where growth strategy meets Agentic AI.",
    "My focus is the journey a product takes after it is built — positioning, messaging, launch, adoption, and the systems that turn attention into usage, and usage into revenue.",
    "I apply AI where it changes the outcome: research and insight, go-to-market execution, workflows, and the repetitive work that slows teams down.",
    "The through-line is simple. Understand the business problem. Apply the right strategy. Build the system. Measure the outcome.",
  ],
  principles: [
    { label: "1", text: "Understand the business problem" },
    { label: "2", text: "Apply the right strategy" },
    { label: "3", text: "Build the system" },
    { label: "4", text: "Measure the outcome" },
  ],
} as const;

export const insights = {
  index: "06",
  eyebrow: "Insights",
  title: "Ideas I keep working through.",
  intro: "Public thinking on the subjects behind the work.",
  topics: [
    { category: "Product Marketing", line: "Positioning and messaging that survive contact with the market." },
    { category: "Go-to-Market", line: "Treating launches as systems, not events." },
    { category: "Agentic AI", line: "What changes when machines execute the workflow." },
    { category: "AI-Enabled Growth", line: "Where automation creates compounding, not just speed." },
    { category: "Product Adoption", line: "Moving past features to actual usage." },
    { category: "Business Systems", line: "Workflows that turn strategy into execution." },
  ],
  cta: { label: "Follow on LinkedIn", href: "https://www.linkedin.com/in/victoria-olamide" },
} as const;

export const services = {
  index: "07",
  eyebrow: "Work together",
  title: ["Let's build what ", "moves the business."],
  intro:
    "If you have a product that needs positioning, a launch that needs to land, or an operational problem AI could remove — I bring product marketing, GTM and Agentic AI to one table, pointed at a measurable outcome.",
  audience: [
    "Founders & startups",
    "Product teams",
    "Growth teams",
    "Executives",
    "Businesses adopting AI",
  ],
  primaryCta: { label: "Work With Me", href: "mailto:hello@victoriaolamide.com" },
  secondaryCta: { label: "Book a strategy call", href: "mailto:hello@victoriaolamide.com?subject=Strategy%20Call" },
} as const;

export const contact = {
  index: "08",
  eyebrow: "Contact",
  title: ["Start with the ", "business problem."],
  intro:
    "Tell me what you need to move — a launch, an adoption number, a workflow — and we will talk about whether and how to build it.",
  email: "hello@victoriaolamide.com",
  linkedin: {
    label: "Victoria Olamide",
    url: "https://www.linkedin.com/in/victoria-olamide",
  },
  cta: { label: "Start a Conversation", href: "mailto:hello@victoriaolamide.com" },
} as const;

export const footer = {
  name: "Victoria Olamide",
  positioning: "Product Marketing Strategist · Go-to-Market · Agentic AI & Growth",
  copyright: "© 2026 Victoria Olamide",
  note: "Product marketing. Go-to-market. Agentic AI. Built for growth.",
} as const;