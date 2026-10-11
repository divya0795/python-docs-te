# Telugu glossary (పదకోశం)

Shared Telugu terms for the Python docs, so every file uses the same words.
See the devguide [translation style guide](https://devguide.python.org/documentation/translations/translating/#translation-style-guide).

Agree on new terms in an issue or PR before using them widely.

## Conventions

- **Never translate** code, Python keywords, built-in and module names,
  file names, command-line options, anything in ``` ``double backticks`` ```,
  or reST markup (roles such as `:ref:`, `:func:`, link targets in `<...>`).
- **Technical terms** are transliterated into Telugu script
  (for example *function* → ఫంక్షన్), because that is how Telugu-speaking
  programmers say and search for them. Use a native Telugu word only when it
  is already common in everyday writing (for example *value* → విలువ).
- **Labels in other tools' interfaces** that stay in English for the reader
  (GitHub buttons such as "New issue", "Sign up") are kept in English inside
  quotes, so readers can find them on screen.
- **Register:** polite, plural second person (మీరు, చేయండి), not the
  informal నువ్వు form.
- **Numbers and punctuation:** use Western digits (0–9) and the usual
  English punctuation; end sentences with a full stop (.), not ।.
- **Proper names** (Python, GitHub, Discourse, Mozilla) stay in Latin script.
- **Suffixes next to markup:** reST ignores a link, role or literal whose
  closing mark is directly followed by a letter, so a Telugu suffix must
  never be glued to it.
  - For links and roles, put the suffix inside the link text:
    ``:ref:`ఇష్యూ ట్రాకర్‌లో <using-the-tracker>` `` (not `` `ఇష్యూ ట్రాకర్ <…>`లో ``).
  - For ``` ``code`` ``` add an escaped space, which renders as nothing:
    ``` ``print()``\ ను ```.
- **Links to named targets** (`` `Documentation bugs`_ ``,
  `` `text <TRANSLATION_REPO_>`_ ``): Sphinx warns
  (`i18n.inconsistent_references`) whenever such a reference is changed, even
  only its label. To translate the label, keep the target name with an
  alias and end the whole message with `#noqa`, which Sphinx strips before
  rendering and which tells it to skip that check:
  `` `డాక్యుమెంటేషన్ బగ్‌లు <Documentation bugs_>`__ #noqa ``.
  The link then keeps following the URL defined in the English source.

## Project and contribution terms

| English | Telugu | Notes |
|---------|--------|-------|
| account | ఖాతా | |
| bug | బగ్ | plural బగ్‌లు |
| bug report | బగ్ రిపోర్ట్ | |
| contribute | సహకరించు | |
| contributor | సహకారి | |
| core developer | కోర్ డెవలపర్ | |
| developer | డెవలపర్ | plural డెవలపర్లు |
| discussion | చర్చ | |
| documentation | డాక్యుమెంటేషన్ | |
| feature | ఫీచర్ | |
| forum | ఫోరమ్ | |
| guide | గైడ్ | |
| improvement | మెరుగుదల | |
| issue | ఇష్యూ | a tracker item; for "problem" use సమస్య |
| issue tracker | ఇష్యూ ట్రాకర్ | |
| log in | లాగిన్ అవ్వు | |
| mailing list | మెయిలింగ్ లిస్ట్ | |
| patch | ప్యాచ్ | |
| problem | సమస్య | |
| release | విడుదల | |
| repository | రిపోజిటరీ | |
| translation | అనువాదం | |
| version | వెర్షన్ | |

## Core programming terms

| English | Telugu | Notes |
|---------|--------|-------|
| argument | ఆర్గ్యుమెంట్ | |
| attribute | అట్రిబ్యూట్ | |
| built-in | బిల్ట్-ఇన్ | e.g. బిల్ట్-ఇన్ ఫంక్షన్ |
| class | క్లాస్ | |
| code | కోడ్ | |
| command | కమాండ్ | |
| command line | కమాండ్ లైన్ | |
| exception | ఎక్సెప్షన్ | |
| error | లోపం | names like `SyntaxError` stay in English |
| expression | ఎక్స్‌ప్రెషన్ | |
| extension module | ఎక్స్‌టెన్షన్ మాడ్యూల్ | |
| function | ఫంక్షన్ | |
| interpreter | ఇంటర్‌ప్రెటర్ | |
| keyword | కీవర్డ్ | |
| loop | లూప్ | |
| method | మెథడ్ | |
| module | మాడ్యూల్ | |
| object | ఆబ్జెక్ట్ | |
| operator | ఆపరేటర్ | |
| package | ప్యాకేజీ | |
| parameter | పారామీటర్ | |
| program | ప్రోగ్రామ్ | |
| programming language | ప్రోగ్రామింగ్ భాష | |
| prompt | ప్రాంప్ట్ | |
| script | స్క్రిప్ట్ | |
| source code | సోర్స్ కోడ్ | |
| standard library | స్టాండర్డ్ లైబ్రరీ | |
| statement | స్టేట్‌మెంట్ | |
| syntax | సింటాక్స్ | |
| tutorial | ట్యుటోరియల్ | |
| value | విలువ | |
| variable | వేరియబుల్ | |

## Data types, files and environment

| English | Telugu | Notes |
|---------|--------|-------|
| dictionary | డిక్షనరీ | |
| directory | డైరెక్టరీ | |
| environment variable | ఎన్విరాన్‌మెంట్ వేరియబుల్ | |
| file | ఫైల్ | |
| floating-point number | ఫ్లోటింగ్-పాయింట్ సంఖ్య | |
| hardware | హార్డ్‌వేర్ | |
| input / output | ఇన్‌పుట్ / అవుట్‌పుట్ | |
| install | ఇన్‌స్టాల్ చేయు | |
| integer | పూర్ణాంకం | |
| list | లిస్ట్ | the Python type; for a general list use జాబితా |
| number | సంఖ్య | |
| operating system | ఆపరేటింగ్ సిస్టమ్ | |
| platform | ప్లాట్‌ఫామ్ | |
| set | సెట్ | |
| software | సాఫ్ట్‌వేర్ | |
| string | స్ట్రింగ్ | |
| tuple | టపుల్ | |
| virtual environment | వర్చువల్ ఎన్విరాన్‌మెంట్ | |
