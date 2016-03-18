#include "comm.h"
#include <string.h> // strncpy
#include <unistd.h>


int main(int argc, char **argv)
{
    TMensaje m;
    int count = 10;

    iniciar(argc, argv, &m);

    while(count-- > 0)
    {
        strncpy(m.msg, "Hola que tal", 80);
        // Enviar el mensaje
        m.x = count;
        m.y = count +1;
        m.pid = getpid();
        enviar(&m);
        usleep(500000);
    }

    return 0;
}
