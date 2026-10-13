"""Public route, language, SEO and copy checks for the advisory site."""

import unittest

import httpx

from app import app
from components import PAGES, url_for
from utils.i18n import LANGUAGES, TRANSLATIONS


class SiteTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://testserver",
        )

    async def asyncTearDown(self):
        await self.client.aclose()

    async def test_every_page_renders_in_every_language(self):
        for code in LANGUAGES:
            for key in PAGES:
                path = url_for(code, key)
                with self.subTest(path=path):
                    response = await self.client.get(path)
                    self.assertEqual(response.status_code, 200)
                    text = response.text
                    self.assertIn(f'<html lang="{code}">', text)
                    self.assertIn("Curonia Capital Ltd", text)
                    self.assertIn("14537690", text)
                    self.assertIn("155 Minories Street", text)
                    self.assertIn(f'rel="canonical" href="https://curoniacapital.com{path}"', text)
                    for alt in LANGUAGES:
                        self.assertIn(f'hreflang="{alt}"', text)
                    self.assertIn('hreflang="x-default"', text)
                    self.assertIn("application/ld+json", text)
                    self.assertNotIn("\u2014", text, "em dash in rendered page")
                    self.assertNotIn("cdn.tailwindcss.com", text)
                    self.assertNotIn("three.module.js", text)
                    self.assertNotIn("AAA Enterprises", text)
                    self.assertNotIn("€50M", text)

    async def test_team_and_intelligence_content(self):
        team = (await self.client.get("/team")).text
        self.assertIn("Julian Kaljuvee", team)
        self.assertIn("Igors Plahins", team)
        self.assertIn("https://www.linkedin.com/in/juliankaljuvee/", team)
        self.assertNotIn("Aurimas Martišauskas", team)

        intelligence = (await self.client.get("/intelligence")).text
        self.assertIn("LiquidRound", intelligence)
        self.assertIn('href="https://liquidround.com/"', intelligence)
        self.assertIn('rel="noopener noreferrer"', intelligence)
        self.assertIn("LiquidRound, Curonia's proprietary AI platform", intelligence)

        sectors = (await self.client.get("/sectors")).text
        self.assertEqual(sectors.count("<h3>"), 6)
        self.assertIn(TRANSLATIONS["sector_6_title"]["en"], sectors)

    async def test_translations_are_complete(self):
        for key, values in TRANSLATIONS.items():
            for code in LANGUAGES:
                with self.subTest(key=key, lang=code):
                    self.assertTrue(values.get(code, "").strip())
                    self.assertNotIn("\u2014", values[code])

    async def test_language_switch_follows_referring_page(self):
        for code in LANGUAGES:
            with self.subTest(lang=code):
                response = await self.client.get(
                    f"/set-lang/{code}", headers={"referer": "http://testserver/lv/sectors"}
                )
                self.assertEqual(response.status_code, 303)
                self.assertEqual(response.headers["location"], url_for(code, "sectors"))
        response = await self.client.get("/set-lang/lt", headers={"referer": "https://elsewhere.example/team"})
        self.assertEqual(response.headers["location"], "/lt/")

    async def test_redirects(self):
        for old, new in (
            ("/platform", "/intelligence"),
            ("/lt/platform", "/lt/intelligence"),
            ("/lv", "/lv/"),
            ("/thesis", "/advisory"),
            ("/track-record", "/advisory"),
            ("/sectors/healthcare", "/sectors"),
        ):
            with self.subTest(path=old):
                response = await self.client.get(old)
                self.assertEqual(response.status_code, 308)
                self.assertEqual(response.headers["location"], new)

    async def test_robots_and_sitemap(self):
        robots = await self.client.get("/robots.txt")
        self.assertEqual(robots.status_code, 200)
        self.assertTrue(robots.headers["content-type"].startswith("text/plain"))
        self.assertIn("Sitemap: https://curoniacapital.com/sitemap.xml", robots.text)

        sitemap = await self.client.get("/sitemap.xml")
        self.assertEqual(sitemap.status_code, 200)
        self.assertEqual(sitemap.headers["content-type"], "application/xml")
        for code in LANGUAGES:
            for key in PAGES:
                self.assertIn(f"<loc>https://curoniacapital.com{url_for(code, key)}</loc>", sitemap.text)

    async def test_not_found_and_static_safety(self):
        missing = await self.client.get("/et/no-such-page")
        self.assertEqual(missing.status_code, 404)
        self.assertIn('<html lang="et">', missing.text)
        self.assertIn('content="noindex"', missing.text)

        for path in ("/requirements.txt", "/AGENTS.md", "/static/../app.py"):
            with self.subTest(path=path):
                self.assertNotEqual((await self.client.get(path)).status_code, 200)

        css = await self.client.get("/static/site.css")
        self.assertEqual(css.status_code, 200)
        self.assertIn("immutable", css.headers["cache-control"])


if __name__ == "__main__":
    unittest.main()
