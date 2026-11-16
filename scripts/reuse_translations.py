"""Fill untranslated strings with translations from another branch.

Each Python version has its own branch (3.14, 3.15, ...), and most of the
documentation text is identical between them. For every untranslated entry in
the .po files of the current checkout, this looks for a translated, non-fuzzy
entry with exactly the same English text on the other branch, preferring the
same file, and copies the translation. This is what ``pomerge`` does in other
translation repositories.

By default only the same file is searched, so pages nobody has translated
are not filled with stray fragments (repeated headings, code samples). Pass
``--any-file`` to also reuse identical text from other files, for example
after a page was renamed upstream.

Usage:
    python scripts/reuse_translations.py BRANCH [--any-file]

Run it after ``make merge`` when starting or updating a branch.
"""

import subprocess
import sys
from pathlib import Path

import polib

SKIP = ("venv", ".venv", "locales")


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    ).stdout


def load_branch(repo: Path, branch: str) -> tuple[dict, dict]:
    """Return {(file, msgctxt, msgid): msgstr} and {(msgctxt, msgid): msgstr}."""
    per_file, anywhere = {}, {}
    for path in git(repo, "ls-tree", "-r", "--name-only", branch).split():
        if not path.endswith(".po"):
            continue
        po = polib.pofile(git(repo, "show", f"{branch}:{path}"))
        for e in po:
            if e.msgstr and not e.obsolete and "fuzzy" not in e.flags:
                per_file[(path, e.msgctxt, e.msgid)] = e.msgstr
                anywhere.setdefault((e.msgctxt, e.msgid), e.msgstr)
    return per_file, anywhere


def main() -> int:
    args = sys.argv[1:]
    any_file = "--any-file" in args
    args = [a for a in args if a != "--any-file"]
    if len(args) != 1:
        print(__doc__)
        return 2
    branch = args[0]
    repo = Path(__file__).resolve().parent.parent
    per_file, anywhere = load_branch(repo, branch)
    if not any_file:
        anywhere = {}
    total = 0
    for po_path in sorted(repo.glob("**/*.po")):
        rel = po_path.relative_to(repo)
        if rel.parts[0] in SKIP:
            continue
        po = polib.pofile(str(po_path), wrapwidth=79)
        filled = 0
        for e in po:
            if e.msgstr or e.obsolete or e.msgid_plural:
                continue
            found = per_file.get((str(rel), e.msgctxt, e.msgid)) or anywhere.get(
                (e.msgctxt, e.msgid)
            )
            if found:
                e.msgstr = found
                filled += 1
        if filled:
            po.save(str(po_path))
            print(f"{rel}: {filled} translations reused")
            total += filled
    print(f"Done: {total} translations reused from {branch}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
