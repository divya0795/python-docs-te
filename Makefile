# Makefile for te Python Documentation
#
# Here is what you can do:
#
# - make  # Automatically build an HTML local version
# - make todo  # To list remaining tasks and show current progression
# - make verifs  # To check for correctness: wrapping, spelling
# - make wrap  # To rewrap modified files
# - make spell  # To check for spelling
# - make clean # To remove build artifacts
# - make fuzzy  # To find fuzzy strings
# - make merge  # To update all .po files to the latest CPython $(BRANCH) sources
# - make core  # To check core completion the way translations.python.org does
#
# Modes are: autobuild-stable, autobuild-dev, and autobuild-html

# Configuration

# The CPYTHON_CURRENT_COMMIT is the commit, in the cpython repository,
# from which we generated our po files.  We use it here so when we
# test build, we're building with the .rst files that generated our
# .po files.

CPYTHON_CURRENT_COMMIT := 4faf413224a1780f9ffa22aeb20acdb1e6f5300e
LANGUAGE := te
BRANCH := 3.14

EXCLUDED := \
	whatsnew/2.?.po \
	whatsnew/3.[0-10].po

# Internal variables

UPSTREAM := https://github.com/python/cpython

PYTHON := $(shell which python3)
MODE := html
POSPELL_TMP_DIR := .pospell/
JOBS := auto
ADDITIONAL_ARGS := --keep-going --color
SPHINXERRORHANDLING = -W

# Detect OS

ifeq '$(findstring ;,$(PATH))' ';'
    detected_OS := Windows
else
    detected_OS := $(shell uname 2>/dev/null || echo Unknown)
    detected_OS := $(patsubst CYGWIN%,Cygwin,$(detected_OS))
    detected_OS := $(patsubst MSYS%,MSYS,$(detected_OS))
    detected_OS := $(patsubst MINGW%,MSYS,$(detected_OS))
endif

ifeq ($(detected_OS),Darwin)        # Mac OS X
    CP_CMD := gcp                   # accessible with `brew install coreutils` or `brew upgrade coreutils`
else
    CP_CMD := cp
endif

.PHONY: all
all: ensure_prerequisites
	git -C venv/cpython checkout $(CPYTHON_CURRENT_COMMIT) || (git -C venv/cpython fetch && git -C venv/cpython checkout $(CPYTHON_CURRENT_COMMIT))
	mkdir -p locales/$(LANGUAGE)/LC_MESSAGES/
	$(CP_CMD) -u --parents *.po */*.po locales/$(LANGUAGE)/LC_MESSAGES/
	$(MAKE) -C venv/cpython/Doc/ \
	  JOBS='$(JOBS)'             \
	  SPHINXOPTS='-D locale_dirs=$(abspath locales) \
	  -D language=$(LANGUAGE)           \
	  -D gettext_compact=0              \
	  -D latex_engine=xelatex           \
	  -D latex_elements.inputenc=       \
	  -D latex_elements.fontenc=        \
	  $(ADDITIONAL_ARGS)'               \
	  SPHINXERRORHANDLING=$(SPHINXERRORHANDLING) \
	  $(MODE)
	@echo "Build success, open file://$(abspath venv/cpython/)/Doc/build/html/index.html or run 'make htmlview' to see them."


# We clone cpython/ inside venv/ because venv/ is the only directory
# excluded by cpython' Sphinx configuration.
venv/cpython/.git/HEAD:
	git clone https://github.com/python/cpython venv/cpython


.PHONY: ensure_prerequisites
ensure_prerequisites: venv/cpython/.git/HEAD
	@if ! (blurb help >/dev/null 2>&1 && sphinx-build --version >/dev/null 2>&1); then \
	    git -C venv/cpython/ checkout $(BRANCH); \
	    echo "You're missing dependencies please install:"; \
	    echo ""; \
	    echo "  python -m pip install -r venv/cpython/Doc/requirements.txt"; \
	    exit 1; \
	fi

.PHONY: htmlview
htmlview: MODE=htmlview
htmlview: all

# The documentation keeps changing upstream. translations.python.org measures
# this translation against .pot files built from the *latest* CPython sources
# of $(BRANCH), so new or changed upstream strings lower the core completion
# even when nothing changed here. "make merge" brings every .po file up to
# date (new strings untranslated, slightly changed ones fuzzy) and records the
# CPython commit in CPYTHON_CURRENT_COMMIT; "make core" reports what is left.
.PHONY: pot
pot: ensure_prerequisites
	git -C venv/cpython fetch origin $(BRANCH)
	git -C venv/cpython checkout --quiet FETCH_HEAD
	$(MAKE) -C venv/cpython/Doc gettext

.PHONY: merge
merge: pot
	$(PYTHON) scripts/merge_pot.py venv/cpython/Doc/build/gettext
	sed -i.bak "s/^CPYTHON_CURRENT_COMMIT := .*/CPYTHON_CURRENT_COMMIT := $$(git -C venv/cpython rev-parse HEAD)/" Makefile
	rm -f Makefile.bak

.PHONY: core
core: pot
	$(PYTHON) scripts/core_completion.py venv/cpython/Doc/build/gettext

.PHONY: todo
todo: ensure_prerequisites
	potodo --exclude venv .venv $(EXCLUDED)

.PHONY: wrap
wrap: ensure_prerequisites
	@echo "Re wrapping modified files"
	powrap -m

SRCS = $(shell git diff --name-only $(BRANCH) | grep '.po$$')
# foo/bar.po => $(POSPELL_TMP_DIR)/foo/bar.po.out
DESTS = $(addprefix $(POSPELL_TMP_DIR)/,$(addsuffix .out,$(SRCS)))

.PHONY: spell
spell: ensure_prerequisites $(DESTS)

.PHONY: line-length
line-length:
	@echo "Searching for long lines..."
	@$(PYTHON) -c 'import glob, sys; bad = [f"{f}:{n}: line too long: {l.rstrip()}" for f in sorted(glob.glob("*.po") + glob.glob("*/*.po")) for n, l in enumerate(open(f, encoding="utf-8"), 1) if len(l.rstrip("\n")) > 80 and l.count(" ") > 1]; print(*bad, sep="\n") if bad else None; sys.exit(1 if bad else 0)'

.PHONY: sphinx-lint
sphinx-lint:
	@echo "Checking all files using sphinx-lint..."
	@sphinx-lint --enable all --disable line-too-long *.po */*.po

$(POSPELL_TMP_DIR)/%.po.out: %.po dict
	@echo "Pospell checking $<..."
	@mkdir -p $(@D)
	pospell -p dict -l te_IN $< && touch $@

.PHONY: fuzzy
fuzzy: ensure_prerequisites
	potodo -f --exclude venv .venv $(EXCLUDED)

.PHONY: verifs
verifs: spell line-length sphinx-lint

.PHONY: clean
clean:
	@echo "Cleaning *.mo and $(POSPELL_TMP_DIR)"
	rm -rf $(POSPELL_TMP_DIR) locales/$(LANGUAGE)/LC_MESSAGES/
	find . -name '*.mo' -delete
	@echo "Cleaning build directory"
	$(MAKE) -C venv/cpython/Doc/ clean
