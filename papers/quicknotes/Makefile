all:	data_MK2.tex
		mkdir -p out
		pdflatex -output-directory out data_MK2.tex

run:	out/data_MK2.pdf
		evince out/data_MK2.pdf &

clean:	out/data_MK2.pdf	
		rm -rf out/
