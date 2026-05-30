"""
Curonia Capital — multipage FastHTML landing site.

Baltic growth equity fund: AI-powered transformation of founder-led SMEs.
Part of AAA Enterprises. Content lives in content/*.py; routes are thin
composition over components.py.
"""

from fasthtml.common import (
    fast_app, serve, Div, Span, A, P, Ul, Li, Section, Article, Header, Table,
    Thead, Tbody, Tr, Th, Td, NotStr, Script, Style, H1, H2, H3, H4, Button,
)

from components import (
    page, Hero, Pillar, MetricTile, CTASection, NewsSection, Section_,
    Heading, Eyebrow, Pill, Button_, LinkedInIcon,
    CONTACT_EMAIL, LINKEDIN_URL,
)
from content.team import TEAM
from content import news as news_mod

news_mod.start_background_refresh()

app, rt = fast_app(live=False, static_path=".", pico=False)


# ---------- / Home ----------

@rt("/")
def home():
    pillars = [
        ("01", "AI playbook", "Our in-house engineering team deploys AI to digitise workflows, automate operations and build proprietary data infrastructure at every portfolio company — no external consultants, faster execution."),
        ("02", "Founder partnership", "Baltic founders aged 55–65 have built strong businesses without institutional capital. They want to professionalise and grow, not exit outright. Growth equity with minority stake lets them retain control."),
        ("03", "Selective consolidation", "The Baltic mid-market is structurally fragmented — hundreds of €2–20M revenue businesses with no scaled regional competitor. We consolidate through bolt-on acquisitions on a unified technology platform."),
        ("04", "Visible exit", "For each platform we underwrite, we map the credible acquirer set — regional strategics, larger PE consolidators, international corporates — before committing capital."),
    ]

    return page(
        "Baltic growth equity, AI-powered",
        "/",
        Hero(),

        # Fund overview
        Section_(
            Div(
                Eyebrow("Fund overview"),
                Heading(2, "Growth equity for the Baltic transformation.", cls="mt-4 max-w-4xl"),
                P(
                    "A €50M growth equity fund partnering with founder-led and family-owned Baltic SMEs "
                    "to accelerate expansion through AI-driven growth and selective consolidation.",
                    cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed",
                ),
                cls="mb-14",
            ),
            Div(
                MetricTile("€50", "M", "Fund size"),
                MetricTile("€2–5", "M", "Investment per company, up to €8M with follow-on"),
                MetricTile("5–10", "", "Expected number of investments"),
                MetricTile("25", "%", "Target IRR"),
                MetricTile("7+2", "yr", "Fund term"),
                MetricTile("LT LV EE", "", "Geography — Lithuania, Latvia, Estonia"),
                cls="grid md:grid-cols-3 lg:grid-cols-6 gap-4",
            ),
            cls="border-b border-line",
        ),

        # Thesis pillars
        Section_(
            Div(
                Eyebrow("Investment thesis"),
                Heading(2, "AI-led organic growth, reinforced by selective consolidation.", cls="mt-4 max-w-4xl"),
                P(
                    "We target founder-led and family-owned SMEs with €2M–€20M revenue, proven models, "
                    "and clear AI-enabled value creation potential. Unlike any other Baltic PE fund, "
                    "we build and deploy AI ourselves.",
                    cls="mt-5 text-ink-muted text-lg max-w-3xl",
                ),
                cls="mb-14",
            ),
            Div(
                *[Pillar(n, t, b) for n, t, b in pillars],
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
        ),

        # Sector focus
        Section_(
            Div(
                Eyebrow("Where we invest"),
                Heading(2, "Four sectors we can transform with AI.", cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                _sector_link("Healthcare", "Dental clinics, dermatology & aesthetics, facility-based healthcare and medtech — fragmented single-site practices ripe for platform consolidation.", "/sectors/healthcare"),
                _sector_link("Education & EdTech", "K-12 and private schools, tutoring platforms, vocational training and digital learning — fragmented chains at sub-€10M scale.", "/sectors/education"),
                _sector_link("Technology", "Vertical SaaS, fintech, cybersecurity, data infrastructure, IoT and managed services — software and data plays with sticky workflows.", "/sectors/technology"),
                _sector_link("Services", "Professional services, engineering, staffing, testing & inspection — fragmented service verticals we can transform with AI.", "/sectors/services"),
                cls="grid md:grid-cols-2 gap-5",
            ),
            cls="border-y border-line bg-bg-elevated/40",
        ),

        # Track record teaser
        Section_(
            Div(
                Eyebrow("Track record"),
                Heading(2, "Built on a platform with €3B+ in group assets.", cls="mt-4 max-w-3xl"),
                P(
                    "Curonia Capital is part of AAA Enterprises, an international group of licensed financial companies "
                    "operating since 1993. Our team has direct operating experience from 1 Asset Management's "
                    "€750M+ AUM portfolio — including the Pet Care Growth Fund and the Education Infrastructure Fund.",
                    cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed",
                ),
                Button_("See the full track record", href="/track-record", primary=False, cls="mt-8"),
                cls="mb-14",
            ),
            Div(
                _track_tile("~€3B", "Total group assets managed and administered"),
                _track_tile("€750M+", "AUM at 1 Asset Management across 12+ funds"),
                _track_tile("100+", "Professionals across the AAA Enterprises group"),
                _track_tile("Since 1993", "Operating across Europe, regulated by Bank of Lithuania"),
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
        ),

        # Team teaser
        Section_(
            Div(
                Eyebrow("Team"),
                Heading(2, "Partners with PE, VC, investment banking, AI engineering, and operational transformation experience.", cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                *[_team_card_compact(m) for m in TEAM],
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
            Div(
                Button_("Meet the full team", href="/team", primary=False),
                cls="mt-10",
            ),
            cls="border-t border-line",
        ),

        NewsSection(
            category="home",
            title="Market intelligence.",
            subtitle="A rolling mix of private equity, financial markets and Baltic economy news from public PE and financial feeds. Refreshed hourly.",
        ),

        CTASection(),

        body_extra=[
            Script(src="/static/three-hero.js", type="module"),
        ],
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
def thesis():
    pillars = [
        ("01", "AI playbook", "Our DeployCo model applies AI to traditional businesses where it moves the needle. We screen for high volume document or call workflows, structured data, and repetitive admin. Our in-house engineering team deploys models within months. Healthcare diagnostics, ICT support, accounting and HR services fit; hands-on trades do not."),
        ("02", "Founder partnership", "Baltic founders, aged 55 to 65, built businesses without institutional capital and lack the balance sheet to fund the next growth phase. Many want to retain majority, professionalise the company, and exit in 3 to 7 years on a planned timeline. Growth equity (minority stake, founder stays operating, capital for AI and expansion) is culturally and commercially the right structure."),
        ("03", "Selective consolidation", "The Baltic mid market is structurally fragmented, with hundreds of €2 to 20M revenue businesses and no scaled regional competitor. Where bolt-ons sharpen the platform, we consolidate. We then, if necessary, internationalise into Nordics, Poland and CEE through M&A or organic expansion, building the regional champion that strategics will pay for at exit."),
        ("04", "Visible exit", "For each platform we underwrite, we map the credible acquirer set (regional strategics, larger PE consolidators, international corporates with Baltic ambitions) before committing capital. A pan-Baltic, AI-enhanced platform attracts multiple competing buyers at exit, with strategics paying for both the regional footprint and the embedded technology."),
    ]

    value_creation = [
        ("Digitise", "Replace manual workflows with cloud-native systems deployed by our in-house AI engineering team."),
        ("Automate operations", "AI-driven scheduling, billing, HR analytics, reporting and compliance automation across all portfolio companies."),
        ("Consolidate data", "Build proprietary data infrastructure — creating defensible analytics moats no competitor can replicate."),
        ("Scale pan-Baltic", "Bolt-on acquisitions across Baltics on unified technology platform, leveraging sector sourcing networks."),
    ]

    return page(
        "Investment Thesis",
        "/thesis",
        Section_(
            Eyebrow("Investment thesis"),
            Heading(1, "AI-led organic growth, reinforced by selective consolidation.", cls="mt-5 max-w-5xl"),
            P(
                "Curonia Capital is a €50M Growth Equity Fund partnering with founder-led and family-owned Baltic SMEs "
                "to accelerate expansion through AI-driven growth and selective add-ons. The fund is sector-agnostic, "
                "with a primary focus on Education, Healthcare, and Technology, targeting companies with proven models, "
                "recurring revenue, AI-enabled value creation potential, and clear exit pathways.",
                cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed",
            ),
            cls="pt-24",
        ),
        Section_(
            Div(
                Eyebrow("Four pillars"),
                Heading(2, "How we invest.", cls="mt-4"),
                cls="mb-14",
            ),
            Div(*[_thesis_row(n, t, b) for n, t, b in pillars], cls="divide-y divide-line border-y border-line"),
        ),
        Section_(
            Div(
                Eyebrow("Value creation"),
                Heading(2, "Technology enablement at every portfolio company.", cls="mt-4 max-w-4xl"),
                P(
                    "Unlike any other Baltic PE fund, we build and deploy AI ourselves. "
                    "Julian Kaljuvee (Blackstone / Microsoft AI) + the in-house AI engineer transform every portfolio company directly — "
                    "no external consultants, faster execution.",
                    cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed",
                ),
                cls="mb-14",
            ),
            Div(
                *[Div(
                    Div(
                        Span(f"0{i+1}", cls="font-mono text-xs tracking-widest text-accent"),
                        cls="mb-3",
                    ),
                    Heading(3, title, cls="mb-2"),
                    P(body, cls="text-ink-muted text-sm leading-relaxed"),
                    cls="p-7 rounded-2xl bg-white border border-line",
                ) for i, (title, body) in enumerate(value_creation)],
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
            cls="border-t border-line bg-bg-elevated/40",
        ),
        Section_(
            Div(
                Eyebrow("Entry and exit"),
                Heading(2, "Disciplined valuation framework.", cls="mt-4 max-w-4xl"),
                cls="mb-14",
            ),
            Div(
                MetricTile("3–6×", "EBITDA", "Cash-generative platforms · Entry"),
                MetricTile("10–14×", "EBITDA", "Pan-Baltic platform · Exit"),
                MetricTile("3–5×", "ARR", "SaaS / vertical software · Entry"),
                MetricTile("6–9×", "ARR", "AI-native, sticky platform · Exit"),
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
        ),
        CTASection(),
        body_extra=[Script(src="/static/three-hero.js", type="module")],
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

SECTORS = {
    "healthcare": {
        "title": "Healthcare",
        "eyebrow": "Healthcare",
        "headline": "Facility-based healthcare and medtech — thousands of fragmented single-site practices.",
        "lede": "The Lithuanian dental market is dominated by founder-led practices with no brand, no digital marketing and limited cross-sell. European medical aesthetics is growing at 12% CAGR with no consolidated Baltic platform. We invest in multi-site clinics and shift the revenue mix toward higher-margin procedures.",
        "pillars": [
            ("Dental clinics", "Grow multi-site dental networks, shift revenue toward aesthetic dentistry — whitening, aligners, veneers, implants. Centralise procurement, layer AI dental imaging across all sites."),
            ("Dermatology & aesthetics", "Consolidate profitable clinics across Vilnius, Kaunas and Klaipėda onto one brand, one booking system and shared procurement. Deploy AI skin diagnostics as a front-door tool."),
            ("Medical tourism", "Package aesthetic dental and skin procedures at 3–5× cost advantage vs Nordics/UK. Proven model in Baltic plastic surgery."),
        ],
        "register": ["Facility-based", "AI diagnostics", "Pan-Baltic platform"],
        "news_key": "healthcare",
        "news_title": "Healthcare PE signal.",
        "news_sub": "Private equity activity in European healthcare, dental and medtech sectors.",
    },
    "education": {
        "title": "Education & EdTech",
        "eyebrow": "Education & EdTech",
        "headline": "Founder-owned schools, training providers and digital learning platforms.",
        "lede": "The global online tutoring market is shifting toward AI-driven personalisation. Lithuania's school-age tutoring market is fragmented across individual tutors and small platforms. We invest in online tutoring platforms and vocational training providers, deploying AI content layers and scaling across Baltic and diaspora markets.",
        "pillars": [
            ("Online tutoring (K-12)", "Consolidate Lithuanian tutoring platforms onto one stack. Deploy AI content layer to replace 1-on-1 tutor hours with AI study programmes. Convert take-rate to SaaS subscriptions."),
            ("Vocational & skills training", "Invest in certified schools across beauty, wellness, IT — aggregate onto one accredited platform. Scale through state-funded programmes and cross-border expansion."),
            ("School infrastructure", "Leverage 1AM Education Infrastructure Fund relationships with Šiaurės Licėjus, Erudito Licėjus, Saulės Gojus and Vilnius International School."),
        ],
        "register": ["AI content", "B2B + B2G channels", "Cross-border"],
        "news_key": "education",
        "news_title": "Education & EdTech signal.",
        "news_sub": "PE activity and trends in European education, edtech and training sectors.",
    },
    "technology": {
        "title": "Technology & Digital Infrastructure",
        "eyebrow": "Technology",
        "headline": "Software, data and infrastructure plays with sticky workflows and resilience to AI.",
        "lede": "We invest in vertical SaaS, fintech, cybersecurity, data analytics and managed IT services. The focus is on businesses with proprietary data moats, high switching costs, and the ability to embed AI directly into their product — making them more valuable, not more vulnerable.",
        "pillars": [
            ("Vertical SaaS & platform software", "ERP, insurtech, payment rails and industry-specific software with deep workflow integration and high retention."),
            ("IT services & managed services", "MSPs, hosting and integrators across HR, ERP and logistics — consolidate a vertical and internationalise with AI accelerating code, data and ticketing migration."),
            ("Cybersecurity & data infrastructure", "Data, analytics and AI infrastructure plays with defensible moats. Digital infra, data centres and telecommunications."),
        ],
        "register": ["Sticky workflows", "Proprietary data", "AI-resilient"],
        "news_key": "technology",
        "news_title": "Technology PE signal.",
        "news_sub": "Private equity activity in European SaaS, IT services and digital infrastructure.",
    },
    "services": {
        "title": "Tech-Enabled Services & B2B/C",
        "eyebrow": "Services",
        "headline": "Fragmented service verticals we can transform with AI.",
        "lede": "Industrial, technical and professional services across the Baltics — each with hundreds of small operators, no regional champion, and high potential for AI-driven operational improvement. We screen for businesses where AI can automate scheduling, dispatch, compliance, customer communication and back-office at scale.",
        "pillars": [
            ("Professional services", "Legal, audit, advisory, accounting — fragmented practices we can platform with shared AI tooling for document processing, compliance and client management."),
            ("Engineering & construction", "Testing, inspection, certification and M&E services with repeatable workflows, regulatory demand and cross-border expansion potential."),
            ("Staffing & workforce services", "Training, recruitment and workforce management — sectors where AI can automate matching, scheduling and credential verification at scale."),
        ],
        "register": ["AI automation", "Workforce uplift", "Sector agnostic"],
        "news_key": "services",
        "news_title": "Business services PE signal.",
        "news_sub": "Private equity activity in European professional and business services.",
    },
}


SECTOR_NEWS = {
    "healthcare": ("healthcare", "Healthcare PE signal.", "Private equity activity in European healthcare, dental and medtech sectors."),
    "education": ("education", "Education & EdTech signal.", "PE activity and trends in European education, edtech and training sectors."),
    "technology": ("technology", "Technology PE signal.", "Private equity activity in European SaaS, IT services and digital infrastructure."),
    "services": ("services", "Business services PE signal.", "Private equity activity in European professional and business services."),
}


def _sector_page(slug):
    s = SECTORS[slug]
    news_key, news_title, news_sub = SECTOR_NEWS[slug]

    return page(
        s["title"],
        f"/sectors/{slug}",
        Section_(
            Eyebrow(s["eyebrow"]),
            Heading(1, s["headline"], cls="mt-5 max-w-5xl"),
            P(s["lede"], cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed"),
            Div(
                *[Pill(r) for r in s["register"]],
                cls="mt-10 flex flex-wrap gap-2",
            ),
            cls="pt-24",
        ),
        Section_(
            Div(
                Eyebrow("Where we focus"),
                Heading(2, "Three focal points in this sector.", cls="mt-4"),
                cls="mb-14",
            ),
            Div(
                *[Pillar(f"0{i+1}", t, b) for i, (t, b) in enumerate(s["pillars"])],
                cls="grid md:grid-cols-3 gap-5",
            ),
        ),
        NewsSection(category=news_key, title=news_title, subtitle=news_sub),
        CTASection(),
    )


@rt("/sectors/healthcare")
def sec_healthcare():
    return _sector_page("healthcare")


@rt("/sectors/education")
def sec_education():
    return _sector_page("education")


@rt("/sectors/technology")
def sec_technology():
    return _sector_page("technology")


@rt("/sectors/services")
def sec_services():
    return _sector_page("services")


# ---------- /track-record ----------

@rt("/track-record")
def track_record():
    group_entities = [
        ("1 Asset Management", "Licensed asset manager with €750M+ AUM and 12+ niche investment strategies across real estate, private debt, education infrastructure and pet care.", "€750M+ AUM"),
        ("RATO Bank", "Specialised Lithuanian bank focused on lending, deposits, and modern financial services for individuals and businesses.", "€120M+ deposits"),
        ("Orion Securities", "Leading Lithuanian investment bank providing capital markets services, including brokerage, corporate finance, venture capital, and wealth management.", "€2.1B+ custody"),
        ("Taurus Wealth", "Lithuania-based investment firm focused on sustainable investing and long-term value creation through strategic investments.", "€95M+ AUM"),
        ("AAA Law", "Lithuanian business law firm advising companies and investors on corporate, IP, regulatory and dispute resolution matters.", "100+ professionals"),
    ]

    fund_precedents = [
        {
            "name": "Pet Care Growth Fund",
            "manager": "1 Asset Management",
            "description": "Built the largest veterinary clinic chain in the Baltics (~€15M revenue) via acquisitions and greenfield development. Active in 5 countries (LT, LV, EE, PL, RO). Leading regional consolidator alongside LuxVet / Cornerstone & OaktreeLuxVet: ~100 clinics, ~€100M revenue.",
            "tags": ["Veterinary", "Roll-up", "5 countries"],
        },
        {
            "name": "Education Infrastructure Fund",
            "manager": "1 Asset Management",
            "description": "Invests in private schools and education-related infrastructure in Lithuania and other Baltic countries. Active investments in Šiaurės Licėjus, Erudito Licėjus, Saulės Gojus and Vilnius International School. B2B channel to ~2,000 enrolled families.",
            "tags": ["Education", "Infrastructure", "Lithuania"],
        },
        {
            "name": "Broader 1AM portfolio",
            "manager": "1 Asset Management",
            "description": "Luxury hotels (Grand Hotel Vilnius), student housing, airport hotels, timberland, private debt, bonds, pre-IPO fund, listed equity (global). Trusted by Swedbank, SEB, Citadele, Santander, European Investment Fund.",
            "tags": ["Multi-strategy", "Institutional LPs", "12+ funds"],
        },
    ]

    return page(
        "Track Record",
        "/track-record",
        Section_(
            Eyebrow("Track record"),
            Heading(1, "Part of AAA Enterprises — ~€3B in group assets.", cls="mt-5 max-w-5xl"),
            P(
                "Curonia Capital is backed by AAA Enterprises, an international group of licensed financial companies "
                "operating since 1993 across Luxembourg, Lithuania, North America and Dubai. The group encompasses banking, "
                "asset management, investment banking, brokerage, family office and venture capital.",
                cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed",
            ),
            cls="pt-24",
        ),

        # Group metrics
        Section_(
            Div(
                Eyebrow("Group at a glance"),
                Heading(2, "AAA Enterprises — key metrics.", cls="mt-4"),
                cls="mb-14",
            ),
            Div(
                MetricTile("~€3", "B", "Total group assets managed and administered"),
                MetricTile("6,000", "+", "Active investors across the group"),
                MetricTile("100", "+", "Professionals across AAA Enterprises"),
                MetricTile("1993", "", "Year of founding — 30+ years of operations"),
                cls="grid md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
            cls="border-b border-line",
        ),

        # Group entities
        Section_(
            Div(
                Eyebrow("Group companies"),
                Heading(2, "A platform of licensed financial companies.", cls="mt-4 max-w-4xl"),
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

        # Fund precedents
        Section_(
            Div(
                Eyebrow("Fund precedents"),
                Heading(2, "Where our team has operated.", cls="mt-4 max-w-3xl"),
                P(
                    "Direct operating experience from 1 Asset Management's portfolio — "
                    "the track record that anchors how we invest and transform portfolio companies.",
                    cls="mt-5 text-ink-muted text-lg max-w-3xl leading-relaxed",
                ),
                cls="mb-14",
            ),
            Div(
                *[Div(
                    Div(
                        Heading(3, p["name"], cls="mb-1"),
                        P(p["manager"], cls="text-accent text-sm font-mono mb-4"),
                    ),
                    P(p["description"], cls="text-ink-muted text-sm leading-relaxed mb-5"),
                    Div(*[Pill(t) for t in p["tags"]], cls="flex flex-wrap gap-2"),
                    cls="p-7 rounded-2xl bg-white border border-line",
                ) for p in fund_precedents],
                cls="grid md:grid-cols-3 gap-5",
            ),
            cls="border-t border-line bg-bg-elevated/40",
        ),

        NewsSection(
            category="pe",
            title="Private equity signal.",
            subtitle="Latest from PE industry, Baltic M&A and financial markets.",
        ),

        CTASection(),
    )


# ---------- /team ----------

@rt("/team")
def team():
    return page(
        "Team",
        "/team",
        Section_(
            Eyebrow("Team"),
            Heading(1, "Partners with PE, VC, investment banking, AI engineering, and operational transformation experience.", cls="mt-5 max-w-4xl"),
            P(
                "A team that has built and exited Baltic platform companies, deployed production AI at global scale, "
                "and executed >€250M in M&A transactions. We keep the partnership deliberately small and the "
                "portfolio engagement deliberately deep.",
                cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed",
            ),
            cls="pt-24",
        ),
        Section_(
            Div(
                *[_member_card(m) for m in TEAM],
                cls="grid md:grid-cols-2 gap-5",
            ),
        ),
        CTASection(
            headline="Building a Baltic platform?",
            body="If you are a founder running a profitable Baltic SME in healthcare, education, technology or services — and want a growth equity partner who deploys AI directly — tell us.",
            cta_label="Write to us",
        ),
    )


def _member_card(m):
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
        P(m["bio"], cls="text-ink-muted leading-relaxed"),
        cls="p-8 rounded-2xl bg-white border border-line",
    )


# ---------- /contact ----------

@rt("/contact")
def contact():
    return page(
        "Contact",
        "/contact",
        Section_(
            Eyebrow("Contact"),
            Heading(1, "Tell us about your business.", cls="mt-5 max-w-4xl"),
            P(
                "Curonia Capital partners with founder-led Baltic SMEs in healthcare, education, technology and services. "
                "€2–5M cheques, growth equity. Send us a note — we'll tell you if we can help.",
                cls="mt-8 text-xl text-ink-muted max-w-3xl leading-relaxed",
            ),
            cls="pt-24",
        ),
        Section_(
            Div(
                Div(
                    Eyebrow("Write to us"),
                    A(CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}",
                      cls="mt-4 block text-xl md:text-2xl font-medium text-ink hover:text-accent break-all transition-colors"),
                    P(
                        "A short note on what your business does, your revenue, where you are based "
                        "and what you are looking for is enough to start a conversation.",
                        cls="mt-4 text-ink-muted leading-relaxed text-sm",
                    ),
                    Div(
                        Button_("Email " + CONTACT_EMAIL, href=f"mailto:{CONTACT_EMAIL}", primary=True),
                        cls="mt-8",
                    ),
                    cls="p-10 rounded-2xl bg-white border border-line",
                ),
                Div(
                    Div(
                        H3("Office", cls="text-sm font-mono tracking-widest uppercase text-ink-muted mb-3"),
                        P("Curonia Capital", cls="text-ink"),
                        P("Part of AAA Enterprises", cls="text-ink-muted"),
                        P("Upės str. 21", cls="text-ink-muted"),
                        P("Vilnius, Lithuania", cls="text-ink-muted"),
                        cls="mb-10",
                    ),
                    Div(
                        H3("Parent company", cls="text-sm font-mono tracking-widest uppercase text-ink-muted mb-3"),
                        A("AAA Enterprises", href="https://www.aaaenterprises.lt/en", target="_blank", cls="block text-ink hover:text-accent mb-2"),
                        A("1 Asset Management", href="https://www.1am.lt", target="_blank", cls="block text-ink hover:text-accent mb-2"),
                    ),
                    cls="p-10 rounded-2xl bg-white border border-line",
                ),
                cls="grid md:grid-cols-2 gap-5",
            ),
        ),
    )


if __name__ == "__main__":
    serve()
