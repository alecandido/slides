# Makefile to generate reveal.js presentations

REVEAL := $(wildcard reveal.js/*) 
STRUCTURES := $(wildcard structures/*) 
THEMES := $(wildcard themes/*) 
MISC := $(wildcard misc/*)

SLIDES_SRC := $(wildcard my-reveal/src/*)

PREVIEW_OUT := $(wildcard my-reveal/build/*)
BUILD_OUT := $(wildcard my-reveal/build/*)

.PHONY: framework preview build


# checkout custom framework

framework: | $(REVEAL) $(STRUCTURES) $(REVEAL) $(MISC)
	git submodule update
	python3 make.py


# build a presentation preview

$(PREVIEW_OUT): $(SLIDES_SRC)
	python3 preview.py

preview: $(PREVIEW_OUT)
	@echo "Preview updated!"


# build a presentation release

$(BUILD_OUT): $(SLIDES_SRC)
	python3 preview.py

build: $(BUILD_OUT)
	@echo "Build finished!"
	python3 build.py
	#tar gzip my-reveal/build-tmp in my-reveal/build
	#delete my-reveal/build-tmp
