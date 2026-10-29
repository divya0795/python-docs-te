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
- **Plurals** of transliterated words take the Telugu ‌లు ending
  (వేరియబుల్‌లు, టూల్‌లు, ఫుట్‌నోట్‌లు), not the English -s (వేరియబుల్స్).
- **Code samples and terminal output** (entries that are only code, a
  shell session or program output) are copied into `msgstr` unchanged, so
  the file counts as translated and readers see exactly what Python prints.
- **Sentences split around a code block** may be re-split at a natural
  point for Telugu word order (the verb usually ends up after the code).
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

## Tutorial terms

| English | Telugu | Notes |
|---------|--------|-------|
| activate / deactivate | యాక్టివేట్ / డీయాక్టివేట్ చేయు | |
| application | అప్లికేషన్ | |
| call (a function) | కాల్ చేయు | |
| character | అక్షరం | |
| comment (in code) | కామెంట్ | |
| compile | కంపైల్ చేయు | |
| completion | కంప్లీషన్ | as in tab completion |
| data structure | డేటా స్ట్రక్చర్ | |
| data type | డేటా టైప్ | |
| default | డిఫాల్ట్ | డిఫాల్ట్‌గా = by default |
| encoding | ఎన్‌కోడింగ్ | |
| environment | ఎన్విరాన్‌మెంట్ | |
| error message | లోప సందేశం | |
| executable | ఎగ్జిక్యూటబుల్ | |
| execute | అమలు చేయు | |
| exit status | ఎగ్జిట్ స్టేటస్ | |
| high-level | ఉన్నత-స్థాయి | |
| history (command history) | హిస్టరీ | |
| import | ఇంపోర్ట్ చేయు | |
| indentation | ఇండెంటేషన్ | |
| interactive mode | ఇంటరాక్టివ్ మోడ్ | |
| library | లైబ్రరీ | |
| option (command-line) | ఆప్షన్ | |
| path | పాత్ | |
| primary / secondary prompt | ప్రైమరీ / సెకండరీ ప్రాంప్ట్ | |
| run | రన్ చేయు | |
| shell | షెల్ | |
| stack trace | స్టాక్ ట్రేస్ | |
| standard input / output / error | స్టాండర్డ్ ఇన్‌పుట్ / అవుట్‌పుట్ / ఎర్రర్ | names of streams |
| third-party | థర్డ్-పార్టీ | |
| upgrade | అప్‌గ్రేడ్ చేయు | |
| implement | రూపొందించు | not అమలు చేయు, which means "execute" |
| user | వినియోగదారు | in fixed names (user interface, user guide, user directory, user site-packages) use యూజర్ |
| user-defined | వినియోగదారు నిర్వచించిన | |

## Core tutorial terms (stage 3)

| English | Telugu | Notes |
|---------|--------|-------|
| annotation | అనొటేషన్ | function annotations |
| assignment | అసైన్‌మెంట్ | assign a value → విలువను కేటాయించు |
| block (of code) | బ్లాక్ | |
| body (of a loop/function) | బాడీ | |
| Boolean | బూలియన్ | `True`/`False` stay in English |
| clause | క్లాజ్ | `else` clause → `else` క్లాజ్ |
| comparison | పోలిక | compare → పోల్చు |
| concatenate | కలుపు | concatenation → కలపడం |
| condition | షరతు | |
| default value | డిఫాల్ట్ విలువ | default argument value → డిఫాల్ట్ ఆర్గ్యుమెంట్ విలువ |
| definition | నిర్వచనం | function definition → ఫంక్షన్ నిర్వచనం |
| docstring | డాక్‌స్ట్రింగ్ | |
| division | భాగహారం | floor division → ఫ్లోర్ డివిజన్ |
| element / item | ఎలిమెంట్ / ఐటెమ్ | |
| immutable / mutable | ఇమ్యూటబుల్ / మ్యూటబుల్ | add (మార్చలేని / మార్చగలిగే) at first use in a file |
| index (noun) | ఇండెక్స్ | plural ఇండెక్స్‌లు |
| iterable / iterator | ఇటరబుల్ / ఇటరేటర్ | |
| iterate / iteration | ఇటరేట్ చేయు / ఇటరేషన్ | |
| key (in a dict) | కీ | key-value pair → కీ-విలువ జత |
| keyword argument | కీవర్డ్ ఆర్గ్యుమెంట్ | |
| lambda expression | లాంబ్డా ఎక్స్‌ప్రెషన్ | |
| list comprehension | లిస్ట్ కాంప్రహెన్షన్ | |
| namespace | నేమ్‌స్పేస్ | |
| nested | నెస్టెడ్ | |
| operand | ఆపరాండ్ | |
| pattern (matching) | ప్యాటర్న్ | pattern matching → ప్యాటర్న్ మ్యాచింగ్ |
| positional argument | పొజిషనల్ ఆర్గ్యుమెంట్ | positional-only → పొజిషనల్-మాత్రమే |
| queue / stack | క్యూ / స్టాక్ | |
| recursion | రికర్షన్ | |
| remainder | శేషం | |
| result | ఫలితం | |
| return (a value) | రిటర్న్ చేయు | return value → రిటర్న్ విలువ |
| scope | స్కోప్ | |
| search path | సెర్చ్ పాత్ | module search path → మాడ్యూల్ సెర్చ్ పాత్ |
| sequence | సీక్వెన్స్ | |
| slice / slicing | స్లైస్ / స్లైసింగ్ | |
| submodule | సబ్‌మాడ్యూల్ | |
| symbol table | సింబల్ టేబుల్ | |
| type | టైప్ | data type → డేటా టైప్ |
| unpacking | అన్‌ప్యాకింగ్ | |

## Terms added while translating stage 3

| English | Telugu | Notes |
|---------|--------|-------|
| true / false (truth values) | సత్యం / అసత్యం | the objects `True`/`False` stay in English; "truthy" also → సత్యం |
| parentheses `()` | కుండలీకరణాలు | |
| brackets `[]` | బ్రాకెట్‌లు | also for the generic "bracketing" |
| curly braces `{}` | కర్లీ బ్రేస్‌లు | |
| absolute / relative import | అబ్సొల్యూట్ / రిలేటివ్ ఇంపోర్ట్ | |
| arithmetic progression | అంకశ్రేణి | |
| bind | బైండ్ చేయు / బైండ్ అవు | |
| cache | క్యాష్ (చేయు) | |
| calling convention | కాలింగ్ కన్వెన్షన్ | |
| capture (in patterns) | క్యాప్చర్ చేయు | |
| collection | కలెక్షన్ | for Python's collection types; a plain "collection of …" → సమాహారం |
| complex number | సంకీర్ణ సంఖ్య | imaginary part → ఊహాజనిత భాగం (to be reviewed) |
| compound (statement, type) | సంయుక్త | |
| constant | స్థిరాంకం | |
| constructor | కన్‌స్ట్రక్టర్ | |
| container | కంటెయినర్ | |
| control flow | కంట్రోల్ ఫ్లో | |
| duplicate | పునరావృత | |
| escape (a character) | ఎస్కేప్ చేయు | |
| evaluate | ఎవాల్యుయేట్ చేయు | |
| export | ఎక్స్‌పోర్ట్ చేయు | |
| floating point | ఫ్లోటింగ్ పాయింట్ | |
| formal parameter | ఫార్మల్ పారామీటర్ | |
| global / local | గ్లోబల్ / లోకల్ | |
| guard (in `match`) | గార్డ్ | |
| in place | అక్కడికక్కడే | |
| initialize | ఇనిషియలైజ్ చేయు | |
| instance | ఇన్‌స్టాన్స్ | |
| lexicographical ordering | నిఘంటు క్రమం | |
| literal | లిటరల్ | plural లిటరల్‌లు |
| mapping | మ్యాపింగ్ | |
| membership test | సభ్యత్వ పరీక్ష | |
| multiple assignment | బహుళ అసైన్‌మెంట్ | |
| negative / non-negative | రుణ / రుణం కాని | |
| newline | న్యూలైన్ | |
| optional | ఐచ్ఛిక | |
| placeholder | ప్లేస్‌హోల్డర్ | |
| power (exponent) | ఘాతం | |
| precedence / priority | ప్రాధాన్యత | |
| raise (an exception) | రైజ్ చేయు | |
| raw string | రా స్ట్రింగ్ | |
| read-only | రీడ్-ఓన్లీ | |
| shadow (a name) | కప్పివేయు | |
| shallow copy | షాలో కాపీ | |
| short-circuit | షార్ట్-సర్క్యూట్ | |
| side effect | సైడ్ ఎఫెక్ట్ | no hyphen |
| sort | సార్ట్ చేయు | |
| subject (of `match`) | సబ్జెక్ట్ | |
| subpackage / subpattern | సబ్‌ప్యాకేజీ / సబ్‌ప్యాటర్న్ | |
| subsequence / substring | ఉప-సీక్వెన్స్ / సబ్‌స్ట్రింగ్ | |
| suffix / prefix | సఫిక్స్ / ప్రిఫిక్స్ | |
| symbolic link | సింబాలిక్ లింక్ | |
| top level | టాప్ లెవెల్ | |
| variant | రూపాంతరం | |
| whitespace | ఖాళీ స్థలం | |
