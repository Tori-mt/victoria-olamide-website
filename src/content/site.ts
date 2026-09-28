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
    { label: "Solutions", href: "#solutions" },
    { label: "Expertise", href: "#expertise" },
    { label: "FAQ", href: "#faq" },
  ],
  cta: { label: "Work With Me", href: "#work-with-me" },
} as const;

export const hero = {
  eyebrow: "Product Marketing · Go-to-Market · Agentic AI",
  headlineTop: "I build AI-powered systems",
  headlineGold: "for business growth.",
  positioning: "Product Marketing · Go-to-Market · Agentic AI & Growth",
  supporting:
    "Product marketing and go-to-market thinking, applied with modern AI to solve acquisition, conversion, adoption and operational problems with measurable outcomes.",
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
  ],
  cta: "Discuss a similar problem",
} as const;

export const solutions = {
  index: "04",
  eyebrow: "Agentic AI · Solutions",
  title: ["AI built around ", "business problems."],
  intro:
    "AI is not the product story. Business improvement is. I design and build AI-enabled systems that sit inside how a company already operates. Each one is pointed at a specific commercial or operational problem.",
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
  index: "05",
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
  index: "03",
  eyebrow: "About",
  title: ["Product thinking. ", "GTM execution. ", "AI systems."],
  paragraphs: [
    "I am a product marketing and go-to-market professional whose work now sits where growth strategy meets Agentic AI.",
    "My focus is the journey a product takes after it is built: positioning, messaging, launch, adoption, and the systems that turn attention into usage, and usage into revenue.",
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

export const faq = {
  index: "06",
  eyebrow: "FAQ",
  title: "Questions before you reach out.",
  intro: "The things most people ask before they message me. If yours is not here, LinkedIn is the fastest way to reach me.",
  items: [
    {
      q: "What do you actually do?",
      a: "I combine product marketing, go-to-market strategy and Agentic AI to help businesses grow. In practice that means positioning, launch execution, and AI-enabled systems that improve acquisition, conversion, adoption or operations.",
    },
    {
      q: "Is this an AI consultancy?",
      a: "No. AI is not the product I sell. It is a tool I use to solve product marketing and go-to-market problems. The strategy comes first, the system gets built around it.",
    },
    {
      q: "Do you build the AI systems yourself, or only advise?",
      a: "I design and build them. The Agentic AI systems section on this site covers the kinds of problems I build for: growth, GTM, operations and customer or product systems.",
    },
    {
      q: "What kind of businesses do you work with?",
      a: "Founders and startups, product teams, growth teams, executives, and businesses adopting AI, generally anyone with a product that needs positioning, a launch that needs to land, or a workflow that needs to move faster.",
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

export const services = {
  index: "07",
  eyebrow: "Work together",
  title: ["Let's build what ", "moves the business."],
  intro:
    "If you have a product that needs positioning, a launch that needs to land, or an operational problem AI could remove, I bring product marketing, GTM and Agentic AI to one table, pointed at a measurable outcome.",
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

export const social = {
  linkedin: { label: "LinkedIn", url: "https://www.linkedin.com/in/victoria-olamide" },
  instagram: { label: "Instagram", url: "#" },
  x: { label: "X", url: "#" },
  tiktok: { label: "TikTok", url: "#" },
} as const;

export const footer = {
  name: "Victoria Olamide",
  positioning: "Product Marketing Strategist · Go-to-Market · Agentic AI & Growth",
  eyebrow: "Let's connect",
  cta: { label: "Connect on LinkedIn", href: "https://www.linkedin.com/in/victoria-olamide" },
  copyright: "© 2026 Victoria Olamide",
  note: "Product marketing. Go-to-market. Agentic AI. Built for growth.",
} as const;