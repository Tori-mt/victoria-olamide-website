// Contact form for victoriaolamide.com (Vercel serverless function).
// Sends the visitor's message to hello@victoriaolamide.com through Resend, with the visitor's
// address as reply-to. Needs RESEND_API_KEY (and optionally CONTACT_FROM / CONTACT_TO) in Vercel.

const TO = process.env.CONTACT_TO || "hello@victoriaolamide.com";
const FROM = process.env.CONTACT_FROM || "Victoria Olamide website <hello@victoriaolamide.com>";

function clean(v, max) {
  return String(v ?? "").replace(/[\u0000-\u001f\u007f]/g, " ").trim().slice(0, max);
}
function esc(s) {
  return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

export default async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ ok: false, error: "Method not allowed" });
  }
  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch { body = {}; }
  }
  body = body || {};

  // Honeypot: real visitors never fill the hidden "company" field.
  if (clean(body.company, 200)) return res.status(200).json({ ok: true });

  const name = clean(body.name, 120);
  const email = clean(body.email, 200);
  const message = String(body.message ?? "").trim().slice(0, 5000);
  if (!name || !message || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) {
    return res.status(400).json({ ok: false, error: "Please add your name, a valid email and a message." });
  }
  if (!process.env.RESEND_API_KEY) {
    return res.status(503).json({ ok: false, error: "Email is not set up yet." });
  }

  const html = `<p><strong>From:</strong> ${esc(name)} &lt;${esc(email)}&gt;</p><p style="white-space:pre-wrap">${esc(message)}</p><p style="color:#888;font-size:12px">Sent from the contact form on victoriaolamide.com</p>`;
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { authorization: `Bearer ${process.env.RESEND_API_KEY}`, "content-type": "application/json" },
    body: JSON.stringify({
      from: FROM,
      to: [TO],
      reply_to: email,
      subject: `Website message from ${name}`,
      html,
      text: `From: ${name} <${email}>\n\n${message}`,
    }),
  });
  if (!r.ok) {
    return res.status(502).json({ ok: false, error: "Could not send right now. Please email hello@victoriaolamide.com." });
  }
  return res.status(200).json({ ok: true });
}
