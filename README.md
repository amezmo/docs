# Amezmo Documentation

![Amezmo Docs repository cover.](.github/assets/amezmo-docs-repo-card2x.jpg)

[![Docs lint status.](https://github.com/amezmo/docs/actions/workflows/docs-lint.yml/badge.svg)](https://github.com/amezmo/docs/actions/workflows/docs-lint.yml)
[![Pull requests welcome.](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/amezmo/docs/pulls)

The source for the [Amezmo](https://www.amezmo.com) docs: everything on
zero-downtime PHP hosting, from your first ``git push`` to tuning Nginx,
OPcache, and Redis on a production instance. Published at
[amezmo.com/docs](https://www.amezmo.com/docs/).

**This repo is Markdown and nothing else.** No framework, no package manager,
no build step, no dependencies to install. Clone it, open a ``.md`` file in your
editor's preview, and you are looking at the page. That keeps the distance
between "this paragraph is wrong" and a merged fix short.

## Contributors

Built by the people who use it.

[![Contributor avatars.](https://contrib.rocks/image?repo=amezmo/docs)](https://github.com/amezmo/docs/graphs/contributors)

Thanks also to [Steven DuBois](https://github.com/sdubois)
([#6](https://github.com/amezmo/docs/pull/6)).

Your avatar goes here after your first merged PR. GitHub has to match the
email on your commit to your account, so add that email under your GitHub
email settings if you don't appear. The image can take up to three days to
refresh.

## How to Contribute

You already know something these docs get wrong. Ship it:

```bash
$ git clone git@github.com:amezmo/docs.git
$ cd docs
$ git checkout -b fix-cron-timezone-note
$ $EDITOR cron/index.md
$ python3 .github/scripts/check_links.py
```

Then open a pull request. Typo fixes, a missing flag, a code sample that no
longer runs, an entire new how-to guide: all of it is welcome. Small PRs take
the least time to review.

Good first contributions:

- Fix a code sample you tried and found stale.
- Add the gotcha that cost you an hour, as a ``> [!WARNING]`` callout.
- Write the how-to guide for your framework in
  [how-to-guides/](how-to-guides/index.md).
- Document an endpoint the [REST API](api/index.md) section is missing.

Read the
[contributor rulebook](CLAUDE.md)
before a larger change. It covers page layout, link conventions, the API
reference format, and the changelog format. It's written for Claude Code, and
it's the same rulebook a human needs.

## Conventions Worth Knowing Up Front

Internal links are relative and keep their ``.md`` suffix, so they work in the
GitHub file browser and on the rendered site: ``releases.md`` for a sibling,
``../instances/scaling.md`` across sections. Never use a ``/docs/``-absolute or
extensionless path.

Links are reciprocal. When one content page links to another, the target links
back. Landing pages are exempt. Record a deliberate one-way link in
[``.github/backlink-ignore.txt``](.github/backlink-ignore.txt)
with a comment explaining why.

Pages render through league/commonmark with the attributes and description list
extensions, plus GitHub alert callouts:

```markdown
<!-- databases/backup-restore.md -->
> [!WARNING]
> Restoring a backup overwrites the target database.
```

Link each new page from its section's ``index.md``. No nav generator discovers
pages. The exception is a section index that uses the ``{{< section >}}``
directive: the site expands it into a list of the section's child pages from
the dashboard's menu tree.

## The Map

[index.md](index.md) is the home page. The big sections:

| Section | What's in it |
| --- | --- |
| [Instances](instances/index.md) | Dedicated and full-stack servers, scaling, and private networking |
| [Deployments](deployments/index.md) | Atomic zero-downtime releases, hooks, and instant rollbacks |
| [Databases](databases/index.md) | Managed MySQL, backups, and restores between environments |
| [REST API](api/index.md) | Endpoint reference for automating the dashboard |
| [How-to guides](how-to-guides/index.md) | Laravel, Craft CMS, Drupal, and others |
| [Domains](domains/index.md), [Cron](cron/index.md), [Workers](workers/index.md) | The rest of the platform surface |

## See Also

- [Amezmo on YouTube](https://www.youtube.com/@AmezmoPHP)
- [PHP hosting guides](https://www.amezmo.com/guides)
- [Amezmo on GitHub](https://github.com/amezmo)
- [Slack community](https://www.amezmo.com/goslack)
