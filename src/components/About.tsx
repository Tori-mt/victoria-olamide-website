import { about } from "../content/site";
import { Reveal } from "./ui/Reveal";

export function About() {
  return (
    <section className="section about" id="about">
      <div className="container about__grid">
        <div className="about__text">
          <Reveal>
            <span className="section-index">{about.index}</span>
            <p className="eyebrow">{about.eyebrow}</p>
          </Reveal>

          <Reveal delay={80}>
            <h2 className="display about__title">
              {about.title.map((line, i) => (
                <span key={line} className={i === about.title.length - 1 ? "gold" : undefined}>
                  {line}
                  {i < about.title.length - 1 && <br />}
                </span>
              ))}
            </h2>
          </Reveal>

          <Reveal delay={160}>
            {about.paragraphs.map((p, i) => (
              <p className="about__para" key={p} data-lead={i === 0 ? "true" : undefined}>
                {p}
              </p>
            ))}
          </Reveal>
        </div>

        <Reveal delay={220} className="about__visual">
          <div className="about__principles">
            <p className="about__principles-kicker">How I work</p>
            <ol className="about__steps">
              {about.principles.map((p) => (
                <li className="about__step" key={p.text}>
                  <span className="about__step-label" aria-hidden="true">
                    {p.label}
                  </span>
                  <span className="about__step-text">{p.text}</span>
                </li>
              ))}
            </ol>
            <p className="about__principles-foot">
              Product marketing. Go-to-market. Agentic AI. One working method.
            </p>
          </div>
        </Reveal>
      </div>
    </section>
  );
}