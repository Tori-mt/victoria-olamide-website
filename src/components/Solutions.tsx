import { solutions } from "../content/site";
import { Reveal } from "./ui/Reveal";

export function Solutions() {
  return (
    <section className="section solutions" id="solutions">
      <div className="container solutions__grid">
        <div className="solutions__intro">
          <Reveal>
            <span className="section-index">{solutions.index}</span>
            <p className="eyebrow">{solutions.eyebrow}</p>
          </Reveal>
          <Reveal delay={80}>
            <h2 className="display solutions__title">
              {solutions.title[0]}
              <span className="gold">{solutions.title[1]}</span>
            </h2>
          </Reveal>
          <Reveal delay={160}>
            <p className="solutions__text">{solutions.intro}</p>
          </Reveal>
        </div>

        <div className="solutions__list" role="list">
          {solutions.areas.map((area, i) => (
            <Reveal key={area.title} delay={i * 70} as="article">
              <div className="solution-row" role="listitem">
                <span className="solution-row__num" aria-hidden="true">
                  {area.num}
                </span>
                <div className="solution-row__content">
                  <h3 className="solution-row__title">{area.title}</h3>
                  <p className="solution-row__desc">{area.description}</p>
                </div>
              </div>
            </Reveal>
          ))}
          <Reveal delay={360}>
            <p className="solutions__note">{solutions.note}</p>
          </Reveal>
        </div>
      </div>
    </section>
  );
}