import { about } from "../content/site";
import { Reveal } from "./ui/Reveal";

export function About() {
  return (
    <section className="section about on-light" id="about">
      <div className="container about__grid">
        <div className="about__text">
          <Reveal>
            <p className="eyebrow">{about.eyebrow}</p>
          </Reveal>

          <Reveal delay={80}>
            <h2 className="display about__title">
              {about.headlineTop}
              <br />
              <span className="gold">{about.headlineGold}</span>
            </h2>
          </Reveal>
        </div>

        <Reveal delay={160} className="about__bio">
          {about.paragraphs.map((p, i) => (
            <p className="about__para" key={p} data-lead={i === 0 ? "true" : undefined}>
              {p}
            </p>
          ))}
        </Reveal>
      </div>
    </section>
  );
}
