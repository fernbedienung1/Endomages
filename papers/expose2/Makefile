all:	expose.tex literature/lit.bib
	mkdir -p out
	pdflatex  -output-directory out expose.tex
	TEXMFOUTPUT="out:" bibtex out/expose.aux
	pdflatex  -output-directory out expose.tex
	pdflatex  -output-directory out expose.tex
run:	out/expose.pdf
	evince out/expose.pdf &	

clean:	
	rm -rf out/	
