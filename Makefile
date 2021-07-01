all: plot ppt post

plot:
	@echo 'Creating plots...'
	@python scripts/create_plots.py

ppt:
	@echo 'Creating powerpoint...'
	@./scripts/run_tex.sh
	
post:
	@echo 'Creating poster...'
	@pandoc -s --template poster/template/template.html -f markdown -t html poster/poster.md -o poster/poster.html
	@brave --headless --virtual-time-budget=10000 --disable-gpu -print-to-pdf=poster/poster.pdf  poster/poster.html

clean:
	@echo 'Removing plots, ppt & poster'
	rm presentation/presentation.pdf poster/poster.html poster/poster.html
