"""Merge freshly built CPython .pot templates into this repository's .po files.

Behaves like ``msgmerge``, so it can run without GNU gettext:

* entries follow the order of the new template;
* existing translations are kept;
* strings that are new upstream are added untranslated;
* a string that only changed slightly upstream gets the closest old
  translation, marked ``fuzzy`` so a translator re-checks it;
* strings removed upstream are dropped.

Source references are rewritten from ``../../bugs.rst:5`` (as produced by
``make -C venv/cpython/Doc gettext``) to ``bugs.rst:5``, matching the files.

Usage:
    python scripts/merge_pot.py PATH_TO_POT_DIR
"""

import difflib
import sys
from pathlib import Path

import polib

FUZZY_CUTOFF = 0.8  # similar to msgmerge's fuzzy matching threshold
KEEP_METADATA = ("Last-Translator", "Language-Team", "Language", "PO-Revision-Date", "Plural-Forms")


def clean_occurrences(entry: polib.POEntry) -> list[tuple[str, str]]:
    return [(path.removeprefix("../../"), line) for path, line in entry.occurrences]


def merge_file(pot_path: Path, po_path: Path) -> tuple[int, int]:
    pot = polib.pofile(str(pot_path), wrapwidth=79)
    old = polib.pofile(str(po_path), wrapwidth=79) if po_path.exists() else None
    new = polib.POFile(wrapwidth=79)
    new.header = old.header if old else pot.header
    new.metadata = dict(pot.metadata)
    if old:
        new.metadata.update({k: v for k, v in old.metadata.items() if k in KEEP_METADATA})
        new.metadata_is_fuzzy = old.metadata_is_fuzzy
    else:
        new.metadata_is_fuzzy = pot.metadata_is_fuzzy

    previous = {(e.msgctxt, e.msgid): e for e in old if not e.obsolete} if old else {}
    unmatched = [e for e in previous.values() if e.msgstr]
    added = fuzzied = 0
    for tmpl in pot:
        entry = polib.POEntry(
            msgid=tmpl.msgid,
            msgctxt=tmpl.msgctxt,
            msgid_plural=tmpl.msgid_plural,
            occurrences=clean_occurrences(tmpl),
            comment=tmpl.comment,
            flags=[f for f in tmpl.flags if f != "fuzzy"],
        )
        prev = previous.get((tmpl.msgctxt, tmpl.msgid))
        if prev is not None:
            entry.msgstr = prev.msgstr
            entry.msgstr_plural = prev.msgstr_plural
            entry.tcomment = prev.tcomment
            if "fuzzy" in prev.flags:
                entry.flags.append("fuzzy")
        else:
            added += 1
            candidates = {e.msgid: e for e in unmatched if e.msgctxt == tmpl.msgctxt}
            close = difflib.get_close_matches(tmpl.msgid, candidates, n=1, cutoff=FUZZY_CUTOFF)
            if close:
                entry.msgstr = candidates[close[0]].msgstr
                entry.flags.append("fuzzy")
                entry.previous_msgid = close[0]
                fuzzied += 1
        new.append(entry)
    if old is not None and _entries(old) == _entries(new):
        return 0, 0  # nothing changed upstream: leave the file (and its header) as is
    po_path.parent.mkdir(parents=True, exist_ok=True)
    new.save(str(po_path))
    return added, fuzzied


def _entries(po: polib.POFile) -> list[tuple]:
    return [
        (e.msgctxt, e.msgid, e.msgid_plural, e.msgstr, tuple(sorted(e.msgstr_plural.items())),
         tuple(e.occurrences), e.comment, tuple(sorted(e.flags)))
        for e in po if not e.obsolete
    ]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    repo = Path(__file__).resolve().parent.parent
    pot_dir = Path(sys.argv[1]).resolve()
    total_added = total_fuzzy = 0
    for pot_path in sorted(pot_dir.rglob("*.pot")):
        rel = pot_path.relative_to(pot_dir).with_suffix(".po")
        added, fuzzied = merge_file(pot_path, repo / rel)
        if added:
            print(f"{rel}: {added} new or changed strings ({fuzzied} pre-filled as fuzzy)")
        total_added += added
        total_fuzzy += fuzzied
    print(f"Done: {total_added} new or changed strings, {total_fuzzy} marked fuzzy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
