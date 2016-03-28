# Cambiar los nombres de los procesos

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
