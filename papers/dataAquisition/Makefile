all:	data.tex literature/lit.bib
	mkdir -p out
	pdflatex  -output-directory out data.tex
	TEXMFOUTPUT="out:" bibtex out/data.aux
	pdflatex  -output-directory out data.tex
	pdflatex  -output-directory out data.tex

run:	out/data.pdf
	evince out/data.pdf &	

clean:	
	rm -rf out/	
