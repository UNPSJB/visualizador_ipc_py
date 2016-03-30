.PHONY: procesos

all: html
# Compila los procesos para IPC
procesos:
	make -C ./c

html:
	pandoc readme.md -o readme.html --template docs/templates/template.html --css docs/templates/template.css --self-contained --toc --toc-depth 2
