import { insights, site } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { ArrowUpRight } from "./ui/Icons";

export function Insights() {
  return (
    <section className="section insights" id="insights">
      <div className="container">
        <div className="section-head section-head--split">
          <div>
            <Reveal>
              <span className="section-index">{insights.index}</span>
              <p className="eyebrow">{insights.eyebrow}</p>
            </Reveal>
            <Reveal delay={80}>
              <h2 className="display">{insights.title}</h2>
            </Reveal>
          </div>
          <Reveal delay={160}>
            <p className="section-head__intro">{insights.intro}</p>
          </Reveal>
        </div>

        <ul className="insights__list">
          {insights.topics.map((t, i) => (
            <Reveal key={t.category} delay={i * 50} as="li">
              <div className="insight-row">
                <span className="insight-row__category">{t.category}</span>
                <span className="insight-row__line">{t.line}</span>
              </div>
            </Reveal>
          ))}
        </ul>

        <Reveal className="insights__foot">
          <a className="link-line" href={insights.cta.href} rel="noopener noreferrer" target="_blank">
            {insights.cta.label}
            <ArrowUpRight className="link-line__arrow" />
          </a>
          <span className="insights__note">{site.brand.name} · public writing and work</span>
        </Reveal>
      </div>
    </section>
  );
}