import { expertise } from "../content/site";
import { Reveal } from "./ui/Reveal";

export function Expertise() {
  return (
    <section className="section expertise on-light" id="expertise">
      <div className="container">
        <div className="section-head section-head--split">
          <div>
            <Reveal>
              <span className="section-index">{expertise.index}</span>
              <p className="eyebrow">{expertise.eyebrow}</p>
            </Reveal>
            <Reveal delay={80}>
              <h2 className="display">{expertise.title}</h2>
            </Reveal>
          </div>
          <Reveal delay={160}>
            <p className="section-head__intro">{expertise.intro}</p>
          </Reveal>
        </div>

        <div className="expertise__list" role="list">
          {expertise.items.map((item, i) => (
            <Reveal key={item.title} delay={i * 60} as="article">
              <div className="expertise-row" role="listitem">
                <span className="expertise-row__num" aria-hidden="true">
                  {item.num}
                </span>
                <h3 className="expertise-row__title">{item.title}</h3>
                <p className="expertise-row__desc">{item.description}</p>
                <span className="expertise-row__rule" aria-hidden="true" />
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}