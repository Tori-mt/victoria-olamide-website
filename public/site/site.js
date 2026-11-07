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
