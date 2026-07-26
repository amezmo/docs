#!/usr/bin/env python3
"""Verify that internal Markdown links resolve to real files.

Internal links are relative, .md-suffixed paths -- GitHub-navigable and
host-agnostic; the site renderer rewrites them to the published URL scheme:
  releases.md
  ../instances/scaling.md
  ../deployments/directories.md#successful-deployments
  ../api/index.md   (directory landing page)

Skipped: external URLs (http/https/mailto), same-page #anchors, and
site-absolute links to the marketing site (e.g. /sites, /locations).

Exits non-zero and prints every unresolved internal link, so it can gate CI.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
EXTERNAL = ("http://", "https://", "mailto:", "//")


def doc_files(root):
    files = set()
    for dirpath, _dirs, names in os.walk(root):
        parts = dirpath.split(os.sep)
        if ".git" in parts or ".github" in parts:
            continue
        for name in names:
            if name.endswith(".md") and name != "CLAUDE.md":
                files.add(os.path.relpath(os.path.join(dirpath, name), root))
    return files


def is_internal(url):
    return not (url.startswith(EXTERNAL) or url.startswith("#") or url.startswith("/"))


def main():
    files = doc_files(ROOT)
    broken = []
    for rel in sorted(files):
        with open(os.path.join(ROOT, rel), encoding="utf-8") as handle:
            for lineno, line in enumerate(handle, 1):
                for match in LINK_RE.finditer(line):
                    url = match.group(1)
                    if not is_internal(url):
                        continue
                    path = url.split("#", 1)[0]
                    target = os.path.normpath(os.path.join(os.path.dirname(rel), path))
                    if not path.endswith(".md") or target not in files:
                        broken.append((rel, lineno, url))

    if broken:
        print(f"Found {len(broken)} broken internal link(s):")
        for rel, lineno, url in broken:
            print(f"  {rel}:{lineno}  ->  {url}")
        return 1

    print(f"OK: all internal links resolve ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
