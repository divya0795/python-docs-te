"""Check completion of the core resources the way translations.python.org does.

The dashboard (https://github.com/python-docs-translations/dashboard) merges
this repository's .po files with .pot templates built from the *latest*
CPython sources of the current branch, then measures the "core" files:
bugs.po, tutorial/*.po and builtins/functions.po. A translation is only added
to the language switcher once core completion is 100%.

Strings added or changed upstream after the .po files were last merged make
the score drop below 100% even though nothing here changed. This script
reproduces the dashboard's number and lists exactly what is missing.

Usage:
    python scripts/core_completion.py PATH_TO_POT_DIR

PATH_TO_POT_DIR is the gettext output of CPython's Doc directory, for example
venv/cpython/Doc/build/gettext after ``make -C venv/cpython/Doc gettext``.
Exits with status 1 when core completion is below 100%.
"""

import sys
import tempfile
from pathlib import Path

import polib
from potodo import potodo
from potodo.arguments_handling import Filters

CORE = ["bugs.po", "tutorial/*.po", "builtins/functions.po"]
# Same exclude patterns as the dashboard's completion.py
CORE_EXCLUDES = ["**/*", "!bugs.po", "!tutorial/*", "!builtins/functions.po"]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    repo = Path(__file__).resolve().parent.parent
    pot_dir = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory() as merge_dir:
        project = potodo.merge_and_scan_paths(
            [repo], pot_path=pot_dir, merge_path=Path(merge_dir), api_url=""
        )
        project.filter(
            filters=Filters(False, True, 0, 100, False, False), exclude=CORE_EXCLUDES
        )
        completion = project.completion
        # The dashboard rounds to 2 decimals, so a few missing words can still
        # show as 100.00%; the per-file list below is the strict check.
        print(f"Core completion: {completion:.4f}%")

        missing = 0
        for pattern in CORE:
            for merged in sorted(Path(merge_dir).rglob(pattern)):
                po = polib.pofile(str(merged))
                untranslated = po.untranslated_entries()
                fuzzy = po.fuzzy_entries()
                if untranslated or fuzzy:
                    rel = merged.relative_to(merge_dir)
                    print(f"  {rel}: {len(untranslated)} untranslated, {len(fuzzy)} fuzzy")
                    for entry in (untranslated + fuzzy)[:5]:
                        print(f"      {entry.msgid[:70]!r}")
                    missing += len(untranslated) + len(fuzzy)
        if missing:
            print(f"{missing} core strings need work; run 'make merge' and translate them.")
        else:
            print("All core strings are translated.")
    return 0 if completion >= 100 and not missing else 1


if __name__ == "__main__":
    sys.exit(main())
