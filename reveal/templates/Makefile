# Makefile to generate reveal.js presentations

SHELL=/bin/bash

REVEAL := $(wildcard reveal.js/*)
STRUCTURES := $(wildcard structures/*)
THEMES := $(wildcard themes/*)
MISC := $(wildcard misc/*)

SLIDES_SRC := $(wildcard my-reveal/src/*)

#PREVIEW_OUT := $(wildcard my-reveal/build/*)
PREVIEW_OUT := my-reveal/index.html
BUILD_OUT := $(wildcard my-reveal/build/*)

# ~~~~~~~
# TARGETS
# ~~~~~~~

all: preview

.PHONY: all framework view preview build inflate

# checkout custom framework
# =========================

framework: | $(REVEAL) $(STRUCTURES) $(REVEAL) $(MISC)
	git submodule update
	python3 make-scripts/make.py

# show the current presentation
# =============================

view:
	$(BROWSER) my-reveal/index.html

# build a presentation preview
# ============================

$(PREVIEW_OUT): $(SLIDES_SRC)
	python3 make-scripts/preview.py
	nohup python3 make-scripts/view.py > /dev/null 2>&1 &

preview: $(PREVIEW_OUT)
	@echo "Preview updated!"


# build a presentation release
# ============================

$(BUILD_OUT): $(SLIDES_SRC)
	python3 make-scripts/build.py

build: $(BUILD_OUT)
	@echo "Build finished!"
	#tar gzip my-reveal/build-tmp in my-reveal/build
	#delete my-reveal/build-tmp


# inflate back a presentation
# ===========================
# erasing the current environment

inflate:
	python3 make-scripts/inflate.py

# src checkpoint
# ==============

checkpoint:
	tar cvzf checkpoint.tar.gz my-reveal/src

restore:
	tar xvzf checkpoint.tar.gz my-reveal/src
	rm -f checkpoint.tar.gz
