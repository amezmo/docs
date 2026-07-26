# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is the public documentation source for **Amezmo**, a zero-downtime, atomic PHP application hosting platform. It contains **only Markdown content** — there is no application code, build step, package manager, or test suite. Changes are prose edits to `.md` files, validated by a lint CI workflow (see "Validation and the backlink rule" below).

The content is published on `amezmo.com` under the `/docs/` URL prefix. This repo is not self-publishing: the dashboard app reads these files from the server and renders them at request time.

To preview a page, open the `.md` file in an editor's Markdown preview (VS Code is configured via `.vscode/settings.json`). The CI lint checks are listed under "Validation and the backlink rule" below.

## Structure

Each top-level directory is a product area (`instances/`, `databases/`, `deployments/`, `domains/`, `environments/`, `secrets/`, `workers/`, `configuration/`, `php/`, `nginx/`, `caching/`, `solr/`, `teams/`, `billing/`, `policies/`, `how-to-guides/`, `api/`, ...). `index.md` at the repo root is the docs home page.

Every directory has an `index.md` that acts as its landing page and links out to the child pages in that section. When you add a new page, add a link to it from the section's `index.md` (and, for top-level sections, keep the root `index.md` and `how-to-guides/index.md` in sync where relevant) — pages are not auto-discovered by a nav generator.

## Conventions (match these when editing or adding pages)

- **No YAML front matter.** Each page starts directly with a single `#` H1 title, followed by prose. Use `##`/`###` for sections.
- **Internal links are relative, `.md`-suffixed paths** — so they work in the GitHub file browser and don't hard-code the `/docs/` mount point; the site renderer rewrites them to the published URL. From `deployments/directories.md`, link a sibling as `releases.md` and another section as `../instances/scaling.md`. Link a directory's landing page via its `index.md` (e.g. `../api/index.md`). Section anchors use `#`, e.g. `../deployments/directories.md#successful-deployments`. Point at the target's real file path; do **not** use `/docs/`-absolute or extensionless links.
- **External links use full `https://` URLs.**

### API reference pages (`api/`)

API endpoint docs follow a fixed layout — replicate it exactly for new endpoints:
1. `#` H1 with the human-readable action name (e.g. `# Create an instance`).
2. The method and path on one line using inline code for the verb: `` `POST` /v1/instances ``.
3. A `## Parameters for "<action>"` section with a Markdown table: `Parameter | Type | In | Description`. Mark required params with `**Required**` in the Description cell, and cross-link related endpoints (e.g. from `api/instances/create-instance.md`, `See [Regions](../regions/list-regions.md)`).
4. A `## Code samples for "<action>"` section with a `### Request example` and `### Response`.
5. Fenced code blocks are preceded by a Leanpub-style title annotation on its own line, e.g. `{title="POST /v1/instances"}` above a ```` ```bash ```` request or `{title="201 Created"}` above a ```` ```javascript ```` JSON response. Keep this annotation — it is part of the site's rendering.

The API base URL in examples is `https://api.amezmo.com` and auth is `-H 'Authorization: Bearer {api_key}'`.

### API changelog (`api/changelog.md`)

Group entries by date with a `##` heading (`## YYYY-MM-DD`, newest first). Under each date, label changes with a **bold type line** — `**Added**`, `**Changed**`, `**Deprecated**`, `**Removed**`, `**Fixed**`, or `**Breaking**` — over a bullet list. Use bold labels, **not** `###` sub-headings: repeated `### Added` headings collide into meaningless `#added-1` anchors and clutter the on-page TOC. Keep breaking changes under their own `**Breaking**` label so readers can scan for them.

## Required CommonMark extensions

Pages are rendered by the site's **league/commonmark** parser (configured in the amezmo.com dashboard app at `app/Http/Docs/Controllers/DocsController.php`), not a generic GFM renderer. Beyond GFM, the docs depend on two extensions that must stay enabled:

- **`AttributesExtension`** — the `{.img-enlargable}` on images (enables the click-to-enlarge lightbox) and the `{title="..."}` code-block captions.
- **`DescriptionListExtension`** — definition lists written as a term line followed by a `: definition` line (used in `databases/index.md`, `cron/index.md`, `environments/trusted-ip-addresses.md`).

Also assumed: raw-HTML passthrough for `<details>`/`<summary>` collapsibles (FAQs and long reference blocks), and a **custom GitHub-alert parser**. Write callouts using GitHub alert syntax — `> [!NOTE]` (also `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`, `[!CAUTION]`) on the blockquote's first line, with the content on the following `>` lines. Use these instead of a bold `**Note**:` prefix; the alert type renders its own label.

## Validation and the backlink rule

CI runs `.github/workflows/docs-lint.yml` on every push and PR. Run these locally from the repo root before proposing changes:

- Internal links resolve: `python3 .github/scripts/check_links.py` (fails the build)
- Reciprocal backlinks: `python3 .github/scripts/check_backlinks.py` (warn-only)
- Spelling: `codespell --config .codespellrc`
- Images use absolute URLs: `python3 .github/scripts/check_image_paths.py`

**Internal links are reciprocal.** If a content page links to another content page, the target should link back with a contextual link. Index and landing pages (`index.md`) are exempt, since their nav is one-directional by design.

When you deliberately leave a link one-way (for example a troubleshooting page that points at billing, where a backlink would be forced), record it in `.github/backlink-ignore.txt` as `SRC -> DST` using the reported `/docs/...` URLs, with a short comment. That file is the escape hatch for intentional one-ways, not a way to skip natural backlinks.

## Editing guidance

- Preserve the existing informal, second-person voice ("your application", "you can...").
- Commit messages in history are terse and page-focused (e.g. `Update scaling.md`, `fix many typos`); follow that style.
