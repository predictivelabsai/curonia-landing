# Repository Guidelines

## Project Structure & Module Organization

`main.py` imports the FastHTML app from `app.py`, where advisory routes compose page content. Shared layout and design tokens live in `components.py`. Edit team data in `content/team.py`; keep translation keys and the EN/LT/LV/ET catalog in `utils/i18n.py`. Browser assets are in `static/` (`site.css`, `three-hero.js`, and `favicon.svg`). Legacy news-feed code remains in `content/news.py` but is not used by the advisory pages.

## Build, Test, and Development Commands

- `python -m venv .venv && source .venv/bin/activate` creates and enters a local environment.
- `pip install -r requirements.txt` installs FastHTML, Uvicorn, and news-feed dependencies.
- `uvicorn main:app --reload --port 5001` runs the site locally at `http://127.0.0.1:5001`.
- `docker compose up --build` builds and runs the container on port 5001.
- `python -m unittest discover -s tests` runs route, language, and content checks.
- `python -m compileall -q main.py app.py components.py content utils` checks Python syntax.

## Coding Style & Naming Conventions

Use four-space indentation and follow the existing Python style: `snake_case` for routes, helpers, and translation keys; `PascalCase` for reusable FastHTML components; and uppercase names for module constants. Keep routes focused on assembling components, and place reusable markup in `components.py`. Keep CSS in `static/site.css` and browser behavior in `static/three-hero.js`. No formatter or linter is configured, so match nearby code when editing.

## Testing Guidelines

Route tests use Python's built-in `unittest` and HTTPX's ASGI transport; there is no coverage threshold. Run the tests and syntax check above, then open affected routes in a browser. For copy or navigation changes, check all four languages using the language switcher. Place new tests in `tests/` and name files `test_*.py`.

## Commit & Pull Request Guidelines

Recent commits use short, imperative subjects such as `Add i18n support with EN/LT/LV/ET language switcher`. Keep each commit focused and describe the visible change. In pull requests, summarize the behavior changed, list routes or languages checked, link any relevant issue, and include screenshots for visual changes. Do not commit local environments, credentials, or generated caches.
