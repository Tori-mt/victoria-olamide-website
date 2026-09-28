import { contact } from "../content/site";
import { Reveal } from "./ui/Reveal";
import { ArrowRight, LinkedinIcon, MailIcon } from "./ui/Icons";

export function Contact() {
  return (
    <section className="section contact" id="contact">
      <div className="container contact__inner">
        <Reveal>
          <span className="section-index">{contact.index}</span>
          <p className="eyebrow">{contact.eyebrow}</p>
        </Reveal>

        <Reveal delay={80}>
          <h2 className="display display--lg contact__title">
            {contact.title[0]}
            <span className="gold">{contact.title[1]}</span>
          </h2>
        </Reveal>

        <Reveal delay={160}>
          <p className="contact__intro">{contact.intro}</p>
        </Reveal>

        <Reveal delay={240}>
          <a className="btn btn--gold contact__cta" href={contact.cta.href}>
            {contact.cta.label}
            <ArrowRight className="btn__arrow" />
          </a>
        </Reveal>

        <Reveal delay={320}>
          <div className="contact__channels">
            <a className="contact__channel" href={`mailto:${contact.email}`}>
              <span className="contact__channel-icon">
                <MailIcon size={15} />
              </span>
              <span className="contact__channel-kicker">Email</span>
              <span className="contact__channel-value">{contact.email}</span>
            </a>
            <a
              className="contact__channel"
              href={contact.linkedin.url}
              rel="noopener noreferrer"
              target="_blank"
            >
              <span className="contact__channel-icon">
                <LinkedinIcon size={15} />
              </span>
              <span className="contact__channel-kicker">LinkedIn</span>
              <span className="contact__channel-value">{contact.linkedin.label}</span>
            </a>
          </div>
        </Reveal>
      </div>
    </section>
  );
}