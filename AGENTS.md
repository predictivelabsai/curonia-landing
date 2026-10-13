# Repository Guidelines

## Project Structure & Module Organization

`main.py` imports the FastHTML app from `app.py`, where page routes, redirects, `robots.txt`, `sitemap.xml` and the 404 handler live. Shared layout, the brand lockup, SEO metadata, JSON-LD and decorative SVGs live in `components.py`. Edit people in `content/team.py` (portraits go in `static/team/`); keep translation keys and the EN/LT/LV/ET catalogue in `utils/i18n.py`. Browser assets are in `static/`: `site.css` (all styles, no framework), `site.js` (small progressive enhancement), `favicon.svg`, `apple-touch-icon.png`, `og-image.png` and logo files in `static/brand/`. Brand rules are in `docs/brand.md`.

Languages are routed by URL: English at the root (`/advisory`), others under a prefix (`/lt/advisory`). Pages are declared in `PAGES` in `components.py` and registered for every language in `app.py`. Only the `static/` folder is served as files.

## Build, Test, and Development Commands

- `python -m venv .venv` then activate it (`.venv\Scripts\Activate.ps1` on Windows, `source .venv/bin/activate` elsewhere) to create a local environment.
- `pip install -r requirements.txt` installs FastHTML, Uvicorn and HTTPX.
- `uvicorn main:app --port 5001` runs the site locally at `http://127.0.0.1:5001`. Static URLs carry a content hash, so CSS and JS edits show on the next page load.
- `docker compose up --build` builds and runs the container on port 5001.
- `python -m unittest discover -s tests` runs route, language, SEO and copy checks.
- `python -m compileall -q main.py app.py components.py content utils` checks Python syntax.

Set `CURONIA_SITE_URL` if the public domain differs from `https://curoniacapital.com` (used for canonical, hreflang, Open Graph and the sitemap).

## Coding Style & Naming Conventions

Use four-space indentation and follow the existing Python style: `snake_case` for routes, helpers and translation keys; `PascalCase` for reusable FastHTML components; uppercase names for module constants. Keep routes focused on assembling components. Keep CSS in `static/site.css` using the tokens at its top, and browser behaviour in `static/site.js`; content must work without JavaScript. Copy uses British English and no em dashes in any language; text wrapped in `*asterisks*` renders as emphasis.

## Testing Guidelines

Route tests use Python's built-in `unittest` and HTTPX's ASGI transport. Run the tests and syntax check above, then open affected routes in a browser at desktop and mobile widths. For copy or navigation changes, check all four languages using the language switcher. Place new tests in `tests/` and name files `test_*.py`.

## Commit & Pull Request Guidelines

Use short, imperative commit subjects such as `Add i18n support with EN/LT/LV/ET language switcher`. Keep each commit focused and describe the visible change. In pull requests, summarise the behaviour changed, list routes or languages checked, link any relevant issue, and include screenshots for visual changes. Do not commit local environments, credentials or generated caches.
