all:	thesis.tex literature/lit.bib literature/thesis.gls
	mkdir -p out
	pdflatex  -interaction=nonstopmode -output-directory out thesis.tex
	makeglossaries -s /usr/share/texmf/tex/latex/glosstex/glosstex.sty out/thesis.glo
	TEXMFOUTPUT="out:" bibtex out/thesis.aux
	pdflatex  -interaction=nonstopmode -output-directory out thesis.tex
	pdflatex  -interaction=nonstopmode -output-directory out thesis.tex

debug:	thesis.tex literature/lit.bib literature/thesis.gls
	mkdir -p out
	pdflatex  -output-directory out thesis.tex
	makeglossaries -s /usr/share/texmf/tex/latex/glosstex/glosstex.sty out/thesis.glo
	TEXMFOUTPUT="out:" bibtex out/thesis.aux
	pdflatex  -output-directory out thesis.tex
	pdflatex  -output-directory out thesis.tex
	
run:	out/thesis.pdf
	evince out/thesis.pdf 2> /dev/null &

prev:	out/thesis.pdf
	evince -w out/thesis.pdf &

doc:	
	echo "This should create Doxygen of your code...."

clean:	
	rm -rf out/	
