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
