# Makefile to generate reveal.js presentations

SHELL=/bin/bash

REVEAL := $(wildcard reveal.js/*)
STRUCTURES := $(wildcard structures/*)
THEMES := $(wildcard themes/*)
MISC := $(wildcard misc/*)

SLIDES_SRC := $(wildcard _sandbox/src/*)

#PREVIEW_OUT := $(wildcard _sandbox/build/*)
PREVIEW_OUT := _sandbox/index.html
BUILD_OUT := $(wildcard _sandbox/build/*)

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
	$(BROWSER) _sandbox/index.html

# build a presentation preview
# ============================

$(PREVIEW_OUT): $(SLIDES_SRC)
	python3 make-scripts/preview.py
	nohup python3 make-scripts/view.py > /dev/null 2>&1 &

preview: $(PREVIEW_OUT)
	@echo "Preview updated!"


# build a presentation release
# ============================

#$(BUILD_OUT): $(SLIDES_SRC)
	#python3 make-scripts/build.py

build: $(BUILD_OUT)
	python3 make-scripts/build.py
	@echo "Build finished!"


# inflate back a presentation
# ===========================
# erasing the current environment

inflate:
	python3 make-scripts/inflate.py

# src checkpoint
# ==============

checkpoint:
	tar cvzf checkpoint.tar.gz _sandbox/src _sandbox/assets

restore:
	tar xvzf checkpoint.tar.gz
	rm -f checkpoint.tar.gz

update: 
	tar cvzf checkpoint.tar.gz _sandbox/src _sandbox/assets
	git submodule update
	python3 make-scripts/make.py
	tar xvzf checkpoint.tar.gz
	rm -f checkpoint.tar.gz
	python3 _sandbox/build_template.py
