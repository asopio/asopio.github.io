PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

help:
	@echo 'Makefile for the Pelican site'
	@echo ''
	@echo 'Usage:'
	@echo '   make html           regenerate the web site'
	@echo '   make clean          remove the generated files'
	@echo '   make serve          serve site at http://localhost:8000'
	@echo '   make devserver      build and serve with autoreload'
	@echo '   make publish        generate using publishconf.py'
	@echo ''

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

serve:
	"$(PELICAN)" --listen --port 8000

devserver:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) --autoreload --listen --port 8000

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

.PHONY: html clean serve devserver publish help
