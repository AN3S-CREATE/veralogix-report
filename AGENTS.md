# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **static HTML marketing website** (Veralogix Smart Mining Solution), deployed via GitHub Pages. There is no build step, package manager, lint, or automated test suite.

### Running the site (dev)
- Serve the repo root with any static server, e.g. `python3 -m http.server 8080`, then open `http://localhost:8080/`.
- Entry point is `index.html`; other pages (`solutions.html`, `roi.html`, `loadscan.html`, `trimble.html`, etc.) are sibling HTML files linked from the nav.
- No restart/rebuild needed after edits — just refresh the browser (the server serves files directly from disk).

### Non-obvious gotchas
- The files under `images/` are intentional **70-byte placeholder PNGs** (see `images/README.md`). Large solid-color blocks where images should appear are expected and are NOT a code bug.
- The page pulls Tailwind CSS, Chart.js, and Google Fonts from external CDNs. With network access these load and the dark/lime-green theme + Chart.js charts render; in a restricted network the content still loads but styling/charts will be missing.
- `jules-scratch/verification/verify_hero_video.py` is a one-off Playwright screenshot script (hardcoded to port 8000); it is not part of the app and Playwright is not a project dependency.
- There is no lint/test/build command — validation is manual (load the site, click tabs, confirm charts render).
