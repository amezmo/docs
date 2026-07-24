#!/usr/bin/env python3
"""Warn-only backlink audit for CI.

If page A links to internal page B, B ideally links back to A. Many one-way
links are legitimate (index/landing-page nav, changelog->endpoint, API
"see also" cross-refs), so this check NEVER fails the build -- it only surfaces
content<->content pages linked one way, as GitHub notices + a job summary, so
the gaps can be reviewed.

Internal links are relative .md paths; they're resolved to files and reported
in canonical /docs/... form (stable regardless of link storage format), which
is also how .github/backlink-ignore.txt entries are matched.

Excluded:
  - index/landing pages (index.md) -- their nav is one-directional by design
  - non-published files (CLAUDE.md, anything under .github/)
  - pairs listed in .github/backlink-ignore.txt (known-intentional one-ways)

Exit code is always 0.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IGNORE_FILE = os.path.join(ROOT, ".github", "backlink-ignore.txt")
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


def resolve(url, source_rel, files):
    if url.startswith(EXTERNAL) or url.startswith("#") or url.startswith("/"):
        return None
    path = url.split("#", 1)[0]
    if not path.endswith(".md"):
        return None
    target = os.path.normpath(os.path.join(os.path.dirname(source_rel), path))
    return target if target in files else None


def docs_url(rel):
    if rel == "index.md":
        return "/docs"
    if rel.endswith("/index.md"):
        return "/docs/" + rel[: -len("/index.md")]
    return "/docs/" + rel[:-3]


def is_index(rel):
    return rel == "index.md" or rel.endswith("/index.md")


def load_ignore():
    pairs = set()
    if not os.path.exists(IGNORE_FILE):
        return pairs
    with open(IGNORE_FILE, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if "->" not in line:
                continue
            src, dst = (p.strip() for p in line.split("->", 1))
            pairs.add((src, dst))
    return pairs


def main():
    files = doc_files(ROOT)
    links = {}
    for rel in files:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
            text = fh.read()
        links[rel] = {
            d for d in (resolve(m.group(1), rel, files) for m in LINK_RE.finditer(text))
            if d and d != rel
        }

    ignore = load_ignore()
    gaps = []
    for src in links:
        for dst in links[src]:
            if is_index(src) or is_index(dst):
                continue  # index/landing-page nav is one-directional by design
            if src in links.get(dst, set()):
                continue  # already reciprocated
            if (docs_url(src), docs_url(dst)) in ignore:
                continue  # known-intentional one-way
            gaps.append((src, dst))

    gaps.sort(key=lambda p: (p[1], p[0]))

    for src, dst in gaps:
        print(f"::notice file={dst}::{docs_url(dst)} is linked from {docs_url(src)} "
              f"but does not link back — consider a contextual backlink.")

    header = (f"Backlink audit: {len(gaps)} content page(s) linked one way "
              f"(warn-only — not a failure).")
    print("\n" + header)
    for src, dst in gaps:
        print(f"  {docs_url(dst)}  could link back to  {docs_url(src)}")
    if gaps:
        print("\nReviewed an intentional one-way? Add it to .github/backlink-ignore.txt to silence it.")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as sm:
            sm.write(f"### Backlink audit (warn-only)\n\n{header}\n\n")
            if gaps:
                sm.write("| Page missing a backlink | Linked from |\n|---|---|\n")
                for src, dst in gaps:
                    sm.write(f"| `{docs_url(dst)}` | `{docs_url(src)}` |\n")
                sm.write("\nSuppress intentional one-way links in `.github/backlink-ignore.txt`.\n")
            else:
                sm.write("No unreviewed one-way content links. :tada:\n")

    return 0  # warn-only: never fails the build


if __name__ == "__main__":
    sys.exit(main())
