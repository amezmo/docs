#!/usr/bin/env python3
"""Fail when lexical-requirements.txt no longer matches lexical-requirements.in.

The .in file holds the top-level pins and the .txt file is the hashed lock
generated from it (the command is at the top of the .txt). This catches an
edit to the .in that was never regenerated: every top-level requirement must
appear in the lock exactly as pinned.
"""
import os
import re
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(SCRIPTS, "lexical-requirements.in")
LOCK = os.path.join(SCRIPTS, "lexical-requirements.txt")


def normalize(req):
    """Compare names the way pip does: case-insensitive, with -, _, and . equal."""
    name, sep, rest = re.split(r"(==| @ )", req, maxsplit=1)
    return re.sub(r"[-_.]+", "-", name.strip()).lower() + sep + rest.strip()


def requirements(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.split(" #", 1)[0].rstrip(" \\\n")
            if line and not line.lstrip().startswith(("#", "--")):
                yield normalize(line)


def main():
    locked = set(requirements(LOCK))
    missing = [req for req in requirements(SOURCE) if req not in locked]
    for req in missing:
        print(f"::error file=.github/scripts/lexical-requirements.in::{req} is not "
              f"in lexical-requirements.txt. Regenerate the lock with the command "
              f"at the top of that file.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
