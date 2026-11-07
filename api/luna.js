// Luna, Victoria's AI assistant: answers typed questions on victoriaolamide.com.
// Uses Google Gemini (free tier) with ONLY the facts in _luna-kb.js. Needs GEMINI_API_KEY in Vercel.
import { KB } from "./_luna-kb.js";

const MODELS = (process.env.LUNA_MODELS || "gemini-3.5-flash-lite,gemini-3.1-flash-lite,gemini-3.8-flash").split(",").map((m) => m.trim());
const ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models";
const NEXT = new Set(["portfolio", "call", "contact", "opptiq", "cv", "none"]);

// Light per-instance rate limit: 12 questions per visitor per 10 minutes.
const hits = new Map();
function limited(key) {
  const now = Date.now();
  const list = (hits.get(key) || []).filter((t) => now - t < 600_000);
  list.push(now);
  hits.set(key, list);
  if (hits.size > 5000) hits.clear();
  return list.length > 12;
}

const SYSTEM = `You are Luna, Victoria Olamide's AI assistant on her website victoriaolamide.com.
Your job: answer visitors' questions about Victoria and her work, and guide them to the right next step so they work with her.
Rules:
- Use ONLY the facts below. Never invent numbers, clients, prices, dates or services. If the facts don't cover it, say Victoria will answer personally and suggest "contact" or "call".
- Speak about Victoria in the third person, warmly and confidently. Plain, simple English. No legal terms. No em dashes or en dashes.
- Keep answers under 70 words.
- Questions about an Opptiq account, payments or reports: briefly explain and say Dashie inside Opptiq handles account help; next step "opptiq".
- Off-topic or unsafe requests: politely steer back to how Victoria can help.
- Always pick ONE next step: "portfolio" (see her work / hiring), "call" (book a strategy call), "contact" (message her), "opptiq" (try Opptiq), "cv" (download CV), or "none".
Reply as JSON only: {"answer": "...", "next": "portfolio|call|contact|opptiq|cv|none"}

FACTS:
${KB.facts}`;

function clean(v, max) {
  return String(v ?? "").replace(/[\u0000-\u001f\u007f]/g, " ").trim().slice(0, max);
}

async function ask(model, question, history) {
  const contents = [];
  for (const h of history) contents.push({ role: h.role === "luna" ? "model" : "user", parts: [{ text: clean(h.text, 600) }] });
  contents.push({ role: "user", parts: [{ text: question }] });
  const r = await fetch(`${ENDPOINT}/${model}:generateContent?key=${process.env.GEMINI_API_KEY}`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    signal: AbortSignal.timeout(20_000),
    body: JSON.stringify({
      systemInstruction: { parts: [{ text: SYSTEM }] },
      contents,
      generationConfig: { temperature: 0.4, maxOutputTokens: 3000, responseMimeType: "application/json" },
    }),
  });
  if (!r.ok) throw new Error(`model ${model} ${r.status}`);
  const j = await r.json();
  const text = j?.candidates?.[0]?.content?.parts?.map((p) => p.text || "").join("") || "";
  const parsed = JSON.parse(text);
  const answer = clean(parsed.answer, 900).replace(/[–—]/g, ",");
  if (!answer) throw new Error("empty answer");
  return { answer, next: NEXT.has(parsed.next) ? parsed.next : "none" };
}

export default async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ ok: false });
  }
  let body = req.body;
  if (typeof body === "string") { try { body = JSON.parse(body); } catch { body = {}; } }
  body = body || {};
  const question = clean(body.question, 500);
  if (question.length < 2) return res.status(400).json({ ok: false, error: "Please type a question." });
  const ip = String(req.headers["x-forwarded-for"] || "").split(",")[0].trim() || "anon";
  if (limited(ip)) return res.status(429).json({ ok: false, error: "You've asked a lot of questions. Please book a call or message Victoria directly." });
  if (!process.env.GEMINI_API_KEY) return res.status(503).json({ ok: false, error: "offline" });
  const history = Array.isArray(body.history) ? body.history.slice(-6) : [];
  for (const model of MODELS) {
    try {
      const out = await ask(model, question, history);
      return res.status(200).json({ ok: true, ...out });
    } catch (e) { /* try the next model */ }
  }
  return res.status(503).json({ ok: false, error: "busy" });
}
