#!/usr/bin/env python3
"""Report-only lexical analysis of the published docs prose.

Splits every word of running prose into function words (closed-class words
such as articles, prepositions, pronouns, conjunctions, and auxiliaries) and
content words (everything else), then reports totals, lexical density
(content words / all words), the most frequent words of each kind, and the
function-word share per top-level section.

When spaCy is installed it also reports two verb distributions, grouped by
lemma so "run", "runs", and "running" count together:

  - auxiliary verbs: tokens the parser labels aux or auxpass, which covers
    modals ("can", "should") and be/have/do used as helpers ("is deployed",
    "have created", "don't")
  - lexical verbs: tokens tagged VERB ("deploy", "create", "run")

The parser gives the "to" of an infinitive ("to deploy") the aux label as
well. It is a particle, not a verb, so it is left out.

be/have/do used as the main verb ("is ready", "has a database") fall in
neither and get a line of their own. The parser is what makes that split:
en_core_web_sm tags every form of be/have/do as AUX whatever its role.

CI installs spaCy from lexical-requirements.txt. Without it the verb sections
are skipped and the rest of the report still runs on the standard library.

Only prose is counted. Fenced code, inline code, HTML, URLs, link targets,
{...} attribute annotations, and GitHub alert markers are stripped first.
Content words are counted as written, so "deployment" and "deployments" are
separate entries.

Excluded, same as check_links.py: the CLAUDE.md/README.md meta files and
anything in a hidden directory such as .github/ or .claude/.

Usage:
  lexical_report.py              # every published page
  lexical_report.py README.md    # only the given files, excluded or not

CI runs it both ways, so README.md gets a report of its own without its words
counting toward the published prose.

Exit code is 0, except for a path argument that is not a file.
"""
import argparse
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
META_FILES = {"CLAUDE.md", "README.md"}
TOP_N = 25
SPACY_MODEL = "en_core_web_sm"
AUX_DEPS = {"aux", "auxpass"}
# Part of speech of the infinitive marker "to", which shares the aux label.
INFINITIVE_MARKER_POS = "PART"

# Closed-class words by category. A word belongs to one category only.
FUNCTION_WORDS = {
    "determiner": """a an the this that these those each every either neither
        some any no all both few many much more most several such what which
        whose another other""",
    "pronoun": """i me my mine myself we us our ours ourselves you your yours
        yourself yourselves he him his himself she her hers herself it its
        itself they them their theirs themselves who whom one ones someone
        anyone everyone something anything everything nothing nobody none
        somebody anybody everybody whatever whichever whoever""",
    "preposition": """about above across after against along among around as at
        before behind below beneath beside besides between beyond by despite
        down during except for from in inside into like near of off on onto
        out outside over past per since through throughout to toward towards
        under underneath unlike until up upon via with within without""",
    "conjunction": """and but or nor so yet because although though while
        whereas if unless whether than once when whenever where wherever""",
    "auxiliary": """am is are was were be been being have has had having do
        does did done can could may might must shall should will would""",
    "contraction": """it's that's there's here's what's who's let's i'm i've
        i'd i'll you're you've you'd you'll we're we've we'd we'll they're
        they've they'd they'll he's she's isn't aren't wasn't weren't hasn't
        haven't hadn't doesn't don't didn't can't couldn't won't wouldn't
        shouldn't mustn't mightn't""",
    "adverb/particle": """not there here then now also only too very how why
        just even still already again ever never always often""",
}
CATEGORY_OF = {w: cat for cat, words in FUNCTION_WORDS.items() for w in words.split()}

# Applied in order: each pattern removes markup or keeps only its visible text.
STRIP = [
    (re.compile(r"^(```|~~~).*?^\1", re.M | re.S), " "),   # fenced code
    (re.compile(r"(`+)[^\n]*?\1"), " "),                   # inline code
    (re.compile(r"<!--.*?-->", re.S), " "),
    (re.compile(r"<[^>]+>"), " "),                         # HTML tags
    (re.compile(r"\{[^}\n]*\}"), " "),                     # {title=...}, {.img-enlargable}
    (re.compile(r"!?\[([^\]]*)\]\([^)]*\)"), r"\1"),       # links and images: keep text
    (re.compile(r"https?://\S+"), " "),
    (re.compile(r"\[![A-Z]+\]"), " "),                     # > [!NOTE] markers
]
WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
# Heading, list, blockquote, and description-list markers at a line start.
LINE_MARKER = re.compile(r"^\s*(#+|[-*+]|\d+\.|>+|:)\s+")


def doc_files(root):
    files = []
    for dirpath, dirs, names in os.walk(root):
        # Hidden directories (.git, .github, .claude, ...) never hold
        # published pages.
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in names:
            if name.endswith(".md") and name not in META_FILES:
                files.append(os.path.relpath(os.path.join(dirpath, name), root))
    return sorted(files)


def prose(text):
    for pattern, repl in STRIP:
        text = pattern.sub(repl, text)
    return text.replace("\u2019", "'")


def words(text):
    return [w.lower() for w in WORD_RE.findall(text)]


def blocks(text):
    """Split prose into paragraphs, headings, list items, and table cells, so
    the parser never runs one sentence across them."""
    for para in re.split(r"\n\s*\n", text):
        lines = para.splitlines()
        if not any(LINE_MARKER.match(line) or "|" in line for line in lines):
            yield " ".join(line.strip() for line in lines).replace("*", "")
            continue
        for line in lines:
            for cell in line.split("|"):
                cell = LINE_MARKER.sub("", cell).replace("*", "").strip()
                if re.search(r"[A-Za-z]", cell):
                    yield cell


def repo_file(arg):
    """Parse a path argument into a path relative to the repo root."""
    path = os.path.abspath(arg)
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"not a file: {arg}")
    return os.path.relpath(path, ROOT)


def load_parser():
    try:
        import spacy
    except ImportError:
        return None
    # Named entities are unused. The parser stays: see the module docstring.
    return spacy.load(SPACY_MODEL, exclude=["ner"])


def section(rel):
    return rel.split(os.sep, 1)[0] if os.sep in rel else "(root)"


def pct(part, whole):
    return f"{part / whole:.1%}" if whole else "n/a"


def print_distribution(title, counter, limit=None):
    total = sum(counter.values())
    print(f"\n{title}")
    for w, n in counter.most_common(limit):
        print(f"  {w:<14} {n:>6}  {pct(n, total):>6}")


def write_distribution(sm, heading, counter, limit=None):
    total = sum(counter.values())
    sm.write(f"\n| {heading} | Count | Share |\n|---|---|---|\n")
    for w, n in counter.most_common(limit):
        sm.write(f"| `{w}` | {n} | {pct(n, total)} |\n")


def main():
    args = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    args.add_argument("files", nargs="*", type=repo_file,
                      help="report on these files instead of every published page")
    given = args.parse_args().files
    nlp = load_parser()
    function, content = Counter(), Counter()
    auxiliary, lexical, main_primary = Counter(), Counter(), Counter()
    modal_lemmas = set()
    sections = {}  # section -> [all words, function words]
    files = given or doc_files(ROOT)
    scope = ", ".join(given) or "published docs"
    for rel in files:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
            text = prose(fh.read())
        page = words(text)
        fw = [w for w in page if w in CATEGORY_OF]
        function.update(fw)
        content.update(w for w in page if w not in CATEGORY_OF)
        counts = sections.setdefault(section(rel), [0, 0])
        counts[0] += len(page)
        counts[1] += len(fw)
        if nlp is None:
            continue
        for doc in nlp.pipe(blocks(text)):
            for tok in doc:
                lemma = tok.lemma_.lower()
                if tok.pos_ == INFINITIVE_MARKER_POS:
                    continue
                if tok.dep_ in AUX_DEPS:
                    auxiliary[lemma] += 1
                    if tok.tag_ == "MD":
                        modal_lemmas.add(lemma)
                elif tok.pos_ == "VERB":
                    lexical[lemma] += 1
                elif tok.pos_ == "AUX":
                    main_primary[lemma] += 1

    n_function, n_content = sum(function.values()), sum(content.values())
    total = n_function + n_content
    by_category = Counter()
    for w, n in function.items():
        by_category[CATEGORY_OF[w]] += n
    hapax = sum(1 for n in content.values() if n == 1)
    ranked = sorted(sections.items(), key=lambda kv: -kv[1][1] / max(kv[1][0], 1))

    lines = [
        f"Pages: {len(files)}  Words: {total}",
        f"Function words: {n_function} ({pct(n_function, total)}), "
        f"{len(function)} of {len(CATEGORY_OF)} listed words used",
        f"Content words: {n_content} ({pct(n_content, total)} lexical density), "
        f"{len(content)} distinct, {hapax} used once",
    ]
    if nlp is None:
        verb_lines = ["Verb analysis skipped: spaCy is not installed "
                      "(CI installs it from .github/scripts/lexical-requirements.txt)."]
    else:
        n_aux, n_lex = sum(auxiliary.values()), sum(lexical.values())
        n_modal = sum(auxiliary[lemma] for lemma in modal_lemmas)
        verb_lines = [
            f"Auxiliary verbs: {n_aux}, {len(auxiliary)} distinct, "
            f"{n_modal} modal ({pct(n_modal, n_aux)})",
            f"Lexical verbs: {n_lex}, {len(lexical)} distinct lemmas, "
            f"{sum(1 for n in lexical.values() if n == 1)} used once",
            "be/have/do as the main verb: "
            + ", ".join(f"{w} {n}" for w, n in main_primary.most_common()),
        ]

    print("\n".join(lines + verb_lines))
    print("\nFunction words by category")
    for cat, n in by_category.most_common():
        print(f"  {cat:<16} {n:>6}  {pct(n, n_function):>6}")
    for label, counter in (("function", function), ("content", content)):
        print(f"\nTop {TOP_N} {label} words")
        for w, n in counter.most_common(TOP_N):
            print(f"  {w:<14} {n:>6}  {pct(n, total):>6} of words")
    if nlp is not None:
        print_distribution("Auxiliary verbs by lemma", auxiliary)
        print_distribution(f"Top {TOP_N} lexical verbs by lemma", lexical, TOP_N)
    print("\nFunction-word share by section")
    for sec, (n_all, n_fw) in ranked:
        print(f"  {sec:<16} {n_fw:>6} / {n_all:>6}  {pct(n_fw, n_all):>6}")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as sm:
            sm.write(f"### Lexical report: {scope} (report-only)\n\n")
            sm.write("".join(f"- {line}\n" for line in lines + verb_lines))
            sm.write("\n| Function word | Count | | Content word | Count |\n"
                     "|---|---|---|---|---|\n")
            for (fw, fn), (cw, cn) in zip(function.most_common(TOP_N),
                                          content.most_common(TOP_N)):
                sm.write(f"| `{fw}` | {fn} | | `{cw}` | {cn} |\n")
            if nlp is not None:
                write_distribution(sm, "Auxiliary verb", auxiliary)
                write_distribution(sm, "Lexical verb", lexical, TOP_N)
            sm.write("\n| Section | Words | Function words | Share |\n"
                     "|---|---|---|---|\n")
            for sec, (n_all, n_fw) in ranked:
                sm.write(f"| `{sec}` | {n_all} | {n_fw} | {pct(n_fw, n_all)} |\n")

    return 0  # report-only: never fails the build


if __name__ == "__main__":
    sys.exit(main())
