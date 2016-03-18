#include "comm.h"
#include <string.h> // strncpy

int main(void)
{
    TMensaje m;
    int count = 10;

    iniciar();
    while(count-- > 0)
    {
        strncpy(m.msg, "Hola que tal", 80);
        //send the message
        enviar(&m);
    }

    return 0;
}
