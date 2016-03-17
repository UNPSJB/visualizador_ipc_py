all: ejemplo_udp

comm.o: comm.c
	gcc -Wall -c $^ -o $@

ejemplo_udp: ejemplo_udp.c comm.o
	gcc -o $@ $^
