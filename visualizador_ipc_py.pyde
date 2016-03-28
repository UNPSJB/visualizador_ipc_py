import sys
import socket
from thread import start_new_thread
from subprocess import call, check_output, CalledProcessError
from leer_struct import buscar_estructura

ANCHO = 800
ALTO = 600
PUERTO = 2016
RXED = 0
import os; print os.getcwd()
TMensaje = buscar_estructura(
    archivo='./c/comm.h',
    nombre='TMensaje'
)

server = None # Equivalente a null

PROCESOS = {}

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
    frameRate(2)
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
        print proc.pid 
    

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
        # Se actualiza
        PROCESOS[m.pid] = m
        RXED += 1
        print RXED

        # TODO: Hacer que no se llame a draw() más de 60 (o frameRate()) veces por segundo
        draw()

def keyPressed():
    """
    Cuando se presiona una tecla
    """
    print "key pressed", key
    if key == 'm':
        run_make()
    elif key == '1':
        run_prog('./c/prog_a')
    elif key == '2':
        run_prog('./c/prog_b')
    elif key == 'q':
        exit()
        
def run_make():
    print "Ejecutando Make"
    try:
        output = check_output('make -C ./c', shell=True)
    except CalledProcessError as e:
        print "ERROR", e
        print e.output

def run_prog(prog):
    def func():
        print "Lanznado %s" % prog
        print call(prog, shell=True)
        
    start_new_thread(func, tuple())
    
def stop():
    """
    Cerrar el socket cuando el proceso termina
    """
    global server
    print "Cerrando"
    try:
        server.close()
        server = None
    except:
        pass