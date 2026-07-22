#!/usr/bin/env python3
"""Verify that internal /docs/... links resolve to real Markdown files.

Link convention (see CLAUDE.md):
  /docs            -> index.md
  /docs/<path>     -> <path>.md  OR  <path>/index.md   (directory landing page)
  #anchors are ignored for resolution (the site renderer owns anchor slugs)

Exits non-zero and prints every unresolved link, so it can gate CI.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Markdown link whose target starts with /docs, e.g. [text](/docs/foo/bar#anchor)
LINK_RE = re.compile(r"\[[^\]]*\]\((/docs[^)]*)\)")


def doc_files(root):
    files = set()
    for dirpath, dirnames, names in os.walk(root):
        if ".git" in dirpath.split(os.sep):
            continue
        for name in names:
            if name.endswith(".md"):
                files.add(os.path.relpath(os.path.join(dirpath, name), root))
    return files


def resolves(target, files):
    path = target.split("#", 1)[0]
    if not path.startswith("/docs"):
        return True  # external or non-docs link; not our concern
    path = path[len("/docs"):].strip("/")
    if path == "":
        return "index.md" in files
    return f"{path}.md" in files or os.path.join(path, "index.md") in files


def main():
    files = doc_files(ROOT)
    broken = []
    for rel in sorted(files):
        with open(os.path.join(ROOT, rel), encoding="utf-8") as handle:
            for lineno, line in enumerate(handle, 1):
                for match in LINK_RE.finditer(line):
                    if not resolves(match.group(1), files):
                        broken.append((rel, lineno, match.group(1)))

    if broken:
        print(f"Found {len(broken)} broken internal /docs link(s):")
        for rel, lineno, target in broken:
            print(f"  {rel}:{lineno}  ->  {target}")
        return 1

    print(f"OK: all internal /docs links resolve ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
