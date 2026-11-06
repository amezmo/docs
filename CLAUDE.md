# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is the public documentation source for **Amezmo**, a zero-downtime, atomic PHP application hosting platform. It contains **only Markdown content** — there is no application code, build step, package manager, or test suite. Changes are prose edits to `.md` files, validated by a lint CI workflow (see "Validation and the backlink rule" below).

The content is published on `amezmo.com` under the `/docs/` URL prefix. This repo is not self-publishing: the dashboard app reads these files from the server and renders them at request time.

To preview a page, open the `.md` file in an editor's Markdown preview (VS Code is configured via `.vscode/settings.json`). The CI lint checks are listed under "Validation and the backlink rule" below.

## Structure

Each top-level directory is a product area (`instances/`, `databases/`, `deployments/`, `domains/`, `environments/`, `secrets/`, `workers/`, `configuration/`, `php/`, `nginx/`, `caching/`, `solr/`, `teams/`, `billing/`, `policies/`, `how-to-guides/`, `api/`, ...). `index.md` at the repo root is the docs home page.

Every directory has an `index.md` that acts as its landing page and links out to the child pages in that section. When you add a new page, add a link to it from the section's `index.md` (and, for top-level sections, keep the root `index.md` in sync where relevant). Pages are not auto-discovered by a nav generator, with one exception: a section index that uses the `{{< section >}}` directive (see "Generated Index" below) lists its children from the dashboard's menu tree and needs no entry.

### Landing Page Section Index

A landing page's index of its child pages is a run of `###` sub-sections, one per child, not a bullet list of bare links:

```markdown
## In This Section

### Backup and Restore

Amezmo takes logical `mysqldump`-style [backups](backup-restore.md) you can
restore anywhere: copy production to your machine, archive it, or move data
between environments.
```

Rules for that block:

- **Give it a parent `## In This Section`** when the index sits above the page's first `##`. Without one the page jumps `#` to `###`, which is a skipped heading level. Where the list already sits under a heading of its own (`## Core Resources`, `## Managing Instances`), keep that heading and put the `###`s under it.
- **Heading text is plain, never a link.** The site's heading renderer keeps heading text outside the permalink anchor on purpose, because Safari Reader Mode discards any heading whose entire content is a single link. Put the link in the excerpt prose instead.
- **One or two sentences per child, written from that page's actual content**, not a restatement of its title. Say what the reader gets, so the excerpt earns the space the bare link used to occupy.
- **Link text describes the destination** (`[Encrypt your backups](encryption.md)`, not `[here](encryption.md)`), per WCAG 2.2 SC 2.4.4.

#### Generated Index: the `{{< section >}}` Directive

Where a landing page wants a plain list of its child pages and no excerpts, write the directive on a line of its own instead of a hand-written bullet list:

```markdown
## In This Section

{{< section >}}
```

The site replaces it with a bullet list of links to every direct child of the page, in menu order, labeled with the menu names. The list comes from the dashboard's documentation tree (`DocumentationMenuService.php`), the same source as the left rail, so it is complete by construction and a new page appears in it as soon as the page is registered. It is the Hugo `section` shortcode the Grafana docs use, without its parameters.

- **Spell it exactly `{{< section >}}`**, spaces included, as the only text in its paragraph. Without the spaces `<section>` is an HTML tag and the directive is not recognized. Inside a sentence, inline code, or a fenced block it stays literal.
- **GitHub and editor previews show the literal directive**, not the list. Only the site expands it.
- **Don't pair it with a hand-written index of the same children** on one page. Pick the `###` excerpt run when each child deserves a sentence, and the directive when the names say enough (`how-to-guides/index.md`).
- A bullet list needs no parent heading for the outline, so `## In This Section` is optional above the directive. Use it when the page has other `##` sections, so the list gets an entry in "On this page".

This applies to a section's own child pages. **Leave "See Also" and "Resources" lists as bullet lists**: cross-references to other sections, marketing guides, YouTube, or the dashboard are not sub-sections of the page, and promoting them to headings puts them in the page outline and the "On this page" TOC as though they were.

## Conventions (match these when editing or adding pages)

- **No YAML front matter.** Each page starts directly with a single `#` H1 title, followed by prose. Use `##`/`###` for sections.
- **Internal links are relative, `.md`-suffixed paths** — so they work in the GitHub file browser and don't hard-code the `/docs/` mount point; the site renderer rewrites them to the published URL. From `deployments/directories.md`, link a sibling as `releases.md` and another section as `../instances/scaling.md`. Link a directory's landing page via its `index.md` (e.g. `../api/index.md`). Section anchors use `#`, e.g. `../deployments/directories.md#successful-deployments`. Point at the target's real file path; do **not** use `/docs/`-absolute or extensionless links.
- **External links use full `https://` URLs.**
- **Horizontal rules (`---`) are for genuine thematic breaks only.** Headings organize the page and the heading underline is a CSS border, not an `<hr>`. So don't put a `---` between sections or use one as a decorative divider. The heading already marks the break, and an `<hr>` there is redundant (it also announces a "separator" to screen readers). Reach for `---` only for the uncommon case of a topic shift within a section that doesn't merit its own heading. A useful test: if the new content belongs in "On this page," it's a heading, not a rule. If a page wants several rules, restructure it with headings instead.

### API reference pages (`api/`)

API endpoint docs follow a fixed layout — replicate it exactly for new endpoints:
1. `#` H1 with the human-readable action name (e.g. `# Create an instance`).
2. The method and path on one line using inline code for the verb: `` `POST` /v1/instances ``.
3. A `## Parameters` section with a Markdown table: `Parameter | Type | In | Required | Description`. Requiredness is a property of the parameter, like Type and In, so it gets its own column (`Yes`, `No`, or `Conditional`) rather than a `**Required**` marker inside the Description cell. Bold there is presentational: screen readers do not announce `<strong>`, so the markup carries nothing, and it leaves "optional" implied by absence. Use `Conditional` when a parameter is required only in some cases, and say which in the Description. Cross-link related endpoints (e.g. from `api/instances/create-instance.md`, `See [Regions](../regions/list-regions.md)`).
4. A `## Code samples` section with a `### Request example` and `### Response`.
5. Fenced code blocks are preceded by a Leanpub-style title annotation on its own line, e.g. `{title="POST /v1/instances"}` above a ```` ```bash ```` request or `{title="201 Created"}` above a ```` ```javascript ```` JSON response. Keep this annotation — it is part of the site's rendering.

Do **not** repeat the endpoint name in these headings (`## Parameters for "Create an instance"`). That convention comes from GitHub's REST reference, where one page carries about twenty endpoints and the quoted name says which one's parameters you are reading. Each page here documents a single endpoint, so the H1, the `<title>`, the breadcrumb, and the left rail already name it. Repeating it makes headings less distinguishing under WCAG 2.2 SC 2.4.6, puts the page title twice into "On this page", and produces anchors like `#parameters-for-create-an-instance` instead of `#parameters`.

The API base URL in examples is `https://api.amezmo.com`. Authenticate with a Bearer token from an `AMEZMO_API_KEY` environment variable, double-quoted so the shell expands it: `-H "Authorization: Bearer $AMEZMO_API_KEY"`. The `api/authentication/index.md` and `api/endpoints.md` pages show the `export` step.

### API changelog (`api/changelog.md`)

Group entries by date with a `##` heading (`## YYYY-MM-DD`, newest first). Under each date, label changes with a **description list**: the type on its own line (`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Breaking`), then each change on a following `: ` line. Keep breaking changes under their own `Breaking` term so readers can scan for them.

```markdown
## 2022-12-12

Added
: `current_deployment` to [Get Environment](environments/get-environment.md)
```

The type is a label for the changes under it, so it wants markup that says so. A `dt`/`dd` pair carries that relationship (WCAG 2.2 SC 1.3.1) where a bold paragraph only implies it. Do **not** use `###` sub-headings here: repeated `### Added` headings collide into meaningless `#added-1` anchors and put four identical entries in the on-page TOC.

## Required CommonMark extensions

Pages are rendered by the site's **league/commonmark** parser (configured in the amezmo.com dashboard app at `app/Http/Docs/Controllers/DocsController.php`), not a generic GFM renderer. Beyond GFM, the docs depend on two extensions that must stay enabled:

- **`AttributesExtension`** — the `{.img-enlargable}` on images (enables the click-to-enlarge lightbox) and the `{title="..."}` code-block captions.
- **`DescriptionListExtension`** — definition lists written as a term line followed by a `: definition` line (used in `databases/index.md`, `cron/index.md`, `environments/trusted-ip-addresses.md`).

The `{{< section >}}` directive is expanded by the dashboard app's `App\Markdown\SectionIndexExpander`, which the docs controllers add to the environment per page. A dashboard build without it renders the directive as literal text.

Also assumed: raw-HTML passthrough for `<details>`/`<summary>` collapsibles (FAQs and long reference blocks), and a **custom GitHub-alert parser**. Write callouts using GitHub alert syntax — `> [!NOTE]` (also `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`, `[!CAUTION]`) on the blockquote's first line, with the content on the following `>` lines. Use these instead of a bold `**Note**:` prefix; the alert type renders its own label.

## Validation and the backlink rule

CI runs `.github/workflows/docs-lint.yml` on every push and PR. Run these locally from the repo root before proposing changes:

- Internal links resolve: `python3 .github/scripts/check_links.py` (fails the build)
- Reciprocal backlinks: `python3 .github/scripts/check_backlinks.py` (warn-only)
- Spelling: `codespell --config .codespellrc`
- Images use absolute URLs: `python3 .github/scripts/check_image_paths.py`
- Lexical report: `python3 .github/scripts/lexical_report.py` (report-only). Counts function words and content words in the prose and prints lexical density, the top words of each kind, and the function-word share per section. The function-word list lives in the script. In CI it also reports auxiliary and lexical verb distributions using spaCy, installed into a virtual environment from a hashed lock. Edit the top-level pins in `.github/scripts/lexical-requirements.in`, then regenerate `.github/scripts/lexical-requirements.txt` with the `uv pip compile` command at its top. CI fails if the two drift (`check_lexical_lock.py`). Locally, without spaCy, the verb sections are skipped. Pass file paths to report on those files instead of the published pages; CI does this for `README.md`, which the default run excludes.

**Internal links are reciprocal.** If a content page links to another content page, the target should link back with a contextual link. Index and landing pages (`index.md`) are exempt, since their nav is one-directional by design.

When you deliberately leave a link one-way (for example a troubleshooting page that points at billing, where a backlink would be forced), record it in `.github/backlink-ignore.txt` as `SRC -> DST` using the reported `/docs/...` URLs, with a short comment. That file is the escape hatch for intentional one-ways, not a way to skip natural backlinks.

## Editing guidance

- Preserve the existing informal, second-person voice ("your application", "you can...").
- Commit messages in history are terse and page-focused (e.g. `Update scaling.md`, `fix many typos`); follow that style.
