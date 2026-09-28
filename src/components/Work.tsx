import { work } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { ArrowRight } from "./ui/Icons";

export function Work() {
  return (
    <section className="section work on-light" id="work">
      <div className="container">
        <div className="section-head section-head--split">
          <div>
            <Reveal>
              <span className="section-index">{work.index}</span>
              <p className="eyebrow">{work.eyebrow}</p>
            </Reveal>
            <Reveal delay={80}>
              <h2 className="display">
                {work.title[0]}
                <span className="gold">{work.title[1]}</span>
              </h2>
            </Reveal>
          </div>
          <Reveal delay={160}>
            <p className="section-head__intro">{work.intro}</p>
          </Reveal>
        </div>

        <div className="work__list">
          {work.cases.map((c, i) => (
            <Reveal key={c.client} delay={i * 100}>
              <article className="case-row">
                <header className="case-row__head">
                  <span className="case-row__num">{c.num}</span>
                  <div className="case-row__client">
                    <h3 className="case-row__client-name">{c.client}</h3>
                    <p className="case-row__meta">
                      {c.role}
                      <span className="case-row__dot" aria-hidden="true">
                        ·
                      </span>
                      {c.industry}
                    </p>
                  </div>
                  <p className="case-row__outcome">
                    <span className="case-row__outcome-value">{c.outcome}</span>
                    <span className="case-row__outcome-note">{c.outcomeNote}</span>
                  </p>
                </header>

                <div className="case-row__body">
                  <div className="case-row__cols">
                    <div className="case-row__col">
                      <p className="case-row__kicker">The problem</p>
                      <p className="case-row__text">{c.problem}</p>
                    </div>
                    <div className="case-row__col">
                      <p className="case-row__kicker">What I did</p>
                      <p className="case-row__text">{c.done}</p>
                    </div>
                  </div>
                  <ul className="case-row__metrics" aria-label="Key metrics">
                    {c.metrics.map((m) => (
                      <li className="case-row__metric" key={m}>
                        <span className="case-row__metric-dot" aria-hidden="true" />
                        {m}
                      </li>
                    ))}
                  </ul>
                </div>
              </article>
            </Reveal>
          ))}
        </div>

        <Reveal className="work__foot">
          <a className="link-line" href="mailto:hello@victoriaolamide.com">
            {work.cta}
            <ArrowRight className="link-line__arrow" />
          </a>
        </Reveal>
      </div>
    </section>
  );
}