# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is the public documentation source for **Amezmo**, a zero-downtime, atomic PHP application hosting platform. It contains **only Markdown content** — there is no application code, build step, package manager, test suite, or linter. Changes are prose edits to `.md` files.

The content is published on `amezmo.com` under the `/docs/` URL prefix. This repo is not self-publishing: the `.github/workflows/deploy.yaml` workflow is a leftover GitHub Actions demo (it only echoes a message) and does not build or deploy anything. Do not treat it as the publishing pipeline.

There are no build/lint/test commands. To preview, open the `.md` file in an editor's Markdown preview (VS Code is configured via `.vscode/settings.json`).

## Structure

Each top-level directory is a product area (`instances/`, `databases/`, `deployments/`, `domains/`, `environments/`, `secrets/`, `workers/`, `configuration/`, `php/`, `nginx/`, `caching/`, `solr/`, `teams/`, `billing/`, `policies/`, `how-to-guides/`, `api/`, ...). `index.md` at the repo root is the docs home page.

Every directory has an `index.md` that acts as its landing page and links out to the child pages in that section. When you add a new page, add a link to it from the section's `index.md` (and, for top-level sections, keep the root `index.md` and `how-to-guides/index.md` in sync where relevant) — pages are not auto-discovered by a nav generator.

## Conventions (match these when editing or adding pages)

- **No YAML front matter.** Each page starts directly with a single `#` H1 title, followed by prose. Use `##`/`###` for sections.
- **Internal links are absolute, extensionless, and rooted at `/docs/`.** A file at `deployments/directories.md` is linked as `/docs/deployments/directories` (no `.md`). A directory link like `/docs/deployments` resolves to that directory's `index.md`. Section anchors use `#`, e.g. `/docs/deployments/directories#successful-deployments`. Do not use relative paths or include `.md` in links.
- **External links use full `https://` URLs.**

### API reference pages (`api/`)

API endpoint docs follow a fixed layout — replicate it exactly for new endpoints:
1. `#` H1 with the human-readable action name (e.g. `# Create an instance`).
2. The method and path on one line using inline code for the verb: `` `POST` /v1/instances ``.
3. A `## Parameters for "<action>"` section with a Markdown table: `Parameter | Type | In | Description`. Mark required params with `**Required**` in the Description cell, and cross-link related endpoints (e.g. `See [Regions](/docs/api/regions/list-regions)`).
4. A `## Code samples for "<action>"` section with a `### Request example` and `### Response`.
5. Fenced code blocks are preceded by a Leanpub-style title annotation on its own line, e.g. `{title="POST /v1/instances"}` above a ```` ```bash ```` request or `{title="201 Created"}` above a ```` ```javascript ```` JSON response. Keep this annotation — it is part of the site's rendering.

The API base URL in examples is `https://api.amezmo.com` and auth is `-H 'Authorization: Bearer {api_key}'`.

## Editing guidance

- Preserve the existing informal, second-person voice ("your application", "you can...").
- Commit messages in history are terse and page-focused (e.g. `Update scaling.md`, `fix many typos`); follow that style.
