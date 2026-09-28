import { footer, site, social } from "../content/site";
import { ArrowUpRight, InstagramIcon, LinkedinIcon, MailIcon, TiktokIcon, XIcon } from "./ui/Icons";

const socialIcons = {
  linkedin: LinkedinIcon,
  instagram: InstagramIcon,
  x: XIcon,
  tiktok: TiktokIcon,
} as const;

export function Footer() {
  return (
    <footer className="footer">
      <div className="container footer__top">
        <div className="footer__top-text">
          <p className="eyebrow">{footer.eyebrow}</p>
          <a
            className="btn btn--gold footer__cta"
            href={footer.cta.href}
            target="_blank"
            rel="noopener noreferrer"
          >
            {footer.cta.label}
            <ArrowUpRight className="btn__arrow" />
          </a>
        </div>
        <a className="footer__email" href={`mailto:${site.brand.email}`}>
          <MailIcon size={15} />
          {site.brand.email}
        </a>
      </div>

      <div className="container footer__inner">
        <div className="footer__brand">
          <p className="footer__name">{footer.name}</p>
          <p className="footer__positioning">{footer.positioning}</p>
          <p className="footer__note">{footer.note}</p>
        </div>

        <div className="footer__side">
          <div className="footer__links">
            {Object.entries(social).map(([key, item]) => {
              const Icon = socialIcons[key as keyof typeof socialIcons];
              return (
                <a
                  key={key}
                  className="footer__social"
                  href={item.url}
                  rel="noopener noreferrer"
                  target="_blank"
                  aria-label={`${site.brand.name} on ${item.label}`}
                >
                  <Icon size={17} />
                </a>
              );
            })}
          </div>
          <p className="footer__copy">{footer.copyright}</p>
        </div>
      </div>
    </footer>
  );
}
