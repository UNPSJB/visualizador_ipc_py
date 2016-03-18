# Cambiar los nombres de los procesos

.PHONY: all

all: prog_a prog_b

# Compilar la librería de comunicaciones con Processing
comm.o: comm.c comm.h
	gcc -Wall -c comm.c -o $@

# Compilador genérico de archivos C
%: %.c comm.o
	gcc -o $@ $^
