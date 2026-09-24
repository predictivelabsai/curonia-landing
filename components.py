"""Shared layout and presentation for the Curonia Capital advisory site."""

from datetime import datetime

from fasthtml.common import (
    A, Body, Button, Div, Footer, H1, H2, H3, Head, Html, Li, Link,
    Main, Meta, Nav, NotStr, P, Script, Section, Span, Title, Ul,
)

from utils.i18n import LANGUAGES, t

SITE_NAME = "Curonia Capital"
LEGAL_NAME = "Curonia Capital Ltd"
COMPANY_NUMBER = "14537690"
REGISTERED_ADDRESS = "155 Minories Street, Suite 275, London, London, United Kingdom, EC3N 1AD"
CONTACT_EMAIL = "info@curoniacapital.com"
PLATFORM_URL = "https://liquidround.com/"

TAILWIND_CONFIG = """
tailwind.config = {
  theme: { extend: {
    colors: {
      bg: { DEFAULT: '#FAFBFD', elevated: '#F1F5F9' },
      ink: { DEFAULT: '#1A2332', muted: '#475569', dim: '#94A3B8' },
      line: '#E2E8F0',
      accent: { DEFAULT: '#2B5F8A', deep: '#1A3D5C' },
    },
    fontFamily: {
      sans: ['Inter', 'system-ui', 'sans-serif'],
      mono: ['JetBrains Mono', 'ui-monospace', 'monospace'],
    },
  } },
};
"""


def nav_items(lang):
    return [
        (t("nav_advisory", lang), "/advisory"),
        (t("nav_sectors", lang), "/sectors"),
        (t("nav_platform", lang), "/platform"),
        (t("nav_team", lang), "/team"),
        (t("nav_contact", lang), "/contact"),
    ]


def Button_(label, href, *, primary=True):
    style = "bg-accent text-white hover:bg-accent-deep" if primary else "border border-line bg-white text-ink hover:border-accent hover:text-accent"
    return A(label, Span("↗", cls="ml-3"), href=href,
             cls=f"inline-flex items-center rounded-full px-5 py-3 text-sm font-medium transition-colors {style}")


def Eyebrow(label):
    return Span(label, cls="font-mono text-[11px] tracking-[0.18em] uppercase text-accent")


def Heading(level, label, *, cls=""):
    tag = {1: H1, 2: H2, 3: H3}[level]
    sizes = {1: "text-4xl sm:text-5xl md:text-7xl", 2: "text-3xl md:text-5xl", 3: "text-xl md:text-2xl"}
    return tag(label, cls=f"{sizes[level]} font-medium tracking-tight leading-tight text-ink {cls}".strip())


def Section_(*children, cls=""):
    return Section(Div(*children, cls="mx-auto max-w-7xl px-5 md:px-6"),
                   cls=f"py-16 md:py-24 {cls}".strip())


def Card(number, title, body):
    return Div(
        Span(number, cls="font-mono text-xs tracking-widest text-accent"),
        Heading(3, title, cls="mt-6 mb-3"),
        P(body, cls="text-sm leading-relaxed text-ink-muted"),
        cls="rounded-2xl border border-line bg-white p-7 h-full",
    )


def Navbar(current_path, lang):
    links = nav_items(lang)
    return Nav(
        Div(
            A(Span("◆", cls="mr-2 text-accent"), SITE_NAME, href="/",
              cls="font-medium tracking-tight text-ink hover:text-accent"),
            Ul(*[Li(A(label, href=href,
                      cls=f"text-sm transition-colors {'text-accent font-medium' if current_path == href else 'text-ink-muted hover:text-accent'}"))
                 for label, href in links], cls="hidden lg:flex items-center gap-7"),
            Div(
                *[A(code.upper(), href=f"/set-lang/{code}",
                    cls=f"text-xs font-mono {'text-accent font-semibold' if code == lang else 'text-ink-dim hover:text-accent'}")
                  for code in LANGUAGES],
                cls="hidden lg:flex items-center gap-2",
            ),
            Button("☰", type="button", aria_label=t("menu", lang),
                   onclick="document.getElementById('mobile-nav').classList.toggle('hidden')",
                   cls="lg:hidden rounded-full border border-line px-3 py-1 text-xl"),
            cls="mx-auto flex h-16 max-w-7xl items-center justify-between gap-5 px-5 md:px-6",
        ),
        Div(
            *[A(label, href=href, cls="block px-5 py-3 text-ink hover:text-accent") for label, href in links],
            Div(*[A(info["native"], href=f"/set-lang/{code}",
                    cls=f"text-xs {'text-accent font-semibold' if code == lang else 'text-ink-muted'}")
                  for code, info in LANGUAGES.items()], cls="flex gap-4 px-5 py-4"),
            id="mobile-nav", cls="hidden border-t border-line bg-white lg:hidden",
        ),
        cls="sticky top-0 z-50 border-b border-line bg-bg/95 backdrop-blur-md",
    )


def Footer_(lang):
    return Footer(
        Div(
            Div(
                Div(
                    A("◆  " + SITE_NAME, href="/", cls="text-lg font-medium text-ink hover:text-accent"),
                    P(t("footer_tagline", lang), cls="mt-4 max-w-sm text-sm leading-relaxed text-ink-muted"),
                    cls="md:col-span-2",
                ),
                Div(Eyebrow(t("footer_explore", lang)),
                    *[A(label, href=href, cls="block mt-3 text-sm text-ink-muted hover:text-accent") for label, href in nav_items(lang)]),
                Div(Eyebrow(t("footer_company", lang)),
                    P(LEGAL_NAME, cls="mt-3 text-sm text-ink"),
                    P(f"{t('company_number', lang)} {COMPANY_NUMBER}", cls="mt-1 text-sm text-ink-muted"),
                    P(REGISTERED_ADDRESS, cls="mt-2 text-sm leading-relaxed text-ink-muted"),
                    A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", cls="mt-3 block text-sm text-accent hover:underline")),
                cls="grid gap-10 md:grid-cols-4",
            ),
            Div(f"© {datetime.now().year} {LEGAL_NAME}", cls="mt-12 border-t border-line pt-6 text-xs text-ink-dim"),
            cls="mx-auto max-w-7xl px-5 md:px-6",
        ),
        cls="border-t border-line bg-bg-elevated py-14",
    )


def page(title, current_path, *content, lang="en", body_extra=None):
    head = Head(
        Meta(charset="utf-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1"),
        Meta(name="description", content=t("meta_description", lang)),
        Link(rel="icon", href="/static/favicon.svg", type="image/svg+xml"),
        Title(f"{title} · {SITE_NAME}"),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"),
        Script(src="https://cdn.tailwindcss.com"),
        Script(NotStr(TAILWIND_CONFIG)),
        Link(rel="stylesheet", href="/static/site.css"),
    )
    return Html(
        head,
        Body(Navbar(current_path, lang), Main(*content, cls="min-h-screen"), Footer_(lang),
             *(body_extra or []), cls="bg-bg font-sans text-ink antialiased"),
        lang=lang,
    )


def Hero(lang):
    return Section(
        Div(id="three-hero", cls="absolute inset-0 opacity-35 pointer-events-none"),
        Div(cls="absolute inset-0 bg-gradient-to-b from-bg/60 via-bg/30 to-bg pointer-events-none"),
        Div(
            Eyebrow(t("hero_eyebrow", lang)),
            Heading(1, t("hero_heading", lang), cls="mt-6 max-w-5xl"),
            P(t("hero_lede", lang), cls="mt-7 max-w-2xl text-lg md:text-xl leading-relaxed text-ink-muted"),
            Div(Button_(t("hero_primary", lang), "/advisory"),
                Button_(t("hero_secondary", lang), "/platform", primary=False),
                cls="mt-9 flex flex-wrap gap-3"),
            cls="relative z-10 mx-auto flex min-h-[72vh] max-w-7xl flex-col justify-center px-5 py-20 md:px-6",
        ),
        cls="relative overflow-hidden bg-bg",
    )


def CTASection(lang):
    return Section_(
        Eyebrow(t("cta_eyebrow", lang)),
        Heading(2, t("cta_heading", lang), cls="mt-4 max-w-3xl"),
        P(t("cta_body", lang), cls="mt-5 max-w-2xl text-lg leading-relaxed text-ink-muted"),
        Div(Button_(t("cta_button", lang), "/contact"), cls="mt-8"),
        cls="border-y border-line bg-bg-elevated/70",
    )
