"""Public route and copy checks for the advisory site."""

import unittest

import httpx

from app import app
from utils.i18n import LANGUAGES, TRANSLATIONS


class SiteTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://testserver",
        )

    async def asyncTearDown(self):
        await self.client.aclose()

    async def test_public_pages_use_advisory_identity(self):
        for path in ("/", "/advisory", "/sectors", "/platform", "/team", "/contact"):
            with self.subTest(path=path):
                response = await self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertIn("Curonia Capital Ltd", response.text)
                self.assertIn("14537690", response.text)
                self.assertIn("155 Minories Street", response.text)
                self.assertIn('href="/platform"', response.text)
                self.assertNotIn("AAA Enterprises", response.text)
                self.assertNotIn("€50M", response.text)

        team = (await self.client.get("/team")).text
        self.assertIn("Julian Kaljuvee", team)
        self.assertIn("Igors Plahins", team)
        self.assertNotIn("Aurimas Martišauskas", team)
        self.assertNotIn("Matas Jakubėlis", team)
        self.assertNotIn("Ieva Belickaitė", team)

        platform = (await self.client.get("/platform")).text
        self.assertIn("LiquidRound", platform)
        self.assertIn("https://liquidround.com/", platform)

    async def test_language_switch_keeps_current_page(self):
        await self.client.get("/platform")
        for code in LANGUAGES:
            with self.subTest(lang=code):
                response = await self.client.get(f"/set-lang/{code}")
                self.assertEqual(response.status_code, 303)
                self.assertEqual(response.headers["location"], "/platform")
                page = await self.client.get("/platform")
                self.assertIn(f'<html lang="{code}">', page.text)
                self.assertIn(TRANSLATIONS["platform_heading"][code], page.text)

    async def test_old_urls_redirect_to_current_pages(self):
        for old, new in (
            ("/thesis", "/advisory"),
            ("/track-record", "/advisory"),
            ("/sectors/healthcare", "/sectors"),
        ):
            with self.subTest(path=old):
                response = await self.client.get(old)
                self.assertEqual(response.status_code, 308)
                self.assertEqual(response.headers["location"], new)


if __name__ == "__main__":
    unittest.main()
