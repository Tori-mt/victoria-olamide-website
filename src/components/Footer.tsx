import { footer, site } from "../content/site";
import { LinkedinIcon, MailIcon } from "./ui/Icons";

export function Footer() {
  return (
    <footer className="footer">
      <div className="container footer__inner">
        <div className="footer__brand">
          <p className="footer__name">{footer.name}</p>
          <p className="footer__positioning">{footer.positioning}</p>
          <p className="footer__note">{footer.note}</p>
        </div>

        <div className="footer__side">
          <div className="footer__links">
            <a
              className="footer__social"
              href={site.brand.linkedin.url}
              rel="noopener noreferrer"
              target="_blank"
              aria-label="Victoria Olamide on LinkedIn"
            >
              <LinkedinIcon size={17} />
            </a>
            <a
              className="footer__social"
              href={`mailto:${site.brand.email}`}
              aria-label={`Email ${site.brand.email}`}
            >
              <MailIcon size={17} />
            </a>
          </div>
          <p className="footer__copy">{footer.copyright}</p>
        </div>
      </div>
    </footer>
  );
}