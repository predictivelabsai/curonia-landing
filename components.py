"""Shared layout, brand marks and presentation for the Curonia Capital site."""

import hashlib
import json
import os
import re
from datetime import datetime
from pathlib import Path

from fasthtml.common import (
    A, Body, Details, Div, Em, Footer, H1, H2, H3, Head, Header, Html, Li, Link,
    Main, Meta, Nav, NotStr, P, Script, Section, Span, Summary, Title, Ul,
)

from utils.i18n import DEFAULT_LANG, LANGUAGES, t

SITE_NAME = "Curonia Capital"
LEGAL_NAME = "Curonia Capital Ltd"
COMPANY_NUMBER = "14537690"
REGISTERED_ADDRESS = "155 Minories Street, Suite 275, London, London, United Kingdom, EC3N 1AD"
CONTACT_EMAIL = "info@curoniacapital.com"
PLATFORM_URL = "https://liquidround.com/"
SITE_URL = os.environ.get("CURONIA_SITE_URL", "https://curoniacapital.com").rstrip("/")

STATIC_DIR = Path(__file__).resolve().parent / "static"

# Page key -> URL slug. English lives at the root, other languages under /{code}/.
PAGES = {
    "home": "",
    "advisory": "advisory",
    "intelligence": "intelligence",
    "sectors": "sectors",
    "team": "team",
    "contact": "contact",
}
NAV_PAGES = ("advisory", "intelligence", "sectors", "team", "contact")


def url_for(lang, page="home"):
    slug = PAGES[page]
    prefix = "" if lang == DEFAULT_LANG else f"/{lang}"
    return f"{prefix}/{slug}" if slug else f"{prefix}/"


def absolute(path):
    return f"{SITE_URL}{path}"


_VERSIONS = {}


def asset(name):
    """Static URL with a content hash so files can be cached as immutable."""
    path = STATIC_DIR / name
    try:
        mtime = path.stat().st_mtime_ns
    except OSError:
        return f"/static/{name}"
    cached = _VERSIONS.get(name)
    if not cached or cached[0] != mtime:
        cached = (mtime, hashlib.sha256(path.read_bytes()).hexdigest()[:10])
        _VERSIONS[name] = cached
    return f"/static/{name}?v={cached[1]}"


def rich(text):
    """Render *emphasis* markers from the copy catalogue as <em>."""
    parts = re.split(r"\*(.+?)\*", text)
    return [Em(part) if i % 2 else part for i, part in enumerate(parts) if part]


# Brand marks ---------------------------------------------------------------

MARK_SVG = (
    '<svg class="mark" viewBox="0 0 36 34" aria-hidden="true" focusable="false">'
    '<path d="M26.2 7.6A12.4 12.4 0 1 0 26.2 26.4" fill="none" stroke="currentColor" '
    'stroke-width="1.7" stroke-linecap="round"/>'
    '<path d="M2.5 17h31" fill="none" stroke="var(--amber)" stroke-width="1.3" stroke-linecap="round"/>'
    "</svg>"
)


def Lockup(cls=""):
    return Span(
        NotStr(MARK_SVG),
        Span(Span("Curonia", cls="word"), Span("Capital", cls="sub"), cls="wordmark"),
        cls=f"lockup {cls}".strip(),
    )


# Small building blocks -----------------------------------------------------

def Eyebrow(index, label, *, cls=""):
    return P(Span(index, cls="idx") if index else None, Span(label), cls=f"eyebrow {cls}".strip())


def Heading(level, text, *, cls=""):
    tag = {1: H1, 2: H2, 3: H3}[level]
    return tag(*rich(text), cls=cls or None)


def TextLink(label, href, *, external=False, cls=""):
    attrs = {"target": "_blank", "rel": "noopener noreferrer"} if external else {}
    return A(Span(label), Span("↗" if external else "→", cls="arrow", aria_hidden="true"),
             href=href, cls=f"text-link {cls}".strip(), **attrs)


def Button(label, href, *, variant="solid"):
    return A(Span(label), Span("→", cls="arrow", aria_hidden="true"), href=href, cls=f"button button--{variant}")


def Section_(*children, cls="", inner="wrap", **kw):
    return Section(Div(*children, cls=inner), cls=f"section {cls}".strip(), **kw)


def SectionHead(index, label, heading, lede=None, *, cls=""):
    return Div(
        Eyebrow(index, label),
        Heading(2, heading, cls="display-2"),
        P(lede, cls="lede") if lede else None,
        cls=f"section-head {cls}".strip(),
    )


# Header and footer ---------------------------------------------------------

def LanguageLinks(lang, page, *, cls="lang-switch"):
    return Ul(
        *[Li(A(code.upper(), href=url_for(code, page or "home"), hreflang=code, lang=code,
               title=info["native"], aria_current="true" if code == lang else None,
               cls="is-active" if code == lang else None))
          for code, info in LANGUAGES.items()],
        cls=cls, aria_label=t("language", lang),
    )


def SiteHeader(lang, page):
    links = [
        Li(A(t(f"nav_{key}", lang), href=url_for(lang, key),
             aria_current="page" if key == page else None))
        for key in NAV_PAGES
    ]
    return Header(
        Div(
            A(Lockup(), href=url_for(lang), cls="brand", aria_label=f"{SITE_NAME}, home"),
            Nav(Ul(*links), cls="primary-nav", aria_label="Primary"),
            Div(
                LanguageLinks(lang, page),
                A(t("header_cta", lang), href=url_for(lang, "contact"), cls="header-cta"),
                cls="header-tools",
            ),
            Details(
                Summary(Span(t("menu", lang)), Span(cls="burger", aria_hidden="true")),
                Div(
                    Nav(Ul(*[Li(A(t(f"nav_{key}", lang), href=url_for(lang, key),
                                   aria_current="page" if key == page else None))
                             for key in NAV_PAGES]), aria_label="Mobile"),
                    LanguageLinks(lang, page, cls="lang-switch lang-switch--mobile"),
                    cls="mobile-panel",
                ),
                cls="mobile-menu",
            ),
            cls="wrap header-inner",
        ),
        cls="site-header", data_header="",
    )


def SiteFooter(lang):
    year = datetime.now().year
    return Footer(
        Div(
            Div(
                Div(
                    A(Lockup("lockup--reverse"), href=url_for(lang), aria_label=f"{SITE_NAME}, home"),
                    P(t("footer_tagline", lang), cls="footer-tagline"),
                    cls="footer-brand",
                ),
                Nav(
                    P(t("footer_explore", lang), cls="footer-label"),
                    Ul(*[Li(A(t(f"nav_{key}", lang), href=url_for(lang, key))) for key in NAV_PAGES]),
                    aria_label=t("footer_explore", lang), cls="footer-col",
                ),
                Div(
                    P(t("footer_company", lang), cls="footer-label"),
                    P(LEGAL_NAME),
                    P(f"{t('company_number', lang)} {COMPANY_NUMBER}"),
                    P(REGISTERED_ADDRESS, cls="footer-address"),
                    cls="footer-col",
                ),
                Div(
                    P(t("footer_contact", lang), cls="footer-label"),
                    A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", cls="footer-email"),
                    LanguageLinks(lang, "home", cls="lang-switch lang-switch--footer"),
                    cls="footer-col",
                ),
                cls="footer-grid",
            ),
            Div(
                P(t("footer_registered", lang)),
                P(f"© {year} {LEGAL_NAME}. {t('footer_rights', lang)}"),
                cls="footer-legal",
            ),
            cls="wrap",
        ),
        cls="site-footer",
    )


# Document ------------------------------------------------------------------

def structured_data(lang, page_url):
    from content.team import TEAM

    org = {
        "@type": "ProfessionalService",
        "@id": f"{SITE_URL}/#organization",
        "name": SITE_NAME,
        "legalName": LEGAL_NAME,
        "url": f"{SITE_URL}/",
        "logo": absolute("/static/brand/curonia-mark.svg"),
        "image": absolute("/static/og-image.png"),
        "email": CONTACT_EMAIL,
        "description": t("desc_home", lang),
        "identifier": {"@type": "PropertyValue", "propertyID": "Companies House", "value": COMPANY_NUMBER},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "155 Minories Street, Suite 275",
            "addressLocality": "London",
            "postalCode": "EC3N 1AD",
            "addressCountry": "GB",
        },
        "areaServed": ["Lithuania", "Latvia", "Estonia", "Poland", "Central and Eastern Europe"],
        "knowsAbout": ["Mergers and acquisitions", "Sell-side advisory", "Buy-side advisory", "Corporate finance"],
        "employee": [
            {"@type": "Person", "name": m["name"], "sameAs": [m["linkedin"]]} for m in TEAM
        ],
    }
    page = {
        "@type": "WebPage",
        "@id": f"{page_url}#webpage",
        "url": page_url,
        "inLanguage": LANGUAGES[lang]["hreflang"],
        "isPartOf": {"@type": "WebSite", "@id": f"{SITE_URL}/#website", "name": SITE_NAME, "url": f"{SITE_URL}/"},
        "about": {"@id": f"{SITE_URL}/#organization"},
    }
    data = json.dumps({"@context": "https://schema.org", "@graph": [org, page]}, ensure_ascii=False)
    return data.replace("</", "<\\/")


FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Geist:wght@400;500&family=Geist+Mono:wght@400&"
    "family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&display=swap"
)


def page(lang, page_key, *content, title=None, description=None, index=True, alternates=True):
    path = url_for(lang, page_key) if page_key else None
    full_title = f"{title} | {SITE_NAME}" if title else SITE_NAME
    description = description or t("desc_home", lang)
    canonical = absolute(path) if path else None
    og_image = absolute(asset("og-image.png"))

    head = [
        Meta(charset="utf-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1"),
        Title(full_title),
        Meta(name="description", content=description),
        Meta(name="theme-color", content="#F6F3EC"),
        Meta(name="robots", content="index, follow" if index else "noindex"),
        Script(NotStr("document.documentElement.classList.add('js')")),
    ]
    if canonical:
        head.append(Link(rel="canonical", href=canonical))
    if path and alternates:
        head += [Link(rel="alternate", hreflang=info["hreflang"], href=absolute(url_for(code, page_key)))
                 for code, info in LANGUAGES.items()]
        head.append(Link(rel="alternate", hreflang="x-default", href=absolute(url_for(DEFAULT_LANG, page_key))))
    head += [
        Meta(property="og:type", content="website"),
        Meta(property="og:site_name", content=SITE_NAME),
        Meta(property="og:title", content=full_title),
        Meta(property="og:description", content=description),
        Meta(property="og:url", content=canonical) if canonical else None,
        Meta(property="og:locale", content=LANGUAGES[lang]["locale"]),
        Meta(property="og:image", content=og_image),
        Meta(property="og:image:width", content="1200"),
        Meta(property="og:image:height", content="630"),
        Meta(name="twitter:card", content="summary_large_image"),
        Meta(name="twitter:title", content=full_title),
        Meta(name="twitter:description", content=description),
        Meta(name="twitter:image", content=og_image),
        Link(rel="icon", href=asset("favicon.svg"), type="image/svg+xml"),
        Link(rel="apple-touch-icon", href=asset("apple-touch-icon.png")),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(rel="stylesheet", href=FONTS_URL),
        Link(rel="stylesheet", href=asset("site.css")),
        Script(src=asset("site.js"), type="module"),
        Script(NotStr(structured_data(lang, canonical or f"{SITE_URL}/")), type="application/ld+json"),
    ]
    return Html(
        Head(*[h for h in head if h is not None]),
        Body(
            A(t("skip", lang), href="#main", cls="skip-link"),
            SiteHeader(lang, page_key),
            Main(*content, id="main", tabindex="-1"),
            SiteFooter(lang),
        ),
        lang=LANGUAGES[lang]["hreflang"],
    )


# Decorative visuals --------------------------------------------------------

HERO_ART = """
<svg class="hero-art" viewBox="0 0 520 560" aria-hidden="true" focusable="false">
  <g class="contours" fill="none" stroke="var(--amber)" stroke-width=".8">
    <path d="M18 552C84 470 136 380 178 296S272 104 404 8"/>
    <path d="M44 556C110 476 162 388 206 304S300 116 430 22" opacity=".85"/>
    <path d="M70 560C136 482 190 396 234 312S328 128 456 38" opacity=".7"/>
    <path d="M96 564C162 490 218 404 262 320S356 142 482 56" opacity=".5"/>
    <path d="M122 568C188 498 246 414 290 330S384 158 508 76" opacity=".35"/>
  </g>
  <g class="links" fill="none" stroke="var(--ink)" stroke-width=".8">
    <path pathLength="1" d="M96 156Q232 70 352 128"/>
    <path pathLength="1" d="M96 156Q206 250 326 268"/>
    <path pathLength="1" d="M352 128Q356 200 326 268"/>
    <path pathLength="1" d="M326 268Q326 344 304 402"/>
    <path pathLength="1" d="M96 156Q176 320 304 402"/>
    <path pathLength="1" d="M304 402Q262 452 228 486"/>
  </g>
  <g class="nodes">
    <g class="node node--home"><circle cx="96" cy="156" r="4"/><text x="70" y="140">LONDON</text></g>
    <g class="node"><circle class="pulse" cx="352" cy="128" r="4"/><circle cx="352" cy="128" r="4"/><text x="366" y="132">TALLINN</text></g>
    <g class="node"><circle class="pulse" cx="326" cy="268" r="4"/><circle cx="326" cy="268" r="4"/><text x="340" y="272">RIGA</text></g>
    <g class="node"><circle class="pulse" cx="304" cy="402" r="4"/><circle cx="304" cy="402" r="4"/><text x="318" y="406">VILNIUS</text></g>
    <g class="node node--home"><circle cx="228" cy="486" r="3.4"/><text x="242" y="490">WARSAW</text></g>
  </g>
</svg>
"""


NIGHT_ART = """
<svg class="night-art" viewBox="0 0 1400 640" preserveAspectRatio="xMaxYMin slice" aria-hidden="true" focusable="false">
  <defs>
    <radialGradient id="night-glow" cx="70%" cy="45%" r="60%">
      <stop offset="0" stop-color="#16324A" stop-opacity=".95"/>
      <stop offset="1" stop-color="#07121B" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="night-fade" cx="70%" cy="47%" r="48%">
      <stop offset="0" stop-color="#fff"/>
      <stop offset=".55" stop-color="#fff" stop-opacity=".6"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </radialGradient>
    <pattern id="night-dots" width="30" height="30" patternUnits="userSpaceOnUse">
      <circle cx="15" cy="15" r="1.1" fill="#ECE6DA"/>
    </pattern>
    <mask id="night-mask"><rect width="1400" height="640" fill="url(#night-fade)"/></mask>
  </defs>
  <rect width="1400" height="640" fill="url(#night-glow)"/>
  <rect width="1400" height="640" fill="url(#night-dots)" mask="url(#night-mask)" opacity=".2"/>
  <g fill="none" stroke="#C9A36A" stroke-width=".8" opacity=".3">
    <path d="M620 520Q860 300 1040 330T1380 190"/>
    <path d="M700 150Q930 250 1120 200T1360 470"/>
    <path d="M1040 330L1120 200"/>
  </g>
  <g fill="#C9A36A">
    <circle cx="620" cy="520" r="3"/><circle cx="1040" cy="330" r="3.5"/><circle cx="1120" cy="200" r="3"/>
    <circle cx="700" cy="150" r="2.5"/><circle cx="1360" cy="470" r="2.5"/>
  </g>
</svg>
"""

# Page motifs ---------------------------------------------------------------
# Abstract fine-line drawings for the empty side of page intros. Decorative only.

def _svg(body, view="0 0 480 420", cls="intro-art"):
    return (f'<svg class="{cls}" viewBox="{view}" aria-hidden="true" focusable="false">'
            f"{body}</svg>")


def _label(x, y, text, anchor="start"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}">{text}</text>'


def _intelligence_art():
    # A wide universe of candidates narrows through three screens to one shortlist.
    dots, lines = [], []
    rows = [(r, 46 + r * 26) for r in range(13)]
    target = (404, 210)
    for r, y in rows:
        for c in range(3):
            x = 40 + c * 26 + (r % 2) * 13
            keep = (r * 3 + c) % 4 == 0
            dots.append(f'<circle cx="{x}" cy="{y}" r="{2.4 if keep else 1.6}" class="{"dot-on" if keep else "dot-off"}"/>')
            if keep:
                lines.append(f'<path pathLength="1" d="M{x} {y}C{x + 140} {y},{target[0] - 170} {target[1]},{target[0]} {target[1]}"/>')
    screens = "".join(
        f'<line x1="{x}" y1="{60 + i * 34}" x2="{x}" y2="{360 - i * 34}" class="screen"/>'
        for i, x in enumerate((170, 250, 330))
    )
    labels = (_label(40, 26, "UNIVERSE") + _label(170, 48, "SCREEN", "middle")
              + _label(250, 82, "ANALYSE", "middle") + _label(330, 116, "REVIEW", "middle")
              + _label(404, 252, "SHORTLIST", "middle"))
    node = (f'<circle class="pulse" cx="{target[0]}" cy="{target[1]}" r="6"/>'
            f'<circle cx="{target[0]}" cy="{target[1]}" r="6" class="node-amber"/>'
            f'<circle cx="{target[0]}" cy="{target[1]}" r="16" class="ring"/>')
    return _svg(f'<g class="flow">{"".join(lines)}</g>{screens}<g>{"".join(dots)}</g>{node}{labels}')


def _advisory_art():
    # Two sides of a transaction meet in one considered outcome.
    ticks = "".join(
        f'<line x1="240" y1="22" x2="240" y2="{30 if i % 3 else 36}" transform="rotate({i * 10} 240 210)" class="tick"/>'
        for i in range(36)
    )
    return _svg(
        '<circle cx="240" cy="210" r="188" class="orbit"/>' + ticks
        + '<circle cx="180" cy="210" r="118" class="line"/>'
        + '<circle cx="300" cy="210" r="118" class="line"/>'
        + '<path d="M240 108.4A118 118 0 0 1 240 311.6A118 118 0 0 1 240 108.4Z" class="lens"/>'
        + '<line x1="20" y1="210" x2="460" y2="210" class="horizon"/>'
        + '<circle class="pulse" cx="240" cy="210" r="5"/><circle cx="240" cy="210" r="5" class="node-amber"/>'
        + _label(120, 214, "SELL-SIDE", "middle") + _label(360, 214, "BUY-SIDE", "middle")
        + _label(240, 404, "MANDATE", "middle")
    )


def _sectors_art():
    # Six sectors around one mandate.
    import math
    parts = ['<circle cx="240" cy="210" r="170" class="orbit dashed"/>',
             '<circle cx="240" cy="210" r="104" class="line"/>',
             '<circle cx="240" cy="210" r="46" class="line"/>']
    for i in range(6):
        a = math.radians(-90 + i * 60)
        x, y = 240 + 170 * math.cos(a), 210 + 170 * math.sin(a)
        mx, my = 240 + 104 * math.cos(a), 210 + 104 * math.sin(a)
        lx, ly = 240 + 196 * math.cos(a), 210 + 196 * math.sin(a) + 3
        parts.append(f'<line pathLength="1" x1="240" y1="210" x2="{x:.1f}" y2="{y:.1f}" class="spoke"/>')
        parts.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="2.2" class="node-ink"/>')
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" class="node-amber"/>')
        parts.append(_label(f"{lx:.1f}", f"{ly:.1f}", f"0{i + 1}", "middle"))
    parts.append('<circle class="pulse" cx="240" cy="210" r="5"/><circle cx="240" cy="210" r="5" class="node-ink"/>')
    return _svg("".join(parts), view="0 0 480 420")


def _team_art():
    # A small group on the contour lines of the spit.
    contours = "".join(
        f'<path d="M{-20 + i * 26} 420C{80 + i * 26} 330 {150 + i * 26} 240 {210 + i * 26} 160S{330 + i * 26} 40 {470 + i * 20} 0" '
        f'class="contour" opacity="{1 - i * 0.16:.2f}"/>'
        for i in range(5)
    )
    people = [(150, 300), (214, 214), (268, 150), (330, 96), (226, 330)]
    links = "".join(
        f'<line pathLength="1" x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" class="link"/>'
        for a, b in [(people[0], people[1]), (people[1], people[2]), (people[2], people[3]),
                     (people[0], people[4]), (people[4], people[1])]
    )
    nodes = "".join(
        f'<circle cx="{x}" cy="{y}" r="15" class="seat"/><circle cx="{x}" cy="{y}" r="4" class="node-amber"/>'
        for x, y in people
    )
    return _svg(contours + links + nodes)


def _contact_art():
    # The London office as a quiet beacon.
    rings = "".join(f'<circle cx="240" cy="210" r="{r}" class="line" opacity="{1 - i * 0.17:.2f}"/>'
                    for i, r in enumerate((34, 72, 114, 158, 200)))
    return _svg(
        rings
        + '<line x1="240" y1="0" x2="240" y2="420" class="cross"/><line x1="20" y1="210" x2="460" y2="210" class="cross"/>'
        + '<circle class="pulse" cx="240" cy="210" r="6"/><circle cx="240" cy="210" r="6" class="node-amber"/>'
        + _label(258, 194, "LONDON · EC3N 1AD") + _label(258, 236, "51.511° N  0.074° W")
    )


def _cta_art():
    # Ripples from a first conversation, crossed by the horizon line.
    ripples = "".join(
        f'<ellipse cx="240" cy="160" rx="{36 + i * 40}" ry="{16 + i * 22}" class="line" opacity="{1 - i * 0.13:.2f}"/>'
        for i in range(6)
    )
    return _svg(
        ripples + '<line x1="0" y1="160" x2="480" y2="160" class="horizon"/>'
        + '<circle class="pulse" cx="240" cy="160" r="5"/><circle cx="240" cy="160" r="5" class="node-amber"/>',
        view="0 0 480 320", cls="intro-art cta-art",
    )


INTRO_ART = {
    "intelligence": _intelligence_art(),
    "advisory": _advisory_art(),
    "sectors": _sectors_art(),
    "team": _team_art(),
    "contact": _contact_art(),
}
CTA_ART = _cta_art()
