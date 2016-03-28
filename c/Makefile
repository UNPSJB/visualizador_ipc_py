# Cambiar los nombres de los procesos

BIN_TAIL=$(shell uname -sm | tr '[:upper:]' '[:lower:]' | sed 's/\s/\./')

.PHONY: all

EJECUTABLES=prog_a prog_b

all: ${EJECUTABLES}

# Compilar la librería de comunicaciones con Processing
comm.o: comm.c comm.h
	gcc -Wall -c comm.c -o $@

# Compilador genérico de archivos C
%: %.c comm.o
	gcc -o $@ $^

clean:
	@rm *.o ${EJECUTABLES}

re: clean all

debug:
	@echo ${BIN_TAIL}
