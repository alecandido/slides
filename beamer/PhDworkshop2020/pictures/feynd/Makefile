PDFS = $(patsubst %.tex,%.pdf,$(wildcard *.tex))

.PHONY: all clean

all: $(PDFS)

%.pdf : %.tex
	latexmk -pdflatex=lualatex -pdf $<
	latexmk -c

clean:
	latexmk -c
	rm -f *.pdf
