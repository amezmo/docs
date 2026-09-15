# Amezmo Documentation

[![Docs lint](https://github.com/amezmo/docs/actions/workflows/docs-lint.yml/badge.svg)](https://github.com/amezmo/docs/actions/workflows/docs-lint.yml)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/amezmo/docs/pulls)

The source for the [Amezmo](https://www.amezmo.com) docs: everything on
zero-downtime PHP hosting, from your first `git push` to tuning Nginx, OPcache,
and Redis on a production instance. Published at
[amezmo.com/docs](https://www.amezmo.com/docs/).

**This repo is Markdown and nothing else.** No framework, no package manager,
no build step, no dependencies to install. Clone it, open a `.md` file in your
editor's preview, and you are looking at the page. That means the distance
between "this paragraph is wrong" and a merged fix is about four minutes.

## Contribute

You already know something we got wrong. Ship it:

```bash
$ git clone git@github.com:amezmo/docs.git
$ cd docs
$ git checkout -b fix-cron-timezone-note
$ $EDITOR cron/index.md
$ python3 .github/scripts/check_links.py
```

Then open a pull request. Typo fixes, a missing flag, a code sample that no
longer runs, an entire new how-to guide: all of it is welcome, and small PRs
get merged fast.

Good first contributions:

- Fix a code sample you tried and found stale.
- Add the gotcha that cost you an hour, as a `> [!WARNING]` callout.
- Write the how-to guide for your framework in
  [how-to-guides/](how-to-guides/index.md).
- Document an endpoint the [REST API](api/index.md) section is missing.

Read the
[contributor rulebook](CLAUDE.md)
before a larger change. It covers page layout, the API reference format, the
changelog format, and the house writing style. It's written for Claude Code, and
it's the same rulebook a human needs.

## Local Checks

CI runs these four on every push and pull request. Run them from the repo root
first:

```bash
$ python3 .github/scripts/check_links.py        # internal links resolve
$ python3 .github/scripts/check_image_paths.py  # images use absolute URLs
$ codespell --config .codespellrc               # spelling
$ python3 .github/scripts/check_backlinks.py    # backlinks (warn-only)
```

The first three gate the build. The backlink check only reports.

## Conventions Worth Knowing Up Front

Internal links are relative and keep their `.md` suffix, so they work in the
GitHub file browser and on the rendered site: `releases.md` for a sibling,
`../instances/scaling.md` across sections. Never use a `/docs/`-absolute or
extensionless path.

Links are reciprocal. When one content page links to another, the target links
back. Landing pages are exempt, and deliberate one-way links are recorded in
[`.github/backlink-ignore.txt`](.github/backlink-ignore.txt)
with a comment explaining why.

Pages render through league/commonmark with the attributes and description list
extensions, plus GitHub alert callouts:

```markdown
> [!WARNING]
> Restoring a backup overwrites the target database.
```

New pages are linked from their section's `index.md`. Nothing is
auto-discovered by a nav generator.

## The Map

[index.md](index.md) is the home page. The big sections:

| Section | What's in it |
| --- | --- |
| [Instances](instances/index.md) | Dedicated and full-stack servers, scaling, private networking |
| [Deployments](deployments/index.md) | Atomic zero-downtime releases, hooks, instant rollbacks |
| [Databases](databases/index.md) | Managed MySQL, backups, restores between environments |
| [REST API](api/index.md) | Endpoint reference for automating the dashboard |
| [How-to guides](how-to-guides/index.md) | Laravel, Craft CMS, Drupal, and friends |
| [Domains](domains/index.md), [Cron](cron/index.md), [Workers](workers/index.md) | The rest of the platform surface |

## Contributors

Built by the people who use it.

[![Contributors](https://contrib.rocks/image?repo=amezmo/docs)](https://github.com/amezmo/docs/graphs/contributors)

Your avatar goes here on your first merged PR.

## See Also

- [Amezmo on YouTube](https://www.youtube.com/@AmezmoPHP)
- [PHP hosting guides](https://www.amezmo.com/guides)
- [Amezmo on GitHub](https://www.github.com/amezmo)
- [Slack community](https://www.amezmo.com/goslack)
