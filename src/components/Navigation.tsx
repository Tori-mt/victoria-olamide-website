import { useEffect, useState } from "react";
import { navigation, site } from "../content/site";
import { useScrolledPast } from "../hooks/useEffects";

export function Navigation() {
  const scrolled = useScrolledPast(24);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [open]);

  const close = () => setOpen(false);

  return (
    <header className={`nav ${scrolled ? "nav--compact" : ""} ${open ? "nav--open" : ""}`}>
      <div className="nav__inner container">
        <a href="#top" className="nav__brand" onClick={close} aria-label="Victoria Olamide, home">
          {site.brand.name}
        </a>

        <nav className="nav__links" aria-label="Primary">
          {navigation.links.map((link) => (
            <a key={link.href} className="nav__link" href={link.href}>
              {link.label}
            </a>
          ))}
        </nav>

        <a className="btn btn--gold nav__cta" href={navigation.cta.href}>
          {navigation.cta.label}
        </a>

        <button
          className="nav__toggle"
          type="button"
          aria-expanded={open}
          aria-controls="mobile-menu"
          aria-label={open ? "Close menu" : "Open menu"}
          onClick={() => setOpen((v) => !v)}
        >
          <span className="nav__toggle-line" />
          <span className="nav__toggle-line" />
        </button>
      </div>

      <div className="nav__mobile" id="mobile-menu" hidden={!open}>
        <nav aria-label="Mobile">
          {navigation.links.map((link, i) => (
            <a
              key={link.href}
              className="nav__mobile-link"
              href={link.href}
              onClick={close}
              style={{ transitionDelay: `${60 + i * 40}ms` }}
            >
              <span className="nav__mobile-index">0{i + 1}</span>
              {link.label}
            </a>
          ))}
        </nav>
        <a className="btn btn--gold nav__mobile-cta" href={navigation.cta.href} onClick={close}>
          {navigation.cta.label}
        </a>
        <p className="nav__mobile-contact">{site.brand.email}</p>
      </div>
    </header>
  );
}