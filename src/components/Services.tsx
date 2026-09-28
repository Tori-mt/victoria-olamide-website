import { services, social } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { ArrowRight, ArrowUpRight } from "./ui/Icons";

export function Services() {
  return (
    <section className="section services on-light" id="work-with-me">
      <div className="container">
        <div className="section-head section-head--split">
          <div>
            <Reveal>
              <span className="section-index">{services.index}</span>
              <p className="eyebrow">{services.eyebrow}</p>
            </Reveal>
            <Reveal delay={80}>
              <h2 className="display">
                {services.title[0]}
                <span className="gold">{services.title[1]}</span>
              </h2>
            </Reveal>
          </div>
          <Reveal delay={160}>
            <p className="section-head__intro">{services.intro}</p>
          </Reveal>
        </div>

        <div className="services__panel">
          <p className="services__lead">{services.lead}</p>
          <div className="services__ctas">
            <a className="btn btn--gold services__cta" href={services.primaryCta.href}>
              {services.primaryCta.label}
              <ArrowRight className="btn__arrow" />
            </a>
            <a className="link-line services__cta-link" href={services.secondaryCta.href}>
              {services.secondaryCta.label}
              <ArrowRight className="link-line__arrow" />
            </a>
            <a
              className="link-line services__cta-link"
              href={social.linkedin.url}
              target="_blank"
              rel="noopener noreferrer"
            >
              Or connect on LinkedIn
              <ArrowUpRight className="link-line__arrow" />
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}
