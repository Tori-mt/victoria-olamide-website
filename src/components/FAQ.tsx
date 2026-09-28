import { useState } from "react";
import { faq } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { ArrowUpRight } from "./ui/Icons";

export function FAQ() {
  const [open, setOpen] = useState<number | null>(0);

  return (
    <section className="section faq" id="faq">
      <div className="container">
        <div className="section-head section-head--split">
          <div>
            <Reveal>
              <span className="section-index">{faq.index}</span>
              <p className="eyebrow">{faq.eyebrow}</p>
            </Reveal>
            <Reveal delay={80}>
              <h2 className="display">{faq.title}</h2>
            </Reveal>
          </div>
          <Reveal delay={160}>
            <p className="section-head__intro">{faq.intro}</p>
          </Reveal>
        </div>

        <ul className="faq__list">
          {faq.items.map((item, i) => {
            const isOpen = open === i;
            return (
              <Reveal key={item.q} delay={i * 50} as="li">
                <div className="faq-row">
                  <button
                    type="button"
                    className="faq-row__question"
                    aria-expanded={isOpen}
                    aria-controls={`faq-answer-${i}`}
                    onClick={() => setOpen(isOpen ? null : i)}
                  >
                    <span className="faq-row__num">0{i + 1}</span>
                    <span className="faq-row__q-text">{item.q}</span>
                    <span className="faq-row__toggle" aria-hidden="true">
                      {isOpen ? "−" : "+"}
                    </span>
                  </button>
                  <div
                    className="faq-row__answer"
                    id={`faq-answer-${i}`}
                    role="region"
                    hidden={!isOpen}
                  >
                    <p>{item.a}</p>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </ul>

        <Reveal className="faq__foot">
          <a className="link-line" href={faq.cta.href} rel="noopener noreferrer" target="_blank">
            {faq.cta.label}
            <ArrowUpRight className="link-line__arrow" />
          </a>
        </Reveal>
      </div>
    </section>
  );
}
