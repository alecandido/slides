TEST_CSS := serif.css


%.css: source/%.scss
	sass --no-source-map $< $@

.PHONY: test install

install:
	mv *.css ../..

test: $(TEST_CSS)
	mv $(TEST_CSS) ../../test.css
