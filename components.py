"""
Shared FastHTML components for the Curonia Capital landing site.

Clean white/light background with institutional blue accents — matching the
AAA Enterprises corporate palette. Design tokens via Tailwind CDN with a
small inline config block. Custom CSS in static/site.css.
"""

from fasthtml.common import (
    Html, Head, Body, Meta, Title, Link, Script, Style, NotStr,
    Nav, Main, Footer, Header, Section, Article, Aside, Div, Span, A, Img, Svg,
    H1, H2, H3, H4, H5, H6, P, Ul, Ol, Li, Button, Small, Strong, Em, I,
)

from utils.i18n import t, LANGUAGES, DEFAULT_LANG

SITE_NAME = "Curonia Capital"
CONTACT_EMAIL = "info@curoniacapital.com"
LINKEDIN_URL = "#"

def _nav_items(lang: str):
    return [
        (t("nav_thesis", lang), "/thesis"),
        (t("nav_sectors", lang), None, [
            (t("nav_healthcare", lang), "/sectors/healthcare"),
            (t("nav_education", lang), "/sectors/education"),
            (t("nav_technology", lang), "/sectors/technology"),
            (t("nav_services", lang), "/sectors/services"),
        ]),
        (t("nav_track_record", lang), "/track-record"),
        (t("nav_team", lang), "/team"),
        (t("nav_contact", lang), "/contact"),
    ]

TAILWIND_CONFIG = """
tailwind.config = {
  theme: {
    extend: {
      colors: {
        bg: { DEFAULT: '#FAFBFD', elevated: '#F1F5F9', raised: '#FFFFFF' },
        ink: { DEFAULT: '#1A2332', muted: '#475569', dim: '#94A3B8' },
        line: { DEFAULT: '#E2E8F0', bright: '#90A4C1' },
        accent: { DEFAULT: '#2B5F8A', dim: '#EBF4FF', deep: '#1A3D5C' },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'ui-monospace', 'monospace'],
        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
      },
      letterSpacing: {
        tightest: '-0.04em',
        tighter: '-0.025em',
      },
    },
  },
};
"""


def Eyebrow(text, *, href=None):
    cls = "font-mono text-[11px] tracking-[0.18em] uppercase text-accent"
    if href:
        return A(text, href=href, cls=cls + " hover:text-ink transition-colors")
    return Span(text, cls=cls)


def Heading(level, text, *, cls=""):
    tag = {1: H1, 2: H2, 3: H3, 4: H4}[level]
    base = {
        1: "text-4xl sm:text-5xl md:text-7xl font-medium tracking-tightest text-ink leading-[1.05] md:leading-[1.02]",
        2: "text-2xl sm:text-3xl md:text-5xl font-medium tracking-tighter text-ink leading-[1.12] md:leading-[1.08]",
        3: "text-lg sm:text-xl md:text-2xl font-medium tracking-tight text-ink",
        4: "text-base md:text-lg font-medium text-ink",
    }[level]
    return tag(text, cls=f"{base} {cls}".strip())


def Button_(text, *, href="#", primary=True, cls=""):
    base = "inline-flex items-center gap-2 px-5 py-3 rounded-full text-sm font-medium transition-all duration-200"
    if primary:
        style = "bg-accent text-white hover:bg-accent-deep shadow-[0_0_0_1px_#2B5F8A] hover:shadow-[0_0_0_1px_#1A3D5C]"
    else:
        style = "bg-transparent text-ink border border-line-bright hover:border-accent hover:text-accent"
    return A(text, Span("→", cls="text-base"), href=href, cls=f"{base} {style} {cls}".strip())


def Pill(text, *, cls=""):
    return Span(
        text,
        cls=f"inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono tracking-wider uppercase text-ink-muted bg-bg-elevated border border-line {cls}".strip(),
    )


def LinkedInIcon():
    return NotStr(
        '<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">'
        '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 '
        '1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 '
        '3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 '
        '0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 '
        '2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 '
        '23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>'
        '</svg>'
    )


def _LangDropdown(lang: str):
    current_flag = LANGUAGES.get(lang, LANGUAGES["en"])["flag"]
    lang_options = [
        A(f'{info["flag"]} {info["native"]}',
          href=f"/set-lang/{code}",
          cls=f"flex items-center gap-2 px-3 py-1.5 rounded text-sm text-ink-muted hover:bg-bg-elevated hover:text-ink transition-colors {'font-semibold text-accent' if code == lang else ''}")
        for code, info in LANGUAGES.items()
    ]
    return Div(
        Button(
            current_flag,
            type="button",
            onclick="this.nextElementSibling.classList.toggle('hidden')",
            cls="w-9 h-9 flex items-center justify-center rounded-full border border-line hover:border-accent text-base transition-colors",
        ),
        Div(
            *lang_options,
            cls="hidden absolute right-0 mt-2 w-36 rounded-xl border border-line bg-white py-1.5 shadow-2xl z-50",
        ),
        cls="relative",
    )


def Navbar(current_path: str = "/", lang: str = "en"):
    nav_items = _nav_items(lang)

    def _nav_item(item):
        if len(item) == 2:
            label, href = item
            active = current_path == href
            return Li(
                A(
                    label,
                    href=href,
                    cls=f"text-sm text-ink-muted hover:text-ink transition-colors {'text-ink font-medium' if active else ''}",
                )
            )
        label, _, children = item
        return Li(
            Div(
                Span(label, cls="text-sm text-ink-muted hover:text-ink transition-colors flex items-center gap-1 cursor-default"),
                Span("▾", cls="text-xs text-ink-dim"),
                cls="flex items-center gap-1",
            ),
            Ul(
                *[
                    Li(
                        A(
                            sub_label,
                            href=sub_href,
                            cls="block px-4 py-2 text-sm text-ink-muted hover:text-ink hover:bg-bg-elevated",
                        )
                    )
                    for sub_label, sub_href in children
                ],
                cls="absolute right-0 mt-3 w-64 rounded-xl border border-line bg-white py-2 shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200",
            ),
            cls="relative group",
        )

    def _flat_mobile():
        out = []
        for item in nav_items:
            if len(item) == 2:
                out.append(item)
            else:
                label, _, children = item
                out.append((label, None))
                out.extend(children)
        return out

    mobile_items = [
        Li(Span(lbl, cls="block text-xs font-mono tracking-widest uppercase text-ink-dim pt-3"))
        if href is None
        else Li(A(lbl, href=href, cls=f"block py-2 text-base {'text-accent' if current_path == href else 'text-ink hover:text-accent'}"))
        for lbl, href in _flat_mobile()
    ]

    return Nav(
        Div(
            A(
                Span("◆", cls="text-accent mr-2"),
                Span(SITE_NAME, cls="font-medium tracking-tight"),
                href="/",
                cls="flex items-center text-ink text-base hover:text-accent transition-colors",
            ),
            Ul(
                *[_nav_item(i) for i in nav_items],
                cls="hidden lg:flex items-center gap-7",
            ),
            Div(
                _LangDropdown(lang),
                A(
                    t("nav_get_in_touch", lang),
                    href="/contact",
                    cls="hidden lg:inline-flex items-center gap-2 px-4 py-2 rounded-full text-xs font-medium bg-accent text-white hover:bg-accent-deep transition-colors",
                ),
                cls="hidden lg:flex items-center gap-3",
            ),
            Button(
                Span("☰", id="nav-burger-icon", cls="text-2xl leading-none"),
                type="button",
                aria_label="Open menu",
                onclick=(
                    "const m=document.getElementById('mobile-nav');"
                    "const i=document.getElementById('nav-burger-icon');"
                    "const open=m.classList.toggle('hidden')===false;"
                    "i.textContent=open?'✕':'☰';"
                ),
                cls="lg:hidden text-ink hover:text-accent w-10 h-10 flex items-center justify-center rounded-full border border-line",
            ),
            cls="max-w-7xl mx-auto px-5 md:px-6 flex items-center justify-between h-16 gap-4",
        ),
        Div(
            Ul(*mobile_items, cls="px-5 pb-5 pt-2 space-y-1"),
            Div(
                Div(
                    *[A(f'{info["flag"]} {info["native"]}', href=f"/set-lang/{code}",
                        cls=f"inline-flex px-3 py-1.5 rounded-full text-xs border {'border-accent text-accent' if code == lang else 'border-line text-ink-muted hover:border-accent'}")
                      for code, info in LANGUAGES.items()],
                    cls="flex flex-wrap gap-2 px-5 mb-4",
                ),
                A(
                    t("nav_get_in_touch", lang),
                    href="/contact",
                    cls="block text-center px-4 py-3 rounded-full text-sm font-medium bg-accent text-white mx-5 mb-5",
                ),
            ),
            id="mobile-nav",
            cls="hidden lg:hidden border-t border-line bg-white",
        ),
        cls="sticky top-0 z-50 backdrop-blur-md bg-bg/80 border-b border-line",
    )


def Section_(*content, bleed=False, cls=""):
    inner_cls = "max-w-7xl mx-auto px-5 md:px-6" if not bleed else "w-full"
    return Section(Div(*content, cls=inner_cls), cls=f"py-14 md:py-20 lg:py-28 {cls}".strip())


def Footer_(lang: str = "en"):
    columns = [
        (t("footer_fund", lang), [
            (t("nav_thesis", lang), "/thesis"),
            (t("nav_track_record", lang), "/track-record"),
            (t("nav_team", lang), "/team"),
        ]),
        (t("footer_sectors", lang), [
            (t("nav_healthcare", lang), "/sectors/healthcare"),
            (t("nav_education", lang), "/sectors/education"),
            (t("nav_technology", lang), "/sectors/technology"),
            (t("nav_services", lang), "/sectors/services"),
        ]),
        (t("footer_connect", lang), [
            (t("nav_contact", lang), "/contact"),
            ("AAA Enterprises", "https://www.aaaenterprises.lt/en"),
        ]),
    ]

    col_divs = [
        Div(
            H4(title, cls="text-xs font-mono tracking-[0.18em] uppercase text-ink-muted mb-5"),
            Ul(
                *[Li(A(label, href=href, cls="text-sm text-ink hover:text-accent transition-colors", **({"target": "_blank"} if href.startswith("http") else {})), cls="mb-2") for label, href in links],
                cls="space-y-2",
            ),
        )
        for title, links in columns
    ]

    return Footer(
        Div(
            Div(
                Div(
                    A(
                        Span("◆", cls="text-accent mr-2"),
                        Span(SITE_NAME, cls="font-medium text-ink tracking-tight"),
                        href="/",
                        cls="flex items-center text-lg mb-4",
                    ),
                    P(t("footer_tagline", lang), cls="text-ink-muted text-sm max-w-xs mb-5 leading-relaxed"),
                    P(
                        "Curonia Capital", NotStr("<br>"),
                        t("footer_part_of", lang), NotStr("<br>"),
                        t("footer_address", lang),
                        cls="text-ink-dim text-xs leading-relaxed",
                    ),
                ),
                *col_divs,
                cls="grid grid-cols-2 md:grid-cols-4 gap-10",
            ),
            Div(
                Div(f"© {__import__('datetime').datetime.now().year} {t('footer_copyright', lang)}", cls="text-ink-dim text-xs"),
                Div(
                    A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", cls="text-ink-dim text-xs hover:text-accent break-all"),
                    cls="flex items-center flex-wrap gap-y-2",
                ),
                cls="mt-10 md:mt-14 pt-6 border-t border-line flex items-start md:items-center justify-between flex-wrap gap-4",
            ),
            cls="max-w-7xl mx-auto px-5 md:px-6",
        ),
        cls="py-12 md:py-16 border-t border-line bg-bg-elevated",
    )


def page(title: str, current_path: str = "/", *content, head_extra=None, body_extra=None, lang: str = "en"):
    tagline = t("footer_tagline", lang)
    head_children = [
        Meta(charset="utf-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1"),
        Meta(name="description", content=f"{SITE_NAME} — {tagline}"),
        Link(rel="icon", href="/static/favicon.svg", type="image/svg+xml"),
        Title(f"{title} · {SITE_NAME}"),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Cormorant+Garamond:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap",
        ),
        Script(src="https://cdn.tailwindcss.com"),
        Script(NotStr(TAILWIND_CONFIG)),
        Link(rel="stylesheet", href="/static/site.css"),
    ]
    if head_extra:
        head_children.extend(head_extra if isinstance(head_extra, list) else [head_extra])

    html_lang = {"en": "en", "lt": "lt", "lv": "lv", "et": "et"}.get(lang, "en")

    body_children = [
        Navbar(current_path, lang=lang),
        Main(*content, cls="min-h-screen"),
        Footer_(lang=lang),
    ]
    if body_extra:
        body_children.extend(body_extra if isinstance(body_extra, list) else [body_extra])

    return Html(
        Head(*head_children),
        Body(*body_children, cls="bg-bg text-ink font-sans antialiased"),
        lang=html_lang,
    )


def Hero(*, lang: str = "en", canvas=True, tall=True):
    headline = (
        Span(t("hero_h1_1", lang)),
        Span(t("hero_h1_2", lang), cls="text-accent"),
    )
    lede = t("hero_lede", lang)
    ctas = [(t("hero_cta_thesis", lang), "/thesis", True), (t("hero_cta_team", lang), "/team", False)]

    height = "min-h-[78vh] md:min-h-[86vh]" if tall else "min-h-[54vh] md:min-h-[58vh]"

    canvas_div = Div(id="three-hero", cls="absolute inset-0 z-10 opacity-40 pointer-events-none") if canvas else None

    return Section(
        Div(
            canvas_div,
            Div(cls="absolute inset-0 z-20 bg-gradient-to-b from-bg/10 via-transparent to-bg pointer-events-none"),
            Div(
                Eyebrow(t("hero_eyebrow", lang)),
                H1(*headline, cls="mt-5 md:mt-6 text-[40px] sm:text-5xl md:text-7xl lg:text-[84px] font-medium tracking-tightest text-ink leading-[1.05] md:leading-[1.02] max-w-5xl"),
                P(lede, cls="mt-6 md:mt-8 text-base md:text-xl text-ink-muted max-w-2xl leading-relaxed"),
                Div(
                    *[Button_(text, href=href, primary=primary) for text, href, primary in ctas],
                    cls="mt-8 md:mt-10 flex items-center gap-3 flex-wrap",
                ),
                cls="relative z-30 max-w-7xl mx-auto px-5 md:px-6 py-16 md:py-0",
            ),
            cls=f"relative {height} flex items-center overflow-hidden bg-bg",
        ),
        Div(
            Div(
                Div(t("hero_parent", lang), cls="text-[11px] md:text-xs font-mono tracking-[0.18em] uppercase text-ink-dim"),
                Div(
                    Span(t("hero_group_assets", lang) + " ", cls="text-ink-muted text-xs md:text-sm"),
                    Span("~€3B ", cls="text-accent text-xs md:text-sm font-mono"),
                    Span(t("hero_since", lang), cls="text-ink-muted text-xs md:text-sm"),
                ),
                cls="max-w-7xl mx-auto px-5 md:px-6 py-4 md:py-5 flex items-center justify-between flex-wrap gap-3",
            ),
            cls="border-y border-line bg-bg-elevated/60",
        ),
    )


def Pillar(number: str, title: str, body: str, *, icon="◆"):
    return Div(
        Div(
            Span(icon, cls="text-accent text-xl"),
            Span(number, cls="font-mono text-xs tracking-widest text-ink-dim ml-auto"),
            cls="flex items-center mb-6",
        ),
        Heading(3, title, cls="mb-3"),
        P(body, cls="text-ink-muted text-sm leading-relaxed"),
        cls="p-7 rounded-2xl bg-white border border-line hover:border-accent/50 transition-colors group",
    )


def MetricTile(value, unit, caption, *, cls=""):
    return Div(
        Div(
            Span(value, cls="text-4xl md:text-5xl font-medium tracking-tighter text-ink"),
            Span(unit, cls="text-lg text-accent ml-1"),
            cls="flex items-baseline",
        ),
        P(caption, cls="text-ink-muted text-sm mt-2"),
        cls=f"p-6 rounded-2xl bg-white border border-line {cls}".strip(),
    )


def CTASection(*, headline=None, body=None, cta_label=None, cta_href="/contact", lang: str = "en"):
    headline = headline or t("cta_heading", lang)
    body = body or t("cta_body", lang)
    cta_label = cta_label or t("cta_button", lang)
    return Section(
        Div(
            Div(
                Eyebrow(t("cta_eyebrow", lang)),
                Heading(2, headline, cls="mt-4 max-w-3xl"),
                P(body, cls="mt-5 text-ink-muted text-lg max-w-2xl leading-relaxed"),
                Div(
                    Button_(cta_label, href=cta_href, primary=True),
                    Button_(t("cta_thesis", lang), href="/thesis", primary=False),
                    cls="mt-8 flex items-center gap-3 flex-wrap",
                ),
                cls="max-w-7xl mx-auto px-6 py-20 md:py-28 relative z-10",
            ),
            Div(cls="absolute inset-0 bg-gradient-to-br from-accent/10 via-transparent to-transparent pointer-events-none"),
            cls="relative border-y border-line bg-bg-elevated/60 overflow-hidden",
        ),
    )


def NewsSection(*, category: str, title: str = "Market intelligence",
                subtitle: str | None = None, lang: str = "en"):
    from content import news as _news

    items = _news.items_for(category)
    if not items:
        return Div()

    def _item(it):
        pub = _news.format_published(it.get("published"))
        meta = [Span(it["source"], cls="text-ink-dim text-xs font-mono")]
        if pub:
            meta.append(Span("·", cls="text-ink-dim text-xs mx-2"))
            meta.append(Span(pub, cls="text-ink-dim text-xs"))
        return A(
            Div(
                H4(it["title"], cls="text-ink text-base md:text-lg font-medium leading-snug mb-3 group-hover:text-accent transition-colors"),
                Div(*meta, cls="flex items-center flex-wrap"),
                cls="p-5 md:p-6 h-full rounded-2xl bg-white border border-line group-hover:border-accent/60 transition-colors",
            ),
            href=it["url"],
            target="_blank",
            rel="noopener",
            cls="block group",
        )

    last = _news.last_refresh_iso()
    last_label = t("news_last_refresh", lang)

    return Section_(
        Div(
            Div(
                Eyebrow(t("news_eyebrow", lang)),
                Heading(2, title, cls="mt-4 max-w-3xl"),
                P(subtitle, cls="mt-4 text-ink-muted max-w-2xl leading-relaxed") if subtitle else None,
                cls="md:flex-1",
            ),
            Div(
                Span(t("news_refresh", lang),
                     cls="text-ink-dim text-xs"),
                Span(NotStr("&nbsp;·&nbsp;") + f"{last_label}: {last}" if last else "",
                     cls="text-ink-dim text-xs"),
                cls="text-left md:text-right md:max-w-xs mt-4 md:mt-0",
            ),
            cls="mb-10 flex flex-col md:flex-row md:items-end md:justify-between gap-4",
        ),
        Div(
            *[_item(it) for it in items],
            cls="grid md:grid-cols-2 gap-4",
        ),
        cls="border-t border-line",
    )
