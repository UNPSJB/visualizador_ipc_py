
import sys
import socket
from utils import bash, run
from leer_struct import buscar_estructura
from subprocess import check_output, CalledProcessError, call
from thread import start_new_thread

ANCHO = 800
ALTO = 600
PUERTO = 2016
RXED = 0

# Definición de la estructura a partir de leer el 
# archivo común comm.h
TMensaje = buscar_estructura(
    archivo='./c/comm.h',
    nombre='TMensaje'
)

server = None # Equivalente a null

PROCESOS = {}

# Configuración de qué accion ejecutar
# cuando se actia el evento keyPressed
TECLAS = {
    'm': run('./run_make.sh'),
    '1': run('./c/prog_a.{plataforma}'),
    '2': run('./c/prog_b.{plataforma}'),
    'q': exit,
}

def setup():
    # Necesario para que una variable global
    # sea modificada
    global server
    size(ANCHO, ALTO)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0', PUERTO))
    argv=()
    start_new_thread(escuchar, argv)
    #noLoop()
    frameRate(24)
    draw()

def draw():
    background(0, 0, 0)
    fill(255, 255, 255)
    color(255, 255, 255)
    text(len(PROCESOS), 490, 0)
    for pid, proc in PROCESOS.iteritems():
        rect(proc.x, proc.y, 100, 100)
        #print (proc.x, proc.y, 100, 100)
        text(proc.prog_name, proc.x + 10, proc.y +10)
    mensaje = "Mensajes: {} Processos: {}".format(RXED, len(PROCESOS)) 
    text(mensaje, ANCHO - (8*len(mensaje)), ALTO - 30)
    

def escuchar():
    global RXED
    print "Comenzando a escuchar en %d" % PUERTO 
    while server:
        dato_crudo, quien = server.recvfrom(1024)
        # Para debug descomentar la siguiente línea
        print "Se recibió", dato_crudo, "de", quien
        m = TMensaje()
        m.unpack(str(dato_crudo))
        if m.estado == -1:
            if m.pid in PROCESOS:
                died = PROCESOS.pop(m.pid)
                print "Se fue", died
        else:
            # Se actualiza
            PROCESOS[m.pid] = m
        RXED += 1
        print "RXED: %d" % RXED

        # TODO: Hacer que no se llame a draw() más de 60 (o frameRate()) veces por segundo
        draw()

def keyPressed():
    """
    Cuando se presiona una tecla
    """
 
    if key in TECLAS:
        accion = TECLAS[key]
        if callable(accion):
            accion()
    else:
        print "{} no está en TECLAS".format(key)

