plot:
	@python scripts/create_plots.py
ppt:
	@pandoc -t beamer presentation/presentation.md -o presentation/presentation.pdf
post:
	@pandoc -s --template poster/template/template.html -f markdown -t html poster/poster.md -o poster/poster.html
	@brave --headless --disable-gpu -print-to-pdf=poster/poster.pdf  poster/poster.html
