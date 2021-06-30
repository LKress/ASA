#!/bin/bash

pdflatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory="presentation/tex_output"  "presentation/presentation.tex"

bibtex presentation/tex_output/presentation

pdflatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory="presentation/tex_output"  "presentation/presentation.tex"

pdflatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory="presentation/tex_output"  "presentation/presentation.tex"

mv presentation/tex_output/presentation.pdf presentation