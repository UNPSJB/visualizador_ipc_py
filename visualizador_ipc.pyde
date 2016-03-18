import sys
import socket
from thread import start_new_thread
from subprocess import call
from leer_struct import buscar_estructura

ANCHO = 800
ALTO = 600

TMensaje = buscar_estructura(
    archivo='./c/comm.h',
    nombre='TMensaje'
)
print TMensaje

server = None # Equivalente a null

PROCESOS = {}

def setup():
    # Necesario para que una variable global
    # sea modificada
    global server
    size(ANCHO, ALTO)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0', 2016))
    argv=()
    start_new_thread(escuchar, argv)
    noLoop()
    draw()

def draw():
    background(0, 0, 0)
    fill(255, 255, 255)
    rect(10, 10, 10, 10)
    text("Alfa", 40, 10)


def escuchar():
    print "Comenzando a escuchar"
    while True:
        dato_crudo, quien = server.recvfrom(1024)
        #print "Se recibió", data, "de", quien
        m = TMensaje()
        m.unpack(dato_crudo)
        #print m.pid, m.x, m.y
        PROCESOS[m.pid] = {
            "x": m.x,
            "y": m.y,
        }

def keyPressed():
    print "key pressed", key
    if key == 'm':
        run_make()
    else:
        run_prog('./c/ejemplo_udp')
        
def run_make():
    print "Ejecutando Make"
    output = call('make -C ./c', shell=True)
    print output

def run_prog(prog):
    def func():
        call(prog, shell=True)
    start_new_thread(func, tuple())