"""Curonia Capital Ltd: Baltic and CEE M&A advisory site."""

import os
import secrets
from pathlib import Path
from urllib.parse import quote, urlsplit

from fasthtml.common import (
    A, Article, Details, Div, H3, HTMLResponse, Img, Li, NotStr, Ol, P,
    RedirectResponse, Response, Span, Summary, Ul, fast_app, serve, to_xml,
)
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.staticfiles import StaticFiles

from components import (
    COMPANY_NUMBER, CONTACT_EMAIL, CTA_ART, HERO_ART, INTRO_ART, LEGAL_NAME, NIGHT_ART, PAGES,
    PLATFORM_URL, REGISTERED_ADDRESS, SITE_URL, Button, Eyebrow, Heading,
    SectionHead, Section_, TextLink, absolute, page, rich, url_for,
)
from content.team import TEAM
from utils.i18n import DEFAULT_LANG, LANGUAGES, t

BASE_DIR = Path(__file__).resolve().parent


class HeadersMiddleware:
    """Long-lived caching for versioned static files and baseline security headers."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        is_static = scope["path"].startswith("/static/")

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                headers = list(message.get("headers", []))
                headers += [
                    (b"x-content-type-options", b"nosniff"),
                    (b"referrer-policy", b"strict-origin-when-cross-origin"),
                    (b"x-frame-options", b"DENY"),
                ]
                if is_static and message["status"] == 200:
                    headers.append((b"cache-control", b"public, max-age=31536000, immutable"))
                message["headers"] = headers
            await send(message)

        await self.app(scope, receive, send_wrapper)


def not_found(req, exc):
    segment = req.url.path.strip("/").split("/", 1)[0]
    lang = segment if segment in LANGUAGES else DEFAULT_LANG
    body = page(
        lang, None,
        Section_(
            Eyebrow("404", t("title_404", lang)),
            Heading(1, t("nf_heading", lang), cls="display-1"),
            P(t("nf_body", lang), cls="lede"),
            Div(Button(t("nf_link", lang), url_for(lang)), cls="actions"),
            cls="page-intro page-intro--solo",
        ),
        title=t("title_404", lang), index=False,
    )
    return HTMLResponse(to_xml(body), status_code=404)


# Session cookies are not used; a random key keeps FastHTML from writing a key file.
app, rt = fast_app(
    live=False,
    pico=False,
    default_hdrs=False,
    secret_key=os.environ.get("CURONIA_SESSION_SECRET") or secrets.token_urlsafe(32),
    middleware=[Middleware(GZipMiddleware, minimum_size=500), Middleware(HeadersMiddleware)],
    exception_handlers={404: not_found},
)

# Serve only the static folder, never arbitrary repository files.
app.router.routes[:] = [r for r in app.router.routes if "{ext:static}" not in getattr(r, "path", "")]
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


# Page sections -------------------------------------------------------------

def page_intro(lang, index, label, heading, lede, *, art=None):
    return Section_(
        Div(
            Eyebrow(index, label),
            Heading(1, heading, cls="display-1"),
            P(lede, cls="lede lede--lg"),
            cls="intro-copy",
        ),
        Div(NotStr(INTRO_ART[art]), cls="intro-visual") if art else None,
        cls="page-intro", inner="wrap intro-inner",
    )


def service_rows(lang, *, detailed=False):
    rows = []
    for i, key in enumerate(("sell", "buy", "strategy"), start=1):
        numeral = ("I", "II", "III")[i - 1]
        points = Ul(*[Li(t(f"{key}_p{n}", lang)) for n in range(1, 4)], cls="ticks") if detailed else None
        rows.append(Article(
            Span(numeral, cls="row-index"),
            H3(t(f"{key}_title", lang), cls="row-title"),
            Div(P(t(f"{key}_body", lang)), points, cls="row-body"),
            None if detailed else Span("→", cls="row-arrow", aria_hidden="true"),
            cls="service-row" + (" service-row--detailed" if detailed else ""),
            data_reveal="",
        ))
    if not detailed:
        rows = [A(row, href=url_for(lang, "advisory"), cls="service-link") for row in rows]
    return Div(*rows, cls="service-list")


def capability_grid(lang, prefix, count, *, kicker=True):
    return Ol(*[
        Li(
            Span(t(f"{prefix}_{i}_kicker", lang) if kicker else f"0{i}", cls="cap-kicker"),
            H3(t(f"{prefix}_{i}_title", lang)),
            P(t(f"{prefix}_{i}_body", lang)),
            data_reveal="",
        )
        for i in range(1, count + 1)
    ], cls="cap-grid")


def intelligence_band(lang, *, with_link=True):
    return Section_(
        Div(
            Eyebrow("02", t("intel_label", lang)),
            Heading(2, t("intel_heading", lang), cls="display-2"),
            P(t("intel_lede", lang), cls="lede"),
            cls="section-head",
        ),
        capability_grid(lang, "cap", 4),
        Div(
            P(t("principle_label", lang), cls="principle-label"),
            P(t("intel_principle", lang), cls="principle-quote"),
            TextLink(t("intel_link", lang), url_for(lang, "intelligence")) if with_link else None,
            cls="principle-row",
        ),
        cls="section--night",
        inner="wrap night-inner",
    )


def night(section):
    """Prepend the decorative night field to a dark section."""
    section.children = (NotStr(NIGHT_ART),) + tuple(section.children)
    return section


def cta_band(lang):
    return Section_(
        Div(
            Div(
                Eyebrow(None, t("cta_label", lang), cls="eyebrow--rule"),
                Heading(2, t("cta_heading", lang), cls="display-2"),
                P(t("cta_body", lang), cls="lede"),
                Div(Button(t("cta_button", lang), url_for(lang, "contact")),
                    Div(Span(t("cta_direct", lang), cls="cta-direct-label"),
                        A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", cls="cta-email"),
                        cls="cta-direct"),
                    cls="actions"),
                cls="cta-copy",
            ),
            Div(NotStr(CTA_ART), cls="cta-visual"),
            cls="cta-panel",
        ),
        cls="cta-band",
    )


# Pages ---------------------------------------------------------------------

def home(lang):
    markets = Ul(*[
        Li(Span(f"0{i}", cls="idx"), Span(t(f"market_{code}", lang)))
        for i, code in enumerate(("lt", "lv", "ee", "pl", "cee"), start=1)
    ], cls="market-list")
    principles = Ol(*[
        Li(H3(t(f"principle_{i}_title", lang)), P(t(f"principle_{i}_body", lang)), data_reveal="")
        for i in range(1, 5)
    ], cls="principles")
    return page(
        lang, "home",
        Section_(
            Div(
                Eyebrow(None, t("hero_eyebrow", lang), cls="eyebrow--rule"),
                Heading(1, t("hero_heading", lang), cls="display-hero"),
                P(t("hero_lede", lang), cls="lede lede--lg"),
                Div(Button(t("hero_primary", lang), url_for(lang, "contact")),
                    TextLink(t("hero_secondary", lang), url_for(lang, "intelligence")),
                    cls="actions"),
                cls="hero-copy",
            ),
            Div(NotStr(HERO_ART), cls="hero-visual"),
            cls="hero", inner="wrap hero-inner",
        ),
        Section_(
            Div(
                Eyebrow("01", t("approach_label", lang)),
                P(*rich(t("approach_statement", lang)), cls="statement"),
                cls="statement-grid",
            ),
            principles,
            cls="section--rule",
        ),
        Section_(
            SectionHead(None, t("services_label", lang), t("services_heading", lang)),
            service_rows(lang),
            cls="section--tight-top",
        ),
        night(intelligence_band(lang)),
        Section_(
            Div(
                Div(
                    Eyebrow("03", t("region_label", lang)),
                    Heading(2, t("region_heading", lang), cls="display-2"),
                    P(t("region_body", lang), cls="lede"),
                    P(Span(cls="dot", aria_hidden="true"), t("region_base", lang), cls="base-note"),
                ),
                markets,
                cls="split",
            ),
        ),
        Section_(
            Div(
                Div(
                    Eyebrow("04", t("team_label", lang)),
                    Heading(2, t("team_teaser_heading", lang), cls="display-2"),
                    P(t("team_teaser_body", lang), cls="lede"),
                    Div(TextLink(t("team_link", lang), url_for(lang, "team")), cls="actions"),
                ),
                Ul(*[Li(Span(m["initials"], cls="monogram"), Span(m["name"], cls="name"))
                     for m in TEAM], cls="team-mini"),
                cls="split split--center",
            ),
            cls="section--rule",
        ),
        cta_band(lang),
        title=t("title_home", lang), description=t("desc_home", lang),
    )


def advisory(lang):
    return page(
        lang, "advisory",
        page_intro(lang, "01", t("nav_advisory", lang), t("advisory_heading", lang), t("advisory_lede", lang), art="advisory"),
        Section_(service_rows(lang, detailed=True), cls="section--tight-top"),
        Section_(
            SectionHead("02", t("clients_label", lang), t("clients_heading", lang)),
            Ol(*[Li(H3(t(f"client_{i}_title", lang)), P(t(f"client_{i}_body", lang)), data_reveal="")
                 for i in range(1, 4)], cls="principles principles--three"),
            cls="section--paper",
        ),
        night(Section_(
            SectionHead("03", t("process_label", lang), t("advisory_process", lang)),
            Ol(*[Li(Span(f"0{i}", cls="step-num"), H3(t(f"process_{i}_title", lang)),
                    P(t(f"process_{i}_body", lang)), data_reveal="")
                 for i in range(1, 5)], cls="timeline"),
            cls="section--night", inner="wrap night-inner",
        )),
        cta_band(lang),
        title=t("title_advisory", lang), description=t("desc_advisory", lang),
    )


def intelligence(lang):
    return page(
        lang, "intelligence",
        page_intro(lang, "01", t("nav_intelligence", lang), t("platform_heading", lang), t("platform_lede", lang), art="intelligence"),
        Section_(
            SectionHead("02", t("lifecycle_label", lang), t("lifecycle_heading", lang)),
            capability_grid(lang, "platform", 4, kicker=False),
            cls="section--tight-top",
        ),
        night(Section_(
            SectionHead("03", t("gov_label", lang), t("gov_heading", lang)),
            Ol(*[Li(H3(t(f"gov_{i}_title", lang)), P(t(f"gov_{i}_body", lang)), data_reveal="")
                 for i in range(1, 4)], cls="principles principles--three principles--night"),
            cls="section--night", inner="wrap night-inner",
        )),
        Section_(
            Div(
                Div(Eyebrow(None, t("built_on", lang)),
                    P(t("platform_note", lang), cls="statement statement--sm")),
                Div(TextLink(t("platform_link", lang), PLATFORM_URL, external=True), cls="actions"),
                cls="split split--center",
            ),
        ),
        cta_band(lang),
        title=t("title_intelligence", lang), description=t("desc_intelligence", lang),
    )


def sectors(lang):
    return page(
        lang, "sectors",
        page_intro(lang, "01", t("nav_sectors", lang), t("sectors_heading", lang), t("sectors_lede", lang), art="sectors"),
        Section_(
            Ol(*[Li(Span(f"0{i}", cls="cap-kicker"), H3(t(f"sector_{i}_title", lang)),
                    P(t(f"sector_{i}_body", lang)), data_reveal="")
                 for i in range(1, 7)], cls="sector-grid"),
            P(t("sectors_note", lang), cls="note"),
            cls="section--tight-top",
        ),
        cta_band(lang),
        title=t("title_sectors", lang), description=t("desc_sectors", lang),
    )


def portrait(member):
    if member.get("photo"):
        return Img(src=f"/static/team/{member['photo']}", alt=member["name"], width="800", height="910",
                   loading="lazy", decoding="async", cls="portrait")
    return Div(Span(member["initials"]), cls="portrait portrait--placeholder", aria_hidden="true")


def person_card(member, lang):
    phone = member.get("phone")
    return Li(
        Div(portrait(member), cls="portrait-frame"),
        H3(member["name"], cls="person-name"),
        P(t(member["role_key"], lang), cls="person-role") if member.get("role_key") else None,
        A(member["email"], href=f"mailto:{member['email']}", cls="person-email") if member.get("email") else None,
        A(phone, href=f"tel:{phone.replace(' ', '')}", cls="person-phone") if phone else None,
        A("LinkedIn", Span("↗", aria_hidden="true"), href=member["linkedin"], target="_blank",
          rel="noopener noreferrer", cls="person-link",
          aria_label=f"{member['name']}, {t('linkedin_label', lang)}") if member.get("linkedin") else None,
        Details(Summary(t("profile", lang)), P(t(member["bio_key"], lang)), cls="person-bio")
        if member.get("bio_key") else None,
        cls="person-card", data_reveal="",
    )


def team(lang):
    return page(
        lang, "team",
        page_intro(lang, "01", t("nav_team", lang), t("team_heading", lang), t("team_lede", lang), art="team"),
        Section_(Ul(*[person_card(m, lang) for m in TEAM], cls="team-grid"), cls="section--tight-top"),
        cta_band(lang),
        title=t("title_team", lang), description=t("desc_team", lang),
    )


def contact(lang):
    subject = quote(t("contact_subject", lang))
    return page(
        lang, "contact",
        page_intro(lang, "01", t("nav_contact", lang), t("contact_heading", lang), t("contact_lede", lang), art="contact"),
        Section_(
            Div(
                Div(
                    Eyebrow(None, t("contact_email", lang)),
                    A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}?subject={subject}", cls="email-link"),
                    P(t("include_label", lang), cls="sub-label"),
                    Ol(*[Li(t(f"include_{i}", lang)) for i in range(1, 4)], cls="include-list"),
                    cls="contact-main",
                ),
                Div(
                    Div(
                        Span(cls="dot", aria_hidden="true"),
                        P(t("discretion_note", lang)),
                        cls="discretion",
                    ),
                    Div(
                        Eyebrow(None, t("contact_office", lang)),
                        P(LEGAL_NAME, cls="office-name"),
                        P(f"{t('company_number', lang)} {COMPANY_NUMBER}"),
                        P(REGISTERED_ADDRESS),
                        cls="office",
                    ),
                    cls="contact-side",
                ),
                cls="contact-grid",
            ),
            cls="section--tight-top",
        ),
        title=t("title_contact", lang), description=t("desc_contact", lang),
    )


RENDERERS = {
    "home": home,
    "advisory": advisory,
    "intelligence": intelligence,
    "sectors": sectors,
    "team": team,
    "contact": contact,
}


def _register(lang, key):
    def handler():
        return RENDERERS[key](lang)

    handler.__name__ = f"{key}_{lang}"
    app.route(url_for(lang, key), methods=["get"])(handler)


for _lang in LANGUAGES:
    for _key in PAGES:
        _register(_lang, _key)


# Redirects and utility routes ----------------------------------------------

def _split_lang(path):
    parts = [p for p in path.split("/") if p]
    if parts and parts[0] in LANGUAGES:
        return parts[0], parts[1:]
    return DEFAULT_LANG, parts


def _page_from_path(path):
    _, rest = _split_lang(path)
    slug = rest[0] if rest else ""
    if slug == "platform":
        return "intelligence"
    for key, value in PAGES.items():
        if value == slug:
            return key
    return "home"


@rt("/set-lang/{code}")
def set_language(code: str, req):
    code = code.lower() if code.lower() in LANGUAGES else DEFAULT_LANG
    referer = urlsplit(req.headers.get("referer", ""))
    same_site = not referer.netloc or referer.netloc == req.url.netloc
    key = _page_from_path(referer.path) if same_site and referer.path else "home"
    return RedirectResponse(url_for(code, key), status_code=303)


@rt("/platform")
def old_platform():
    return RedirectResponse(url_for(DEFAULT_LANG, "intelligence"), status_code=308)


def _register_language_extras(lang):
    def platform():
        return RedirectResponse(url_for(lang, "intelligence"), status_code=308)

    def bare():
        return RedirectResponse(url_for(lang), status_code=308)

    platform.__name__, bare.__name__ = f"old_platform_{lang}", f"bare_{lang}"
    app.route(f"/{lang}/platform", methods=["get"])(platform)
    app.route(f"/{lang}", methods=["get"])(bare)


for _lang in LANGUAGES:
    if _lang != DEFAULT_LANG:
        _register_language_extras(_lang)


# Preserve old indexed URLs without retaining superseded fund claims.
@rt("/thesis")
def old_thesis():
    return RedirectResponse(url_for(DEFAULT_LANG, "advisory"), status_code=308)


@rt("/track-record")
def old_track_record():
    return RedirectResponse(url_for(DEFAULT_LANG, "advisory"), status_code=308)


@rt("/sectors/{slug}")
def old_sector(slug: str):
    return RedirectResponse(url_for(DEFAULT_LANG, "sectors"), status_code=308)


@rt("/favicon.ico")
def favicon():
    return RedirectResponse("/static/favicon.svg", status_code=308)


@rt("/robots.txt")
def robots():
    body = f"User-agent: *\nAllow: /\nDisallow: /set-lang/\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    return Response(body, media_type="text/plain; charset=utf-8")


@rt("/sitemap.xml")
def sitemap():
    entries = []
    for key in PAGES:
        alternates = "".join(
            f'<xhtml:link rel="alternate" hreflang="{info["hreflang"]}" href="{absolute(url_for(code, key))}"/>'
            for code, info in LANGUAGES.items()
        ) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{absolute(url_for(DEFAULT_LANG, key))}"/>'
        for code in LANGUAGES:
            priority = "1.0" if key == "home" else "0.8"
            entries.append(f"<url><loc>{absolute(url_for(code, key))}</loc>{alternates}"
                           f"<changefreq>monthly</changefreq><priority>{priority}</priority></url>")
    body = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + "".join(entries) + "</urlset>\n")
    return Response(body, media_type="application/xml")


if __name__ == "__main__":
    serve()
