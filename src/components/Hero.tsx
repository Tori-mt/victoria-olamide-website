import { hero } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { Portrait } from "./ui/Portrait";

export function Hero() {
  return (
    <section className="hero" id="top">
      <div className="hero__photo" aria-hidden="true">
        <Portrait className="portrait--hero" />
      </div>
      <div className="hero__scrim" aria-hidden="true" />

      <div className="container hero__inner">
        <div className="hero__content">
          <Reveal>
            <p className="eyebrow">{hero.eyebrow}</p>
          </Reveal>

          <Reveal delay={90}>
            <h1 className="hero__name">{hero.name}</h1>
          </Reveal>

          <Reveal delay={180}>
            <div className="hero__tags">
              {hero.tags.map((tag) => (
                <span className="hero__tag" key={tag}>
                  {tag}
                </span>
              ))}
            </div>
          </Reveal>
        </div>
      </div>

      <a className="hero__scroll" href="#intro" aria-label="Scroll to more">
        <span className="hero__scroll-line" aria-hidden="true" />
        <span className="hero__scroll-label">Scroll</span>
      </a>
    </section>
  );
}
