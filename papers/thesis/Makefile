all:	thesis.tex literature/lit.bib
	mkdir -p out
	pdflatex  -interaction=nonstopmode -output-directory out thesis.tex
	TEXMFOUTPUT="out:" bibtex out/thesis.aux
	pdflatex  -interaction=nonstopmode -output-directory out thesis.tex
	pdflatex  -interaction=nonstopmode -output-directory out thesis.tex

run:	out/thesis.pdf
	evince out/thesis.pdf 2> /dev/null &

prev:	out/thesis.pdf
	evince -w out/thesis.pdf &

doc:	
	echo "This should create Doxygen of your code...."

clean:	
	rm -rf out/	
