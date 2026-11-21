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
  shell session or program output) are copied into `msgstr` unchanged,
  except that comments (the text after `#`) are translated, so readers see
  exactly what Python prints. `#!` lines, encoding declarations and
  commented-out code stay in English, and the comment keeps its column.
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
| developer | డెవలపర్ | plural డెవలపర్‌లు |
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
| floating-point number | ఫ్లోటింగ్ పాయింట్ సంఖ్య | no hyphen, as in the stage 3 table |
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

## Terms for the rest of the tutorial (stage 4)

| English | Telugu | Notes |
|---------|--------|-------|
| alias | అలియాస్ | |
| approximation | ఉజ్జాయింపు | approximate value → సుమారు విలువ |
| base class / derived class | బేస్ క్లాస్ / డిరైవ్డ్ క్లాస్ | |
| binary / decimal fraction | బైనరీ భిన్నం / దశాంశ భిన్నం | |
| byte | బైట్ | plural బైట్‌లు |
| class / instance variable | క్లాస్ వేరియబుల్ / ఇన్‌స్టాన్స్ వేరియబుల్ | |
| clean-up action | క్లీన్-అప్ చర్య | |
| compression | కంప్రెషన్ | compress → కంప్రెస్ చేయు |
| exception chaining | ఎక్సెప్షన్ చైనింగ్ | |
| file object | ఫైల్ ఆబ్జెక్ట్ | |
| format (verb) | ఫార్మాట్ చేయు | formatted string literal → ఫార్మాట్ చేసిన స్ట్రింగ్ లిటరల్; f-string → f-స్ట్రింగ్ |
| garbage collection | గార్బేజ్ కలెక్షన్ | |
| generator / generator expression | జనరేటర్ / జనరేటర్ ఎక్స్‌ప్రెషన్ | |
| handle (an exception) | నిర్వహించు | exception handling → ఎక్సెప్షన్ నిర్వహణ |
| inheritance / multiple inheritance | ఇన్‌హెరిటెన్స్ / బహుళ ఇన్‌హెరిటెన్స్ | inherit → ఇన్‌హెరిట్ చేయు |
| logging | లాగింగ్ | |
| method object | మెథడ్ ఆబ్జెక్ట్ | |
| name mangling | నేమ్ మాంగ్లింగ్ | |
| override | ఓవర్‌రైడ్ చేయు | |
| precision | కచ్చితత్వం | |
| private variable | ప్రైవేట్ వేరియబుల్ | |
| regular expression | రెగ్యులర్ ఎక్స్‌ప్రెషన్ | |
| representation error | రిప్రజెంటేషన్ లోపం | |
| round / rounding | రౌండ్ చేయు / రౌండింగ్ | |
| serialize / deserialize | సీరియలైజ్ / డీసీరియలైజ్ చేయు | |
| syntax error | సింటాక్స్ లోపం | the class `SyntaxError` stays in English |
| template | టెంప్లేట్ | |
| thread / multi-threading | థ్రెడ్ / మల్టీ-థ్రెడింగ్ | |
| traceback | ట్రేస్‌బ్యాక్ | |
| unit test | యూనిట్ టెస్ట్ | |
| weak reference | వీక్ రిఫరెన్స్ | |
| wildcard | వైల్డ్‌కార్డ్ | |

### Words reviewers flagged as misleading

| English | Avoid | Use |
|---------|-------|-----|
| informal | అనధికారిక (= unofficial) | సరళమైన |
| unique (distinct values) | ప్రత్యేక (= special), పునరావృతం కాని (= not repeated) | విభిన్న |
| arbitrary (order) | యాదృచ్ఛిక (= random) | ఇష్టానుసార |
| member / element | సభ్యుడు (a person) | ఐటెమ్ / ఎలిమెంట్ |
| the caller | వారు (a person) | కాల్ చేసిన కోడ్ |
| discouraged | ప్రోత్సహించరు (= not encouraged) | ఉపయోగించవద్దని సిఫార్సు చేస్తారు |
| significant (digits, places) | ముఖ్యమైన / ప్రాముఖ్యత (= important) | సార్థక |
| informal "we" | మా (excludes the reader) | మన / మనం |
| email | ఈమెయిల్ | ఇమెయిల్ |
| implicit / implicitly | పరోక్ష (= indirect) | అంతర్లీన / అంతర్లీనంగా |

## Terms added while translating stage 4

| English | Telugu | Notes |
|---------|--------|-------|
| abstract data type | అబ్‌స్ట్రాక్ట్ డేటా టైప్ | |
| aliasing | అలియాసింగ్ | |
| append (file mode) | అపెండ్ చేయు | |
| arithmetic | అంకగణితం | |
| base (of a number system) | ఆధారం | |
| binding / rebind | బైండింగ్ / మళ్లీ బైండ్ చేయు | |
| bit / digit | బిట్ / అంకె | significant digits → సార్థక అంకెలు |
| callback | కాల్‌బ్యాక్ | |
| catch (an exception) | క్యాచ్ చేయు | |
| client | క్లయింట్ | |
| concurrency | కాన్కరెన్సీ | |
| data attribute | డేటా అట్రిబ్యూట్ | |
| debug / debugger | డీబగ్ చేయు / డీబగ్గర్ | |
| delimiter | డిలిమిటర్ | |
| enclosing (scope) | ఆవరించి ఉన్న | |
| exception group | ఎక్సెప్షన్ గ్రూప్ | |
| field | ఫీల్డ్ | |
| format specifier | ఫార్మాట్ స్పెసిఫైయర్ | |
| fraction | భిన్నం | numerator / denominator → లవం / హారం |
| handler | హ్యాండ్లర్ | |
| hexadecimal | హెక్సాడెసిమల్ | |
| hierarchy | హైరార్కీ | |
| identifier | ఐడెంటిఫైయర్ | |
| implementation (noun) | ఇంప్లిమెంటేషన్ | the verb stays రూపొందించు |
| instantiate / instantiation | ఇన్‌స్టాన్షియేట్ చేయు / ఇన్‌స్టాన్షియేషన్ | |
| invariant | ఇన్‌వేరియంట్ | |
| iterator protocol | ఇటరేటర్ ప్రోటోకాల్ | |
| mean / median | సగటు / మధ్యగతం | |
| member (C++) | మెంబర్ | not సభ్యుడు |
| method resolution order | మెథడ్ రిజల్యూషన్ ఆర్డర్ | |
| non-local | నాన్-లోకల్ | |
| note (on an exception) | నోట్ | |
| pad (a string) | ప్యాడ్ చేయు | |
| performance | పనితీరు | |
| pointer | పాయింటర్ | |
| quotient | భాగఫలం | |
| rational number | అకరణీయ సంఖ్య | |
| redirection | దారి మళ్లింపు | |
| representation | రిప్రజెంటేషన్ | |
| subclass / parent class | సబ్‌క్లాస్ / పేరెంట్ క్లాస్ | |
| text / binary mode | టెక్స్ట్ / బైనరీ మోడ్ | |
| truncate | కత్తిరించు | |
| unhandled exception | నిర్వహించని ఎక్సెప్షన్ | |
| wrapper | ర్యాపర్ | |

## Built-in functions terms (stage 5)

| English | Telugu | Notes |
|---------|--------|-------|
| abstract base class | అబ్‌స్ట్రాక్ట్ బేస్ క్లాస్ | |
| asynchronous iterator / iterable | అసింక్రొనస్ ఇటరేటర్ / ఇటరబుల్ | awaitable → అవెయిటబుల్ |
| audit event | ఆడిట్ ఈవెంట్ | raises an auditing event → ఆడిటింగ్ ఈవెంట్‌ను రైజ్ చేస్తుంది |
| buffer | బఫర్ | |
| bytes-like object | బైట్స్ లాంటి ఆబ్జెక్ట్ | |
| callable | కాలబుల్ | |
| class method / static method | క్లాస్ మెథడ్ / స్టాటిక్ మెథడ్ | |
| code object | కోడ్ ఆబ్జెక్ట్ | |
| coroutine | కోరూటీన్ | |
| decorator | డెకరేటర్ | |
| deprecated | డెప్రికేట్ చేయబడింది | "deprecated since version" is generated by Sphinx |
| descriptor | డిస్క్రిప్టర్ | |
| hash / hashable | హ్యాష్ / హ్యాషబుల్ | |
| metaclass | మెటాక్లాస్ | |
| property | ప్రాపర్టీ | |
| sentinel | సెంటినెల్ | |
| signature | సిగ్నేచర్ | |
| truth value testing | సత్యం విలువ పరీక్ష | |
| keyword-only argument | కీవర్డ్-మాత్రమే ఆర్గ్యుమెంట్ | matches పొజిషనల్-మాత్రమే |

Function names, parameter names (*iterable*, *key*, *default*) and
exception names stay in English; entries that are only a function name
in the overview table are copied unchanged.

## Terms added while translating stage 5

| English | Telugu | Notes |
|---------|--------|-------|
| absolute value | పరమ విలువ | |
| accessor / getter / setter / deleter | యాక్సెసర్ / గెటర్ / సెటర్ / డిలీటర్ | |
| bytecode | బైట్‌కోడ్ | |
| closure | క్లోజర్ | |
| coercion | కోర్షన్ | |
| exhausted (iterator) | అయిపోయిన | `:term:` link text: అయిపోయినప్పుడు &lt;exhausted&gt; |
| exponent | ఘాతాంకం | |
| file descriptor | ఫైల్ డిస్క్రిప్టర్ | |
| functionality | కార్యాచరణ | not పనితీరు (= performance) |
| identity (of an object) | ఐడెంటిటీ | |
| idiom | పద్ధతి | |
| import hook | ఇంపోర్ట్ హుక్ | |
| infinity | అనంతం | positive / negative → ధన / రుణ అనంతం |
| inverse | విలోమం | |
| lazy | లేజీ | |
| lookup | లుకప్ | |
| path-like object | పాత్ లాంటి ఆబ్జెక్ట్ | |
| pickle / pickling | పికిల్ చేయు / పికిలింగ్ | |
| proxy object | ప్రాక్సీ ఆబ్జెక్ట్ | |
| qualified name | క్వాలిఫైడ్ నేమ్ | |
| real part / real number | వాస్తవ భాగం / వాస్తవ సంఖ్య | |
| runtime | రన్‌టైమ్ | |
| superclass / sibling class | సూపర్‌క్లాస్ / సిబ్లింగ్ క్లాస్ | |
| type hint | టైప్ హింట్ | |
| unique (one of a kind) | ఏకైక | for "no other object has it" → ఇతర ఏ ఆబ్జెక్ట్‌కూ లేని |
| warning | హెచ్చరిక | |
