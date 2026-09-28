import { useRef, useState, useEffect } from "react";
import { results } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { CountUp } from "./ui/CountUp";

export function Results() {
  const ref = useRef<HTMLDivElement | null>(null);
  const [active, setActive] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    let done = false;
    const trigger = () => {
      if (done) return;
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) {
        done = true;
        setActive(true);
        window.removeEventListener("scroll", trigger);
        window.removeEventListener("resize", trigger);
      }
    };
    trigger();
    if (!done) {
      window.addEventListener("scroll", trigger, { passive: true });
      window.addEventListener("resize", trigger);
    }
    return () => {
      window.removeEventListener("scroll", trigger);
      window.removeEventListener("resize", trigger);
    };
  }, []);

  return (
    <section className="section results" id="results" aria-label="Results and outcomes">
      <div className="container">
        <div className="section-head section-head--split">
          <div>
            <Reveal>
              <span className="section-index">{results.index}</span>
              <p className="eyebrow">{results.eyebrow}</p>
            </Reveal>
            <Reveal delay={80}>
              <h2 className="display">{results.title}</h2>
            </Reveal>
          </div>
          <Reveal delay={160}>
            <p className="section-head__intro">{results.intro}</p>
          </Reveal>
        </div>

        <div className="results__grid" ref={ref}>
          {results.stats.map((stat, i) => (
            <Reveal key={stat.label} className="results__stat-cell" delay={i * 80}>
              <div className="result">
                <span className="result__value" aria-label={`${stat.prefix ?? ""}${stat.value}${stat.suffix} ${stat.label.replace(/\n/g, " ")}`}>
                  <CountUp value={stat.value} prefix={stat.prefix} suffix={stat.suffix} active={active} />
                </span>
                <span className="result__label">{stat.label}</span>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}