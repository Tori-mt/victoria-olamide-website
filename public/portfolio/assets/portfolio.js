// Mobile menu + scroll reveal. No dependencies.
(function () {
  var nav = document.querySelector(".nav");
  var btn = document.querySelector(".menu-btn");
  if (nav && btn) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.querySelector("span").textContent = open ? "Close" : "Menu";
    });
    nav.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("open"); });
    });
  }

  var els = document.querySelectorAll(".rv");
  if (!("IntersectionObserver" in window)) {
    els.forEach(function (el) { el.classList.add("in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
  els.forEach(function (el) { io.observe(el); });
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

// AI Library filter.
document.querySelectorAll("[data-library]").forEach(function (lib) {
  var chips = lib.querySelectorAll(".lchip");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      chips.forEach(function (x) { x.classList.toggle("on", x === c); });
      var f = c.getAttribute("data-f");
      lib.querySelectorAll(".lrow").forEach(function (r) {
        r.classList.toggle("hide", f !== "all" && r.getAttribute("data-c") !== f);
      });
    });
  });
});

// Deep link from the main site: /portfolio/ai-systems?show=sales#library
(function () {
  var show = new URLSearchParams(location.search).get("show");
  var lib = document.querySelector("[data-library]");
  if (!show || !lib) return;
  var panel = lib.querySelector('[data-focus="' + show + '"]');
  if (!panel) return;
  var chips = lib.querySelector(".lchips");
  var rows = lib.querySelectorAll(".lrow");
  panel.hidden = false;
  chips.hidden = true;
  rows.forEach(function (r) {
    var on = (" " + r.getAttribute("data-t") + " ").indexOf(" " + show + " ") > -1;
    r.classList.toggle("hide", !on);
  });
  panel.querySelector(".lall").addEventListener("click", function () {
    panel.hidden = true;
    chips.hidden = false;
    rows.forEach(function (r) { r.classList.remove("hide"); });
    history.replaceState(null, "", location.pathname + "#library");
  });
  document.querySelectorAll(".rv").forEach(function (e) { e.classList.add("in"); });
})();
