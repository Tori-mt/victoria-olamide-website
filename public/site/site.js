(function () {
  var nav = document.querySelector(".nav");
  var btn = document.querySelector(".menu");
  function onScroll() { if (nav) nav.classList.toggle("solid", window.scrollY > 40); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (btn) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.textContent = open ? "Close" : "Menu";
    });
    nav.querySelectorAll(".links a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("open"); btn.textContent = "Menu"; });
    });
    // outside click closes menu
    function closeMenu() { nav.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); btn.textContent = "Menu"; }
    document.addEventListener("click", function (e) { if (nav.classList.contains("open") && !nav.contains(e.target)) closeMenu(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav.classList.contains("open")) { closeMenu(); btn.focus(); } });
  }
  var els = document.querySelectorAll(".rv");
  if (!("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("in"); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
  els.forEach(function (e) { io.observe(e); });
})();

// Testimonials: autoplay, swipe (native scroll-snap), dots, arrows.
document.querySelectorAll("[data-carousel]").forEach(function (car) {
  var track = car.querySelector(".ttrack");
  var slides = track.children;
  var dots = car.querySelectorAll(".tdot");
  var i = 0, timer = null;
  function go(n) {
    i = (n + slides.length) % slides.length;
    track.scrollTo({ left: slides[i].offsetLeft - slides[0].offsetLeft, behavior: "smooth" });
  }
  function mark() {
    var step = slides[0].offsetWidth + 16;
    i = Math.round(track.scrollLeft / step);
    dots.forEach(function (d, k) { d.classList.toggle("on", k === i); });
  }
  function stop() { if (timer) clearInterval(timer); timer = null; }
  function play() {
    stop();
    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      timer = setInterval(function () { go(i + 1); }, 6500);
    }
  }
  track.addEventListener("scroll", function () { window.requestAnimationFrame(mark); }, { passive: true });
  car.querySelector(".prev").addEventListener("click", function () { go(i - 1); play(); });
  car.querySelector(".next").addEventListener("click", function () { go(i + 1); play(); });
  dots.forEach(function (d, k) { d.addEventListener("click", function () { go(k); play(); }); });
  car.addEventListener("mouseenter", stop);
  car.addEventListener("mouseleave", play);
  track.addEventListener("touchstart", stop, { passive: true });
  track.addEventListener("touchend", play, { passive: true });
  mark();
  play();
});


// Contact dialog: opens from any [data-contact] link, posts to /api/contact.
(function () {
  var dlg = document.getElementById("contact");
  if (!dlg || typeof dlg.showModal !== "function") return; // old browsers keep the mailto link
  var form = dlg.querySelector("form");
  var status = dlg.querySelector(".cstatus");
  var btn = form.querySelector('button[type="submit"]');
  document.querySelectorAll("[data-contact]").forEach(function (a) {
    a.addEventListener("click", function (e) { e.preventDefault(); status.textContent = ""; status.className = "cstatus"; dlg.showModal(); });
  });
  dlg.querySelector("[data-close]").addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var data = Object.fromEntries(new FormData(form).entries());
    if (!data.name || !data.message || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(data.email || "")) {
      status.className = "cstatus err"; status.textContent = "Please add your name, a valid email and a message."; return;
    }
    btn.disabled = true; status.className = "cstatus"; status.textContent = "Sending...";
    fetch("/api/contact", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return { ok: false }; }); })
      .then(function (j) {
        if (j.ok) { status.className = "cstatus ok"; status.textContent = "Thank you! Your message is on its way. I'll reply to your email soon."; form.reset(); }
        else { status.className = "cstatus err"; status.innerHTML = (j.error || "Something went wrong.") + ' You can also email <a href="mailto:hello@victoriaolamide.com">hello@victoriaolamide.com</a>.'; }
      })
      .catch(function () { status.className = "cstatus err"; status.innerHTML = 'Could not send right now. Please email <a href="mailto:hello@victoriaolamide.com">hello@victoriaolamide.com</a>.'; })
      .then(function () { btn.disabled = false; });
  });
})();

// Logo and name always go back to the top of the home page.
document.querySelectorAll("[data-home]").forEach(function (a) {
  a.addEventListener("click", function (e) {
    if (location.pathname === "/" || location.pathname === "/index.html") {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
      history.replaceState(null, "", "/");
      var nav = document.querySelector(".nav");
      if (nav) nav.classList.remove("open");
    }
  });
});

// ===== Motion (7 Nov 2026) =====
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Numbers count up when they scroll into view: "5,000+", "~46%", "260+", "45%" ...
  var nums = document.querySelectorAll(".stat b");
  nums.forEach(function (el) {
    var m = el.textContent.trim().match(/^([^\d]*)([\d,]+)(.*)$/);
    if (!m) return;
    el.setAttribute("data-count", "");
    el._pre = m[1]; el._n = parseInt(m[2].replace(/,/g, ""), 10); el._suf = m[3]; el._comma = m[2].indexOf(",") > -1;
  });
  function fmt(el, v) {
    var s = el._comma ? Math.round(v).toLocaleString("en-US") : String(Math.round(v));
    el.textContent = el._pre + s + el._suf;
  }
  function run(el) {
    if (el._done || el._n === undefined) return;
    el._done = true;
    if (reduce) return;
    var dur = 1400 + Math.min(el._n, 5000) / 5, t0 = null;
    fmt(el, 0);
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      fmt(el, el._n * e);
      if (p < 1) requestAnimationFrame(step); else fmt(el, el._n);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } });
    }, { threshold: 0.6 });
    nums.forEach(function (el) { if (el._n !== undefined) io.observe(el); });
  }

  // FAQ: a soft pop sound and a zoom as you move between questions and open one.
  var ctx = null, last = 0;
  function pop(vol) {
    try {
      var now = Date.now();
      if (now - last < 90) return;
      last = now;
      ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
      if (ctx.state === "suspended") ctx.resume();
      var o = ctx.createOscillator(), g = ctx.createGain(), t = ctx.currentTime;
      o.type = "sine";
      o.frequency.setValueAtTime(620, t);
      o.frequency.exponentialRampToValueAtTime(240, t + 0.09);
      g.gain.setValueAtTime(0.0001, t);
      g.gain.exponentialRampToValueAtTime(vol, t + 0.01);
      g.gain.exponentialRampToValueAtTime(0.0001, t + 0.12);
      o.connect(g); g.connect(ctx.destination);
      o.start(t); o.stop(t + 0.14);
    } catch (e) { /* sound is a nice-to-have */ }
  }
  var unlocked = false;
  ["pointerdown", "keydown", "touchstart"].forEach(function (ev) {
    window.addEventListener(ev, function () { unlocked = true; }, { once: true, passive: true });
  });
  var items = document.querySelectorAll(".faq details");
  items.forEach(function (d) {
    d.addEventListener("mouseenter", function () { if (unlocked && !reduce) pop(0.05); });
    d.addEventListener("toggle", function () {
      if (!d.open) return;
      items.forEach(function (o) { if (o !== d) o.open = false; });
      pop(0.12);
      d.classList.remove("popped"); void d.offsetWidth; d.classList.add("popped");
    });
  });
})();

// ===== Luna, Victoria's AI assistant =====
(function () {
  var panel = document.getElementById("luna");
  if (!panel) return;
  var openBtn = document.querySelector("[data-luna-open]");
  var log = panel.querySelector(".luna-log");
  var chipsBox = panel.querySelector(".luna-chips");
  // Fold the suggestions away after a question so the answer stays readable.
  var moreBtn = document.createElement("button");
  moreBtn.type = "button";
  moreBtn.className = "luna-more";
  moreBtn.setAttribute("aria-expanded", "false");
  moreBtn.textContent = "More questions \u25BE";
  moreBtn.hidden = true;
  chipsBox.parentNode.insertBefore(moreBtn, chipsBox);
  function foldChips() { chipsBox.hidden = true; moreBtn.hidden = false; moreBtn.setAttribute("aria-expanded", "false"); }
  function openChips() { chipsBox.hidden = false; moreBtn.hidden = true; moreBtn.setAttribute("aria-expanded", "true"); var b = chipsBox.querySelector("button"); if (b) b.focus(); }
  moreBtn.addEventListener("click", openChips);
  var form = panel.querySelector(".luna-form");
  var input = form.querySelector("input");
  var QA = JSON.parse(document.getElementById("luna-data").textContent);
  var history = [];
  var started = false;
  var CAL = "https://calendly.com/hello-victoriaolamide/30min";
  var NEXT = {
    portfolio: ['View my portfolio', "/portfolio", false],
    call: ['Book a strategy call', CAL, true],
    contact: ['Message Victoria', "#contact", false],
    opptiq: ['Try Opptiq free', "https://opptiq.victoriaolamide.com", true],
    cv: ['Download CV', "/portfolio/Victoria-Olamide-CV.pdf", false]
  };

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function scroll() { log.scrollTop = log.scrollHeight; }
  function add(who, html, next) {
    var b = document.createElement("div");
    b.className = "luna-msg " + who;
    b.innerHTML = html;
    if (next && NEXT[next]) {
      var n = NEXT[next], a = document.createElement("a");
      a.className = "luna-next";
      a.textContent = n[0] + " →";
      a.href = n[1];
      if (n[2]) { a.target = "_blank"; a.rel = "noopener"; }
      if (next === "contact") a.setAttribute("data-contact", "");
      if (next === "cv") a.setAttribute("download", "");
      b.appendChild(document.createElement("br"));
      b.appendChild(a);
    }
    log.appendChild(b);
    scroll();
    return b;
  }
  function chips(list) {
    chipsBox.innerHTML = "";
    list.forEach(function (item) {
      var c = document.createElement("button");
      c.type = "button";
      c.className = "luna-chip";
      c.textContent = item.q;
      c.addEventListener("click", function () { askChip(item); });
      chipsBox.appendChild(c);
    });
  }
  function askChip(item) {
    foldChips();
    add("me", esc(item.q));
    history.push({ role: "me", text: item.q });
    setTimeout(function () { add("bot", esc(item.a), item.n); history.push({ role: "luna", text: item.a }); }, 350);
    chips(QA.filter(function (x) { return x !== item; }).slice(0, 4));
  }
  // Closest written answer, used when the AI can't be reached.
  function closest(q) {
    var words = q.toLowerCase().match(/[a-z]{3,}/g) || [], best = null, score = 0;
    QA.forEach(function (item) {
      var hay = (item.q + " " + item.a).toLowerCase(), s = 0;
      words.forEach(function (w) { if (hay.indexOf(w) > -1) s++; });
      if (s > score) { score = s; best = item; }
    });
    return score >= 2 ? best : null;
  }
  function wireContact(el) {
    el.querySelectorAll("[data-contact]").forEach(function (a) {
      if (a._w) return; a._w = true;
      a.addEventListener("click", function (e) {
        var d = document.getElementById("contact");
        if (d && d.showModal) { e.preventDefault(); d.showModal(); }
      });
    });
  }
  // Greeting bubble beside the avatar (Victoria, 13 Nov 2026): appears after a moment, closes for this visit.
  var launch = document.querySelector(".luna-launch");
  var greet = launch && launch.querySelector(".luna-greet");
  if (greet) {
    var greetOff = false;
    try { greetOff = sessionStorage.getItem("luna_greet") === "off"; } catch (e) {}
    if (!greetOff) setTimeout(function () { if (panel.hidden) greet.hidden = false; }, 1200);
    launch.querySelector("[data-luna-greet]").addEventListener("click", function () { open(); });
    launch.querySelector("[data-luna-greet-x]").addEventListener("click", function () {
      greet.hidden = true;
      try { sessionStorage.setItem("luna_greet", "off"); } catch (e) {}
    });
  }
  function open() {
    if (launch) launch.classList.add("open");
    panel.hidden = false;
    openBtn.setAttribute("aria-expanded", "true");
    openBtn.classList.add("on");
    if (!started) {
      started = true;
      add("bot", "Hi! I'm Luna, Victoria's AI assistant. Ask me about her work, AI agents, hiring her, or Opptiq. Tap a question or type your own.");
      chips(QA.slice(0, 5));
    }
    setTimeout(function () { input.focus(); }, 50);
  }
  function close() {
    if (launch) launch.classList.remove("open");
    panel.hidden = true;
    openBtn.setAttribute("aria-expanded", "false");
    openBtn.classList.remove("on");
  }
  openBtn.addEventListener("click", function () { panel.hidden ? open() : close(); });
  panel.querySelector("[data-luna-close]").addEventListener("click", close);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) close(); });
  var obs = new MutationObserver(function () { wireContact(log); });
  obs.observe(log, { childList: true });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var q = input.value.trim();
    if (q.length < 2) return;
    input.value = "";
    add("me", esc(q));
    foldChips();
    var typing = add("bot typing", "<span></span><span></span><span></span>");
    fetch("/api/luna", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ question: q, history: history.slice(-6) }) })
      .then(function (r) { return r.json().catch(function () { return { ok: false }; }); })
      .then(function (j) {
        typing.remove();
        if (j.ok) { add("bot", esc(j.answer), j.next); history.push({ role: "me", text: q }, { role: "luna", text: j.answer }); return; }
        if (j.error && j.error.indexOf("lot of questions") > -1) { add("bot", esc(j.error), "call"); return; }
        var best = closest(q);
        if (best) add("bot", esc(best.a), best.n);
        else add("bot", "Great question. Victoria will answer that one personally. Send her a message and she'll get back to you.", "contact");
      })
      .catch(function () {
        typing.remove();
        var best = closest(q);
        if (best) add("bot", esc(best.a), best.n);
        else add("bot", "I couldn't reach my brain just now. Send Victoria a message and she'll reply personally.", "contact");
      });
  });
})();

// Install the app: show quick steps, then send people to Opptiq where the real install button lives.
(function () {
  var dlg = document.getElementById("install");
  if (!dlg || typeof dlg.showModal !== "function") return;
  document.querySelectorAll("[data-install]").forEach(function (a) {
    a.addEventListener("click", function (e) { e.preventDefault(); dlg.showModal(); });
  });
  dlg.querySelector("[data-close-install]").addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
})();

// ===== Visitor stats (Victoria's admin page, 13 Nov 2026) =====
// One anonymous page view per visit: a random id kept in this browser, the page and where the visitor came
// from. Country and city are added by the server; no names or IP addresses are stored.
(function () {
  try {
    var id = "";
    try {
      id = localStorage.getItem("vo_vid") || "";
      if (!id && window.crypto && crypto.randomUUID) { id = crypto.randomUUID(); localStorage.setItem("vo_vid", id); }
    } catch (e) {}
    var data = JSON.stringify({ v: id, p: location.pathname, r: document.referrer });
    var url = "https://opptiq.victoriaolamide.com/api/v";
    if (!(navigator.sendBeacon && navigator.sendBeacon(url, new Blob([data], { type: "text/plain" })))) {
      fetch(url, { method: "POST", body: data, keepalive: true, mode: "no-cors" });
    }
  } catch (e) {}
})();
