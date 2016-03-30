.PHONY: procesos

MDS=$(shell find ./ -iname "*.md")
TARGETS    = $(patsubst %.md,%.html, $(MDS))


all: html
# Compila los procesos para IPC
procesos:
	make -C ./c

html: ${TARGETS}

%.html: %.md
	pandoc $^ -o $@ --template docs/templates/template.html --css docs/templates/template.css --self-contained --toc --toc-depth 2

clean:
	-rm ${TARGETS}

re: clean all
debug:
	@echo ${MDS}
	@echo ${TARGETS}
