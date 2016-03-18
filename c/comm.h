#ifndef _comm_h_
#define _comm_h_


/**
 * Modificar esta estructura para mostrar información útil
 */
typedef struct {
    int pid;
    int id;
    char msg[80];
    int x;
    int y;
    int status;
} TMensaje;


/**
 * Iniciar la comunicación con Processing.
 * Debe ser llamado antes de utilizar enviar.
 */
void iniciar(int argc, char **argv);
/**
 * Enviar un mensaje a Processing
 * @param m mensaje a ser enviado. Este mensaje está definido en el tipo TMensaje que
 *          puede ser modificado para agregar información útil de acuerdo al problema
 *          que se esté simulando.
 */
void enviar(TMensaje *m);

#endif
