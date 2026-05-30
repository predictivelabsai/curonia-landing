"""
Curonia Capital — multipage FastHTML landing site with i18n (EN/LT/LV/ET).

Baltic growth equity fund: AI-powered transformation of founder-led SMEs.
Part of AAA Enterprises. Content lives in content/*.py; routes are thin
composition over components.py. Language is stored in session cookie.
"""

from fasthtml.common import (
    fast_app, serve, Div, Span, A, P, Ul, Li, Section, Article, Header, Table,
    Thead, Tbody, Tr, Th, Td, NotStr, Script, Style, H1, H2, H3, H4, Button,
    RedirectResponse,
)

from components import (
    page, Hero, Pillar, MetricTile, CTASection, NewsSection, Section_,
    Heading, Eyebrow, Pill, Button_, LinkedInIcon,
    CONTACT_EMAIL, LINKEDIN_URL,
)
from content.team import TEAM
from content import news as news_mod
from utils.i18n import t, get_lang, set_lang

news_mod.start_background_refresh()

app, rt = fast_app(live=False, static_path=".", pico=False, secret_key="curonia-cap-2024")

BIO_KEYS = {"Aurimas Martišauskas": "bio_am", "Matas Jakubėlis": "bio_mj",
            "Julian Kaljuvee": "bio_jk", "Ieva Belickaitė": "bio_ib"}


# ---------- Language switcher ----------

@rt("/set-lang/{code}")
def set_language(code: str, sess):
    set_lang(sess, code)
    ref = sess.get("_referer", "/")
    return RedirectResponse(ref, status_code=303)


# ---------- / Home ----------

@rt("/")
def home(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/"

    pillars = [
        ("01", t("pillar_1_title", lang), t("pillar_1_body", lang)),
        ("02", t("pillar_2_title", lang), t("pillar_2_body", lang)),
        ("03", t("pillar_3_title", lang), t("pillar_3_body", lang)),
        ("04", t("pillar_4_title", lang), t("pillar_4_body", lang)),
    ]

    return page(
        t("hero_eyebrow", lang),
        "/",
        Hero(lang=lang),

        Section_(
            Div(
                Eyebrow(t("fund_eyebrow", lang)),
                Heading(2, t("fund_heading", lang), cls="mt-4 max-w-4xl"),
                P(t("fund_lede", lang), cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed"),
                cls="mb-14",
            ),
            Div(
                MetricTile("€50", "M", t("metric_fund_size", lang)),
                MetricTile("€2–5", "M", t("metric_investment", lang)),
                MetricTile("5–10", "", t("metric_investments", lang)),
                MetricTile("25", "%", t("metric_target_irr", lang)),
                MetricTile("7+2", "yr", t("metric_fund_term", lang)),
                MetricTile("LT LV EE", "", t("metric_geography", lang)),
                cls="grid md:grid-cols-3 lg:grid-cols-6 gap-4",
            ),
            cls="border-b border-line",
        ),

        Section_(
            Div(
                Eyebrow(t("thesis_eyebrow", lang)),
                Heading(2, t("thesis_heading", lang), cls="mt-4 max-w-4xl"),
                P(t("thesis_lede", lang), cls="mt-5 text-ink-muted text-lg max-w-3xl"),
                cls="mb-14",
            ),
            Div(
                *[Pillar(n, ti, bo) for n, ti, bo in pillars],
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
        ),

        Section_(
            Div(
                Eyebrow(t("sectors_eyebrow", lang)),
                Heading(2, t("sectors_heading", lang), cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                _sector_link(t("sector_healthcare_title", lang), t("sector_healthcare_body", lang), "/sectors/healthcare"),
                _sector_link(t("sector_education_title", lang), t("sector_education_body", lang), "/sectors/education"),
                _sector_link(t("sector_technology_title", lang), t("sector_technology_body", lang), "/sectors/technology"),
                _sector_link(t("sector_services_title", lang), t("sector_services_body", lang), "/sectors/services"),
                cls="grid md:grid-cols-2 gap-5",
            ),
            cls="border-y border-line bg-bg-elevated/40",
        ),

        Section_(
            Div(
                Eyebrow(t("track_eyebrow", lang)),
                Heading(2, t("track_heading", lang), cls="mt-4 max-w-3xl"),
                P(t("track_lede", lang), cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed"),
                Button_(t("track_cta", lang), href="/track-record", primary=False, cls="mt-8"),
                cls="mb-14",
            ),
            Div(
                _track_tile("~€3B", t("track_tile_1", lang)),
                _track_tile("€750M+", t("track_tile_2", lang)),
                _track_tile("100+", t("track_tile_3", lang)),
                _track_tile("Since 1993", t("track_tile_4", lang)),
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
        ),

        Section_(
            Div(
                Eyebrow(t("team_eyebrow", lang)),
                Heading(2, t("team_heading", lang), cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                *[_team_card_compact(m) for m in TEAM],
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
            Div(
                Button_(t("team_cta", lang), href="/team", primary=False),
                cls="mt-10",
            ),
            cls="border-t border-line",
        ),

        NewsSection(
            category="home",
            title=t("news_home_title", lang),
            subtitle=t("news_home_sub", lang),
            lang=lang,
        ),

        CTASection(lang=lang),

        body_extra=[Script(src="/static/three-hero.js", type="module")],
        lang=lang,
    )


def _sector_link(title, body, href):
    return A(
        Div(
            Div(
                Span(title, cls="text-ink text-xl font-medium tracking-tight"),
                Span("→", cls="text-accent text-xl ml-auto"),
                cls="flex items-center mb-3",
            ),
            P(body, cls="text-ink-muted text-sm leading-relaxed"),
            cls="p-7 rounded-2xl border border-line bg-white hover:border-accent/50 hover:bg-bg-elevated transition-all",
        ),
        href=href,
        cls="block",
    )


def _track_tile(value, caption):
    return Div(
        Div(value, cls="text-2xl md:text-3xl font-medium tracking-tight text-accent mb-2"),
        P(caption, cls="text-ink-muted text-sm leading-relaxed"),
        cls="p-6 rounded-2xl bg-white border border-line",
    )


def _team_card_compact(m):
    return Div(
        Div(
            Heading(3, m["name"], cls="mb-1"),
            A(
                LinkedInIcon(),
                href=m["linkedin"],
                target="_blank",
                cls="text-ink-muted hover:text-accent transition-colors shrink-0",
            ),
            cls="flex items-center gap-3",
        ),
        cls="p-6 rounded-2xl bg-white border border-line",
    )


# ---------- /thesis ----------

@rt("/thesis")
def thesis(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/thesis"

    pillars = [
        ("01", t("pillar_1_title", lang), t("thesis_p1_body", lang)),
        ("02", t("pillar_2_title", lang), t("thesis_p2_body", lang)),
        ("03", t("pillar_3_title", lang), t("thesis_p3_body", lang)),
        ("04", t("pillar_4_title", lang), t("thesis_p4_body", lang)),
    ]

    value_creation = [
        (t("vc_digitise", lang), t("vc_digitise_body", lang)),
        (t("vc_automate", lang), t("vc_automate_body", lang)),
        (t("vc_consolidate", lang), t("vc_consolidate_body", lang)),
        (t("vc_scale", lang), t("vc_scale_body", lang)),
    ]

    return page(
        t("thesis_page_title", lang),
        "/thesis",
        Section_(
            Eyebrow(t("thesis_eyebrow", lang)),
            Heading(1, t("thesis_heading", lang), cls="mt-5 max-w-5xl"),
            P(t("thesis_page_lede", lang), cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),
        Section_(
            Div(
                Eyebrow(t("thesis_pillars_eyebrow", lang)),
                Heading(2, t("thesis_pillars_heading", lang), cls="mt-4"),
                cls="mb-14",
            ),
            Div(*[_thesis_row(n, ti, bo) for n, ti, bo in pillars], cls="divide-y divide-line border-y border-line"),
        ),
        Section_(
            Div(
                Eyebrow(t("vc_eyebrow", lang)),
                Heading(2, t("vc_heading", lang), cls="mt-4 max-w-4xl"),
                P(t("vc_lede", lang), cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed"),
                cls="mb-14",
            ),
            Div(
                *[Div(
                    Div(
                        Span(f"0{i+1}", cls="font-mono text-xs tracking-widest text-accent"),
                        cls="mb-3",
                    ),
                    Heading(3, vc_title, cls="mb-2"),
                    P(vc_body, cls="text-ink-muted text-sm leading-relaxed"),
                    cls="p-7 rounded-2xl bg-white border border-line",
                ) for i, (vc_title, vc_body) in enumerate(value_creation)],
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
            cls="border-t border-line bg-bg-elevated/40",
        ),
        Section_(
            Div(
                Eyebrow(t("ee_eyebrow", lang)),
                Heading(2, t("ee_heading", lang), cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                MetricTile("3–6×", "EBITDA", t("ee_entry_cash", lang)),
                MetricTile("10–14×", "EBITDA", t("ee_exit_pan", lang)),
                MetricTile("3–5×", "ARR", t("ee_entry_saas", lang)),
                MetricTile("6–9×", "ARR", t("ee_exit_ai", lang)),
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
        ),
        CTASection(lang=lang),
        body_extra=[Script(src="/static/three-hero.js", type="module")],
        lang=lang,
    )


def _thesis_row(number, title, body):
    return Div(
        Div(
            Div(number, cls="font-mono text-xs tracking-widest text-accent"),
            cls="md:w-24 shrink-0",
        ),
        Div(
            Heading(3, title, cls="mb-3"),
            P(body, cls="text-ink-muted leading-relaxed"),
            cls="flex-1",
        ),
        cls="flex flex-col md:flex-row gap-6 py-10",
    )


# ---------- /sectors/* ----------

_SECTOR_KEYS = {
    "healthcare": {
        "eyebrow": "nav_healthcare",
        "title": "nav_healthcare",
        "headline": "sh_headline",
        "lede": "sh_lede",
        "pillars": [("sh_dental", "sh_dental_body"), ("sh_derma", "sh_derma_body"), ("sh_tourism", "sh_tourism_body")],
        "pills": "sh_pills",
        "news_key": "healthcare",
        "news_title": "sh_news_title",
        "news_sub": "sh_news_sub",
    },
    "education": {
        "eyebrow": "nav_education",
        "title": "nav_education",
        "headline": "se_headline",
        "lede": "se_lede",
        "pillars": [("se_tutoring", "se_tutoring_body"), ("se_vocational", "se_vocational_body"), ("se_schools", "se_schools_body")],
        "pills": "se_pills",
        "news_key": "education",
        "news_title": "se_news_title",
        "news_sub": "se_news_sub",
    },
    "technology": {
        "eyebrow": "nav_technology",
        "title": "nav_technology",
        "headline": "st_headline",
        "lede": "st_lede",
        "pillars": [("st_saas", "st_saas_body"), ("st_it", "st_it_body"), ("st_cyber", "st_cyber_body")],
        "pills": "st_pills",
        "news_key": "technology",
        "news_title": "st_news_title",
        "news_sub": "st_news_sub",
    },
    "services": {
        "eyebrow": "nav_services",
        "title": "nav_services",
        "headline": "ss_headline",
        "lede": "ss_lede",
        "pillars": [("ss_professional", "ss_professional_body"), ("ss_engineering", "ss_engineering_body"), ("ss_staffing", "ss_staffing_body")],
        "pills": "ss_pills",
        "news_key": "services",
        "news_title": "ss_news_title",
        "news_sub": "ss_news_sub",
    },
}


def _get_pills(key, lang):
    from utils.i18n import TRANSLATIONS
    entry = TRANSLATIONS.get(key, {})
    val = entry.get(lang) or entry.get("en") or []
    return val if isinstance(val, list) else [val]


def _sector_page(slug, lang):
    sk = _SECTOR_KEYS[slug]

    pills = _get_pills(sk["pills"], lang)

    return page(
        t(sk["title"], lang),
        f"/sectors/{slug}",
        Section_(
            Eyebrow(t(sk["eyebrow"], lang)),
            Heading(1, t(sk["headline"], lang), cls="mt-5 max-w-5xl"),
            P(t(sk["lede"], lang), cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            Div(
                *[Pill(r) for r in pills],
                cls="mt-10 flex flex-wrap gap-2",
            ),
            cls="pt-24",
        ),
        Section_(
            Div(
                Eyebrow(t("sp_where_focus", lang)),
                Heading(2, t("sp_focal_points", lang), cls="mt-4"),
                cls="mb-14",
            ),
            Div(
                *[Pillar(f"0{i+1}", t(tk, lang), t(bk, lang)) for i, (tk, bk) in enumerate(sk["pillars"])],
                cls="grid md:grid-cols-3 gap-5",
            ),
        ),
        NewsSection(category=sk["news_key"], title=t(sk["news_title"], lang), subtitle=t(sk["news_sub"], lang), lang=lang),
        CTASection(lang=lang),
        lang=lang,
    )


@rt("/sectors/healthcare")
def sec_healthcare(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/sectors/healthcare"
    return _sector_page("healthcare", lang)


@rt("/sectors/education")
def sec_education(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/sectors/education"
    return _sector_page("education", lang)


@rt("/sectors/technology")
def sec_technology(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/sectors/technology"
    return _sector_page("technology", lang)


@rt("/sectors/services")
def sec_services(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/sectors/services"
    return _sector_page("services", lang)


# ---------- /track-record ----------

@rt("/track-record")
def track_record(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/track-record"

    group_entities = [
        ("1 Asset Management", t("tr_1am_desc", lang), "€750M+ AUM"),
        ("RATO Bank", t("tr_rato_desc", lang), "€120M+ deposits"),
        ("Orion Securities", t("tr_orion_desc", lang), "€2.1B+ custody"),
        ("Taurus Wealth", t("tr_taurus_desc", lang), "€95M+ AUM"),
        ("AAA Law", t("tr_law_desc", lang), "100+ professionals"),
    ]

    fund_precedents = [
        {
            "name": t("tr_pet_name", lang),
            "manager": "1 Asset Management",
            "description": t("tr_pet_desc", lang),
            "tags": _get_pills("tr_pet_tags", lang),
        },
        {
            "name": t("tr_edu_name", lang),
            "manager": "1 Asset Management",
            "description": t("tr_edu_desc", lang),
            "tags": _get_pills("tr_edu_tags", lang),
        },
        {
            "name": t("tr_broader_name", lang),
            "manager": "1 Asset Management",
            "description": t("tr_broader_desc", lang),
            "tags": _get_pills("tr_broader_tags", lang),
        },
    ]

    return page(
        t("tr_page_title", lang),
        "/track-record",
        Section_(
            Eyebrow(t("track_eyebrow", lang)),
            Heading(1, t("tr_heading", lang), cls="mt-5 max-w-5xl"),
            P(t("tr_lede", lang), cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),

        Section_(
            Div(
                Eyebrow(t("tr_glance_eyebrow", lang)),
                Heading(2, t("tr_glance_heading", lang), cls="mt-4"),
                cls="mb-14",
            ),
            Div(
                MetricTile("~€3", "B", t("tr_metric_assets", lang)),
                MetricTile("6,000", "+", t("tr_metric_investors", lang)),
                MetricTile("100", "+", t("tr_metric_pros", lang)),
                MetricTile("1993", "", t("tr_metric_founded", lang)),
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
            cls="border-b border-line",
        ),

        Section_(
            Div(
                Eyebrow(t("tr_entities_eyebrow", lang)),
                Heading(2, t("tr_entities_heading", lang), cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                *[Div(
                    Div(
                        Heading(3, name, cls="mb-1"),
                        Span(metric, cls="text-accent text-sm font-mono"),
                        cls="flex items-center justify-between gap-4 mb-3",
                    ),
                    P(desc, cls="text-ink-muted text-sm leading-relaxed"),
                    cls="p-7 rounded-2xl bg-white border border-line",
                ) for name, desc, metric in group_entities],
                cls="grid md:grid-cols-2 lg:grid-cols-3 gap-5",
            ),
        ),

        Section_(
            Div(
                Eyebrow(t("tr_precedents_eyebrow", lang)),
                Heading(2, t("tr_precedents_heading", lang), cls="mt-4 max-w-3xl"),
                P(t("tr_precedents_lede", lang), cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed"),
                cls="mb-14",
            ),
            Div(
                *[Div(
                    Div(
                        Heading(3, p["name"], cls="mb-1"),
                        P(p["manager"], cls="text-accent text-sm font-mono mb-4"),
                    ),
                    P(p["description"], cls="text-ink-muted text-sm leading-relaxed mb-5"),
                    Div(*[Pill(tg) for tg in p["tags"]], cls="flex flex-wrap gap-2"),
                    cls="p-7 rounded-2xl bg-white border border-line",
                ) for p in fund_precedents],
                cls="grid md:grid-cols-3 gap-5",
            ),
            cls="border-t border-line bg-bg-elevated/40",
        ),

        NewsSection(
            category="pe",
            title=t("tr_pe_news_title", lang),
            subtitle=t("tr_pe_news_sub", lang),
            lang=lang,
        ),

        CTASection(lang=lang),
        lang=lang,
    )


# ---------- /team ----------

@rt("/team")
def team(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/team"

    return page(
        t("nav_team", lang),
        "/team",
        Section_(
            Eyebrow(t("team_eyebrow", lang)),
            Heading(1, t("team_page_heading", lang), cls="mt-5 max-w-4xl"),
            P(t("team_page_lede", lang), cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),
        Section_(
            Div(
                *[_member_card(m, lang) for m in TEAM],
                cls="grid md:grid-cols-2 gap-5",
            ),
        ),
        CTASection(
            headline=t("team_cta_headline", lang),
            body=t("team_cta_body", lang),
            cta_label=t("team_cta_label", lang),
            lang=lang,
        ),
        lang=lang,
    )


def _member_card(m, lang="en"):
    bio_key = BIO_KEYS.get(m["name"])
    bio = t(bio_key, lang) if bio_key else m["bio"]
    return Article(
        Div(
            Heading(3, m["name"], cls="mb-0"),
            A(
                LinkedInIcon(),
                href=m["linkedin"],
                target="_blank",
                cls="text-ink-muted hover:text-accent transition-colors shrink-0",
            ),
            cls="flex items-center gap-3 mb-5",
        ),
        P(bio, cls="text-ink-muted leading-relaxed"),
        cls="p-8 rounded-2xl bg-white border border-line",
    )


# ---------- /contact ----------

@rt("/contact")
def contact(sess):
    lang = get_lang(sess)
    sess["_referer"] = "/contact"

    return page(
        t("contact_page_title", lang),
        "/contact",
        Section_(
            Eyebrow(t("nav_contact", lang)),
            Heading(1, t("contact_heading", lang), cls="mt-5 max-w-4xl"),
            P(t("contact_lede", lang), cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            cls="pt-24",
        ),
        Section_(
            Div(
                Div(
                    Eyebrow(t("contact_write", lang)),
                    A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}",
                      cls="mt-4 block text-xl md:text-2xl font-medium text-ink hover:text-accent break-all transition-colors"),
                    P(t("contact_note", lang), cls="mt-4 text-ink-muted leading-relaxed text-sm"),
                    Div(
                        Button_("Email " + CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", primary=True),
                        cls="mt-8",
                    ),
                    cls="p-10 rounded-2xl bg-white border border-line",
                ),
                Div(
                    Div(
                        H3(t("contact_office", lang), cls="text-sm font-mono tracking-widest uppercase text-ink-muted mb-3"),
                        P("Curonia Capital", cls="text-ink"),
                        P(t("footer_part_of", lang), cls="text-ink-muted"),
                        P("Upės str. 21", cls="text-ink-muted"),
                        P("Vilnius, Lithuania", cls="text-ink-muted"),
                        cls="mb-10",
                    ),
                    Div(
                        H3(t("contact_parent", lang), cls="text-sm font-mono tracking-widest uppercase text-ink-muted mb-3"),
                        A("AAA Enterprises", href="https://www.aaaenterprises.lt/en", target="_blank", cls="block text-ink hover:text-accent mb-2"),
                        A("1 Asset Management", href="https://www.1am.lt", target="_blank", cls="block text-ink hover:text-accent mb-2"),
                    ),
                    cls="p-10 rounded-2xl bg-white border border-line",
                ),
                cls="grid md:grid-cols-2 gap-5",
            ),
        ),
        lang=lang,
    )


if __name__ == "__main__":
    serve()
