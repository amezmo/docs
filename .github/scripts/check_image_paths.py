#!/usr/bin/env python3
"""Verify that every Markdown image references an absolute http(s) URL.

Docs images are served from object storage (static.amezmo.net), not from the
repo. A bare or local path -- e.g. ![x](/assets/foo.png), a relative path, or a
raw <img src="/assets/..."> -- won't resolve on the published site, so this gate
rejects any image whose URL is not an absolute http(s):// URL.

Exits non-zero and prints every offending reference, so it can gate CI.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Markdown image  ![alt](url ...)  -- capture the URL up to whitespace or ")"
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(\s*([^)\s]+)")
# Raw HTML image  <img ... src="url">
IMG_SRC_RE = re.compile(r"""<img\b[^>]*\bsrc\s*=\s*["']([^"']*)["']""", re.IGNORECASE)


def doc_files(root):
    files = set()
    for dirpath, dirnames, names in os.walk(root):
        if ".git" in dirpath.split(os.sep):
            continue
        for name in names:
            if name.endswith(".md"):
                files.add(os.path.relpath(os.path.join(dirpath, name), root))
    return files


def is_absolute(url):
    return url.startswith("http://") or url.startswith("https://")


def main():
    files = doc_files(ROOT)
    violations = []
    for rel in sorted(files):
        with open(os.path.join(ROOT, rel), encoding="utf-8") as handle:
            for lineno, line in enumerate(handle, 1):
                for regex in (MD_IMAGE_RE, IMG_SRC_RE):
                    for match in regex.finditer(line):
                        url = match.group(1)
                        if not is_absolute(url):
                            violations.append((rel, lineno, url))

    if violations:
        print(f"Found {len(violations)} image reference(s) using a bare/local path.")
        print(
            "Images must use an absolute https URL "
            "(e.g. https://s3.us-east-2.amazonaws.com/static.amezmo.net/<file>)."
        )
        for rel, lineno, url in violations:
            print(f"  {rel}:{lineno}  ->  {url}")
            # GitHub Actions inline annotation
            print(f"::error file={rel},line={lineno}::Bare image path, use an absolute https URL: {url}")
        return 1

    print(f"OK: every Markdown image uses an absolute URL ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
