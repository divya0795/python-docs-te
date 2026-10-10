# python-docs-te — తెలుగు (Telugu) translation of the Python documentation

This repository holds the Telugu (`te`) translation of the
[Python documentation](https://docs.python.org/3/), following
[PEP 545](https://peps.python.org/pep-0545/) and the
[Python Developer's Guide translation process](https://devguide.python.org/documentation/translations/coordinating/).

**Status:** just started. Translating Python 3.15 (branch `3.15`).

## Priorities

To get added to the language switcher on docs.python.org, these files have to be fully translated first:

1. `bugs.po` (with links pointing to this repository's issue tracker)
2. every file in `tutorial/`
3. `builtins/functions.po`

## How to contribute

1. Fork this repository and create a branch from `3.15`.
2. Pick a `.po` file (run `make todo` to see what's left) and translate the `msgstr` entries.
3. Keep terms consistent with [`GLOSSARY.md`](GLOSSARY.md).
4. Run `make verifs` (wrapping and spelling checks) before you commit.
5. Open a pull request.

Read the [translating guide](https://devguide.python.org/documentation/translations/translating/) before you start.

## Communication

- Discourse: [Documentation › Translations](https://discuss.python.org/c/documentation/translations/)
- Discord: [Python Docs server](https://discord.gg/h3qDwgyzga), `#translations` channel

## Documentation Contribution Agreement

Python's documentation is maintained using a global network of volunteers. By posting this project on Transifex, Github, and other public places, and inviting you to participate, we are proposing an agreement that you will provide your improvements to Python's documentation or the translation of Python's documentation for the PSF's use under the CC0 license (available at https://creativecommons.org/publicdomain/zero/1.0/legalcode). In return, you may publicly claim credit for the portion of the translation you contributed and if your translation is accepted by the PSF, you may (but are not required to) submit a patch including an appropriate annotation in the Misc/ACKS or TRANSLATORS file. Although nothing in this Documentation Contribution Agreement obligates the PSF to incorporate your textual contribution, your participation in the Python community is welcomed and appreciated.

You signify acceptance of this agreement by submitting your work to the PSF for inclusion in the documentation.
