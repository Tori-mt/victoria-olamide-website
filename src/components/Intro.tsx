import { intro } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { ArrowRight } from "./ui/Icons";

export function Intro() {
  return (
    <section className="section intro" id="intro">
      <div className="container intro__inner">
        <Reveal>
          <h2 className="display intro__headline">
            {intro.headlineTop}
            <br />
            <span className="gold">{intro.headlineGold}</span>
          </h2>
        </Reveal>

        <Reveal delay={80}>
          <p className="intro__support">{intro.supporting}</p>
        </Reveal>

        <Reveal delay={140}>
          <div className="intro__actions">
            <a className="btn btn--gold" href={intro.primaryCta.href}>
              {intro.primaryCta.label}
              <ArrowRight className="btn__arrow" />
            </a>
            <a className="btn btn--ghost" href={intro.secondaryCta.href}>
              {intro.secondaryCta.label}
            </a>
          </div>
        </Reveal>

        <Reveal delay={200}>
          <p className="intro__narrative" aria-label="How Victoria works">
            {intro.narrative.map((step, i) => (
              <span className="intro__narrative-step" key={step}>
                {step}
                {i < intro.narrative.length - 1 && (
                  <span className="intro__narrative-arrow" aria-hidden="true">
                    →
                  </span>
                )}
              </span>
            ))}
          </p>
        </Reveal>
      </div>
    </section>
  );
}
