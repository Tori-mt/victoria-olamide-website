import { useEffect, useState } from "react";

interface CountUpProps {
  value: number;
  prefix?: string;
  suffix?: string;
  active: boolean;
  duration?: number;
  decimals?: number;
}

function formatNumber(n: number, decimals: number) {
  if (decimals === 0) return Math.round(n).toLocaleString("en-US");
  return n.toLocaleString("en-US", {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

export function CountUp({
  value,
  prefix = "",
  suffix = "",
  active,
  duration = 1400,
  decimals = 0,
}: CountUpProps) {
  const [display, setDisplay] = useState(() => formatNumber(0, decimals));

  useEffect(() => {
    if (!active) return;

    const reduced =
      typeof window !== "undefined" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (reduced) {
      setDisplay(formatNumber(value, decimals));
      return;
    }

    let rafId = 0;
    const t0 = performance.now();

    const tick = (now: number) => {
      const progress = Math.min((now - t0) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 4);
      setDisplay(formatNumber(value * eased, decimals));
      if (progress < 1) rafId = requestAnimationFrame(tick);
    };

    rafId = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(rafId);
  }, [active, value, duration, decimals]);

  return (
    <span>
      {prefix && <span className="countup__affix">{prefix}</span>}
      {display}
      {suffix}
    </span>
  );
}