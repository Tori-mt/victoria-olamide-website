"""Victoria Olamide monogram: a V set inside an O.

The V's arms break out through the top of the ring (growth beyond the frame),
and its base lands on a gold point, echoing Opptiq's ring-and-point mark.
"""


def monogram(size=64, ring="#1a1409", v="#1a1409", point="#f0a020", bg="#fbf7ef", fill_bg=False, uid="vo"):
    back = f'<circle cx="32" cy="32" r="31" fill="{bg}"/>' if fill_bg else ""
    vpath = "M16.5 7.5 L32 46 L47.5 7.5"
    return (
        f'<svg class="logo" width="{size}" height="{size}" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Victoria Olamide monogram">'
        f'<defs><linearGradient id="g-{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6c86a"/><stop offset="1" stop-color="#d9781a"/></linearGradient></defs>'
        f'{back}'
        f'<circle cx="32" cy="33" r="18.5" fill="none" stroke="{ring}" stroke-width="2.6"/>'
        # knockout so the V reads as passing in front of the ring
        f'<path d="{vpath}" fill="none" stroke="{bg}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<path d="M16.5 7.5 L32 46" fill="none" stroke="{v}" stroke-width="3.6" stroke-linecap="round"/>'
        f'<path d="M32 46 L47.5 7.5" fill="none" stroke="url(#g-{uid})" stroke-width="3.6" stroke-linecap="round"/>'
        f'<circle cx="32" cy="51.5" r="3.6" fill="{point}" stroke="{bg}" stroke-width="2"/>'
        f'</svg>'
    )


if __name__ == "__main__":
    from pathlib import Path
    out = Path(__file__).resolve().parent.parent / "public"
    (out / "portfolio" / "img" / "logo.svg").write_text(monogram(256), encoding="utf-8")
    fav = monogram(64, ring="#fbf7ef", v="#fbf7ef", bg="#1a1409", fill_bg=True, uid="fav")
    (out / "favicon.svg").write_text(fav, encoding="utf-8")
    print("logo written")
