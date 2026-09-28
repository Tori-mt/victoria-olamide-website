import { useEffect, useRef, useState } from "react";

interface CountUpOptions {
  duration?: number;
  decimals?: number;
  start?: number;
}

export function useCountUp(target: number, active: boolean, options: CountUpOptions = {}) {
  const { duration = 1400, decimals = 0, start = 0 } = options;
  const [value, setValue] = useState(numberToDisplay(start, decimals));

  function numberToDisplay(n: number, d: number) {
    if (d === 0) return Math.round(n).toLocaleString("en-US");
    return n.toLocaleString("en-US", {
      minimumFractionDigits: d,
      maximumFractionDigits: d,
    });
  }

  useEffect(() => {
    if (!active) return;

    const prefersReduced =
      typeof window !== "undefined" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (prefersReduced) {
      setValue(numberToDisplay(target, decimals));
      return;
    }

    let rafId = 0;
    const t0 = performance.now();

    const tick = (now: number) => {
      const progress = Math.min((now - t0) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 4);
      setValue(numberToDisplay(start + (target - start) * eased, decimals));
      if (progress < 1) rafId = requestAnimationFrame(tick);
    };

    rafId = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(rafId);
  }, [active, target, duration, decimals, start]);

  return value;
}

export function usePrefersReducedMotion() {
  const [reduced, setReduced] = useState(
    () => typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches,
  );

  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    setReduced(mq.matches);
    const onChange = (e: MediaQueryListEvent) => setReduced(e.matches);
    mq.addEventListener?.("change", onChange);
    return () => mq.removeEventListener?.("change", onChange);
  }, []);

  return reduced;
}

export function useScrolledPast(threshold: number) {
  const ref = useRef(false);
  const [scrolledPast, setScrolledPast] = useState(false);
  useEffect(() => {
    const onScroll = () => {
      const past = window.scrollY > threshold;
      if (past !== ref.current) {
        ref.current = past;
        setScrolledPast(past);
      }
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, [threshold]);
  return scrolledPast;
}