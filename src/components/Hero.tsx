import { hero, site } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { Portrait } from "./ui/Portrait";
import { ArrowRight } from "./ui/Icons";

export function Hero() {
  return (
    <section className="hero" id="top">
      <div className="hero__bg" aria-hidden="true" />

      <div className="container hero__inner">
        <div className="hero__content">
          <Reveal>
            <p className="eyebrow">{hero.eyebrow}</p>
          </Reveal>

          <Reveal delay={90}>
            <h1 className="display display--lg hero__title">
              {hero.headlineTop}
              <br />
              <span className="gold">{hero.headlineGold}</span>
            </h1>
          </Reveal>

          <Reveal delay={180}>
            <p className="hero__positioning">{hero.positioning}</p>
          </Reveal>

          <Reveal delay={250}>
            <p className="hero__support">{hero.supporting}</p>
          </Reveal>

          <Reveal delay={320}>
            <div className="hero__actions">
              <a className="btn btn--gold" href={hero.primaryCta.href}>
                {hero.primaryCta.label}
                <ArrowRight className="btn__arrow" />
              </a>
              <a className="btn btn--ghost" href={hero.secondaryCta.href}>
                {hero.secondaryCta.label}
              </a>
            </div>
          </Reveal>

          <Reveal delay={400}>
            <p className="hero__narrative" aria-label="How Victoria works">
              {hero.narrative.map((step, i) => (
                <span className="hero__narrative-step" key={step}>
                  {step}
                  {i < hero.narrative.length - 1 && (
                    <span className="hero__narrative-arrow" aria-hidden="true">
                      →
                    </span>
                  )}
                </span>
              ))}
            </p>
          </Reveal>
        </div>

        <Reveal className="hero__media" delay={180}>
          <Portrait />
          <p className="hero__media-caption">
            <span className="hero__media-tag">Product Marketing + Agentic AI</span>
            <span className="hero__media-note">{site.brand.name}</span>
          </p>
        </Reveal>
      </div>

      <a className="hero__scroll" href="#results" aria-label="Scroll to results">
        <span className="hero__scroll-line" aria-hidden="true" />
        <span className="hero__scroll-label">Scroll</span>
      </a>
    </section>
  );
}