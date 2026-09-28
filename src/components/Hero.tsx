import { hero, site } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { Portrait } from "./ui/Portrait";
import { ArrowRight } from "./ui/Icons";

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

          <Reveal delay={80}>
            <p className="hero__name">{site.brand.name}</p>
          </Reveal>

          <Reveal delay={150}>
            <h1 className="hero__headline">
              {hero.headlineTop}
              <br />
              <span className="gold">{hero.headlineGold}</span>
            </h1>
          </Reveal>

          <Reveal delay={220}>
            <p className="hero__positioning">{hero.positioning}</p>
          </Reveal>

          <Reveal delay={270}>
            <p className="hero__support">{hero.supporting}</p>
          </Reveal>

          <Reveal delay={330}>
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

          <Reveal delay={390}>
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
      </div>

      <a className="hero__scroll" href="#results" aria-label="Scroll to results">
        <span className="hero__scroll-line" aria-hidden="true" />
        <span className="hero__scroll-label">Scroll</span>
      </a>
    </section>
  );
}
