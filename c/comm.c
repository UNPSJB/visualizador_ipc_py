#include <stdio.h> //printf
#include <string.h> //memset
#include <stdlib.h> //exit(0) atexit()
#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>

#include "comm.h"
#define SERVER "127.0.0.1"
#define BUFLEN 512
#define PORT 2016

struct sockaddr_in si_other;
int s, 
    i, 
    slen, 
    id=0 /* Identificado de mensaje */;
char prog_name[BUFLEN];
char buf[BUFLEN];
char message[BUFLEN];

void die(char *s)
{
    perror(s);
    exit(1);
}

void close_socket(void) {
    close(s);
}


void iniciar(int argc, char **argv) {
    if (argc) {
        strncpy(prog_name, argv[0], sizeof(prog_name)-1);
    }
    slen = sizeof(si_other);
    if ((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
    {
        die("socket");
    }
    memset((char *) &si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = htons(PORT);

    if (inet_aton(SERVER , &si_other.sin_addr) == 0)
    {
        fprintf(stderr, "inet_aton() failed\n");
        exit(1);
    }
    atexit(close_socket);
}


void enviar(TMensaje *m) {
    m->pid = getpid();
    m->id = id++;
    if (sendto(s, m, sizeof(TMensaje) , 0 , (struct sockaddr *) &si_other, slen)==-1)
    {
        die("sendto()");
    }
}

