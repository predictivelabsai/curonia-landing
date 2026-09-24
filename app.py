"""Curonia Capital Ltd: Baltic and CEE M&A advisory site."""

import os
import secrets

from fasthtml.common import (
    A, Article, Div, H3, P, RedirectResponse, Script, Span, fast_app, serve,
)

from components import (
    CTASection, Card, COMPANY_NUMBER, CONTACT_EMAIL, Eyebrow, Heading, Hero,
    LEGAL_NAME, PLATFORM_URL, REGISTERED_ADDRESS, Section_, Button_, page,
)
from content.team import TEAM
from utils.i18n import get_lang, set_lang, t

# Set CURONIA_SESSION_SECRET in the deployment environment for stable sessions.
app, rt = fast_app(
    live=False,
    static_path=".",
    pico=False,
    secret_key=os.environ.get("CURONIA_SESSION_SECRET") or secrets.token_urlsafe(32),
)


def intro(eyebrow, heading, lede):
    return Section_(
        Eyebrow(eyebrow),
        Heading(1, heading, cls="mt-5 max-w-5xl"),
        P(lede, cls="mt-7 max-w-3xl text-lg md:text-xl leading-relaxed text-ink-muted"),
        cls="pt-20 md:pt-28",
    )


def section_heading(eyebrow, heading, lede=None):
    return Div(
        Eyebrow(eyebrow),
        Heading(2, heading, cls="mt-4 max-w-4xl"),
        P(lede, cls="mt-5 max-w-3xl text-lg leading-relaxed text-ink-muted") if lede else None,
        cls="mb-12",
    )


def service_cards(lang):
    return [
        Card("01", t("sell_title", lang), t("sell_body", lang)),
        Card("02", t("buy_title", lang), t("buy_body", lang)),
        Card("03", t("strategy_title", lang), t("strategy_body", lang)),
    ]


def sector_cards(lang):
    return [
        Card(f"0{i}", t(f"sector_{i}_title", lang), t(f"sector_{i}_body", lang))
        for i in range(1, 6)
    ]


def remember(sess, path):
    sess["_referer"] = path
    return get_lang(sess)


@rt("/set-lang/{code}")
def set_language(code: str, sess):
    set_lang(sess, code)
    return RedirectResponse(sess.get("_referer", "/"), status_code=303)


@rt("/")
def home(sess):
    lang = remember(sess, "/")
    return page(
        t("hero_heading", lang), "/",
        Hero(lang),
        Section_(
            section_heading(t("home_focus_eyebrow", lang), t("home_focus_heading", lang),
                            t("home_focus_lede", lang)),
            Div(*service_cards(lang), cls="grid gap-5 md:grid-cols-3"),
        ),
        Section_(
            Div(
                Eyebrow(t("home_region_eyebrow", lang)),
                Heading(2, t("home_region_heading", lang), cls="mt-4"),
                P(t("home_region_body", lang), cls="mt-5 max-w-3xl text-lg leading-relaxed text-ink-muted"),
                Div(*[Span(name, cls="rounded-full border border-line bg-white px-4 py-2 text-sm text-ink-muted")
                      for name in ("Lithuania", "Latvia", "Estonia", "Poland", "CEE")],
                    cls="mt-8 flex flex-wrap gap-2"),
                cls="max-w-4xl",
            ),
            cls="border-y border-line bg-bg-elevated/70",
        ),
        Section_(
            section_heading(t("home_platform_eyebrow", lang), t("home_platform_heading", lang),
                            t("home_platform_body", lang)),
            Button_(t("learn_platform", lang), "/platform"),
        ),
        CTASection(lang),
        lang=lang,
        body_extra=[Script(src="/static/three-hero.js", type="module")],
    )


@rt("/advisory")
def advisory(sess):
    lang = remember(sess, "/advisory")
    return page(
        t("nav_advisory", lang), "/advisory",
        intro(t("nav_advisory", lang), t("advisory_heading", lang), t("advisory_lede", lang)),
        Section_(
            Div(*service_cards(lang), cls="grid gap-5 md:grid-cols-3"),
            cls="border-t border-line bg-bg-elevated/40",
        ),
        Section_(
            section_heading(t("nav_advisory", lang), t("advisory_process", lang)),
            Div(*[
                Card(f"0{i}", t(f"process_{i}_title", lang), t(f"process_{i}_body", lang))
                for i in range(1, 5)
            ], cls="grid gap-5 md:grid-cols-2 lg:grid-cols-4"),
        ),
        CTASection(lang),
        lang=lang,
    )


@rt("/sectors")
def sectors(sess):
    lang = remember(sess, "/sectors")
    return page(
        t("nav_sectors", lang), "/sectors",
        intro(t("nav_sectors", lang), t("sectors_heading", lang), t("sectors_lede", lang)),
        Section_(Div(*sector_cards(lang), cls="grid gap-5 md:grid-cols-2 lg:grid-cols-3"),
                 cls="border-t border-line"),
        CTASection(lang),
        lang=lang,
    )


@rt("/platform")
def platform(sess):
    lang = remember(sess, "/platform")
    return page(
        t("nav_platform", lang), "/platform",
        intro(t("platform_eyebrow", lang), t("platform_heading", lang), t("platform_lede", lang)),
        Section_(
            Div(*[
                Card(f"0{i}", t(f"platform_{i}_title", lang), t(f"platform_{i}_body", lang))
                for i in range(1, 4)
            ], cls="grid gap-5 md:grid-cols-3"),
            P(t("platform_note", lang), cls="mt-10 max-w-3xl border-l-2 border-accent pl-5 text-ink-muted leading-relaxed"),
            Div(Button_(t("platform_link", lang), PLATFORM_URL), cls="mt-8"),
            cls="border-t border-line bg-bg-elevated/40",
        ),
        CTASection(lang),
        lang=lang,
    )


def member_card(member, lang):
    return Article(
        Div(member["initials"], cls="flex h-14 w-14 items-center justify-center rounded-full bg-bg-elevated font-mono text-accent"),
        H3(member["name"], cls="mt-6 text-2xl font-medium text-ink"),
        P(t(member["bio_key"], lang), cls="mt-4 leading-relaxed text-ink-muted"),
        A("LinkedIn ↗", href=member["linkedin"], target="_blank", rel="noopener noreferrer",
          cls="mt-6 inline-block text-sm font-medium text-accent hover:underline"),
        cls="rounded-2xl border border-line bg-white p-8",
    )


@rt("/team")
def team(sess):
    lang = remember(sess, "/team")
    return page(
        t("nav_team", lang), "/team",
        intro(t("nav_team", lang), t("team_heading", lang), t("team_lede", lang)),
        Section_(Div(*[member_card(member, lang) for member in TEAM],
                     cls="grid gap-5 md:grid-cols-2"), cls="border-t border-line"),
        CTASection(lang),
        lang=lang,
    )


@rt("/contact")
def contact(sess):
    lang = remember(sess, "/contact")
    return page(
        t("nav_contact", lang), "/contact",
        intro(t("nav_contact", lang), t("contact_heading", lang), t("contact_lede", lang)),
        Section_(
            Div(
                Div(
                    Eyebrow(t("contact_email", lang)),
                    A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}",
                      cls="mt-5 block break-all text-xl md:text-2xl font-medium text-accent hover:underline"),
                    cls="rounded-2xl border border-line bg-white p-8",
                ),
                Div(
                    Eyebrow(t("contact_office", lang)),
                    H3(LEGAL_NAME, cls="mt-5 text-xl font-medium"),
                    P(f"{t('company_number', lang)} {COMPANY_NUMBER}", cls="mt-2 text-sm text-ink-muted"),
                    P(REGISTERED_ADDRESS, cls="mt-3 text-ink-muted leading-relaxed"),
                    cls="rounded-2xl border border-line bg-white p-8",
                ),
                cls="grid gap-5 md:grid-cols-2",
            ),
            cls="border-t border-line",
        ),
        lang=lang,
    )


# Preserve old indexed URLs without retaining superseded fund claims.
@rt("/thesis")
def old_thesis():
    return RedirectResponse("/advisory", status_code=308)


@rt("/track-record")
def old_track_record():
    return RedirectResponse("/advisory", status_code=308)


@rt("/sectors/{slug}")
def old_sector(slug: str):
    return RedirectResponse("/sectors", status_code=308)


if __name__ == "__main__":
    serve()
