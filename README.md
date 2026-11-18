# python-docs-te — తెలుగు (Telugu) translation of the Python documentation

This repository holds the Telugu (`te`) translation of the
[Python documentation](https://docs.python.org/3/), following
[PEP 545](https://peps.python.org/pep-0545/) and the
[Python Developer's Guide translation process](https://devguide.python.org/documentation/translations/coordinating/).

**Status:** the core resources (`bugs.po`, `tutorial/` and `builtins/functions.po`)
are translated. This branch is for Python 3.14; Python 3.15 is on branch `3.15`.

## Priorities

To get added to the language switcher on docs.python.org, these files have to be fully translated first:

1. `bugs.po` (with links pointing to this repository's issue tracker)
2. every file in `tutorial/`
3. `builtins/functions.po`

## How to contribute

1. Fork this repository and create a branch from the branch of the Python
   version you are translating (`3.15` or `3.14`).
2. Pick a `.po` file (run `make todo` to see what's left) and translate the `msgstr` entries.
3. Keep terms consistent with [`GLOSSARY.md`](GLOSSARY.md), and follow the
   [code samples](#code-samples) rule below.
4. Run `make wrap` to rewrap the files you changed, then `make verifs`
   (wrapping, spelling and markup checks) before you commit.
5. Open a pull request.

Read the [translating guide](https://devguide.python.org/documentation/translations/translating/) before you start.

### Code samples

This is the rule for the whole Telugu translation, so every page reads the
same way. The devguide recommends translating comments and string literals
in code examples but never names; this project translates **comments only**,
as the Chinese, Japanese and Korean translations do.

In code samples, interactive sessions and tracebacks:

- **Translate** comments (the text after `#`), keeping the `#` in the same
  column.
- **Never translate** keywords or names: variables, functions, classes,
  arguments, attributes and modules.
- **Keep in English** string literals, prompts (`>>>`, `...`), indentation,
  program output and error messages. A translated string would no longer
  match the output printed next to it, so readers would see something
  different from what Python prints when they run the example.
- **Leave as they are** `#!` lines, `# -*- coding: ... -*-` lines and
  commented-out code.

Changing this rule means changing it here and in
[`GLOSSARY.md`](GLOSSARY.md), and applying it to every file at once.

## Keeping up with CPython

[translations.python.org](https://translations.python.org) measures this
translation against the *latest* CPython sources of each branch, so new or changed
upstream strings lower the core completion (`bugs.po`, `tutorial/` and
`builtins/functions.po`) even when nothing changed here. To stay at 100%:

1. Run `make merge` to update every `.po` file (new strings appear
   untranslated, slightly changed ones as fuzzy).
2. Run `make core` to list the core strings that need work, and translate them.
3. Commit the result.

The tools need `polib`, `potodo` and `powrap`
(`python -m pip install polib potodo powrap`); `powrap`, used by `make wrap`,
`make merge` and `make verifs`, needs GNU gettext's `msgcat`
(`apt install gettext` or `brew install gettext`). `make spell` needs
`pospell` and the `hunspell-te` dictionary. On macOS, `make` (the HTML build)
also needs GNU coreutils (`brew install coreutils`). The Test workflow runs
the same core check every week and fails when upstream has moved ahead.

This repository is the source of truth and translations are made through
pull requests. If the translation is ever connected to Transifex, upload
fixes made here to Transifex (`tx push -t`) before the next pull from it,
otherwise the sync overwrites them.

## Communication

- Discourse: [Documentation › Translations](https://discuss.python.org/c/documentation/translations/)
- Discord: [Python Docs server](https://discord.gg/h3qDwgyzga), `#translations` channel

## Documentation Contribution Agreement

Python's documentation is maintained using a global network of volunteers. By posting this project on Transifex, Github, and other public places, and inviting you to participate, we are proposing an agreement that you will provide your improvements to Python's documentation or the translation of Python's documentation for the PSF's use under the CC0 license (available at https://creativecommons.org/publicdomain/zero/1.0/legalcode). In return, you may publicly claim credit for the portion of the translation you contributed and if your translation is accepted by the PSF, you may (but are not required to) submit a patch including an appropriate annotation in the Misc/ACKS or TRANSLATORS file. Although nothing in this Documentation Contribution Agreement obligates the PSF to incorporate your textual contribution, your participation in the Python community is welcomed and appreciated.

You signify acceptance of this agreement by submitting your work to the PSF for inclusion in the documentation.
