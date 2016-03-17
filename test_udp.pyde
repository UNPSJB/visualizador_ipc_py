import socket
from thread import start_new_thread
from subprocess import call

server = None # Equivalente a null
 
def setup():
    # Necesario para que una variable global
    # sea modificada
    global server
    size(500, 500)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0', 2016))
    argv=()
    start_new_thread(escuchar, argv)
    noLoop()
    draw()

def draw():
    rect(10, 10, 10, 10)
    fill(128, 0, 0)
    text("Alfa", 40, 10)


def escuchar():
    print "Comenzando a escuchar"
    while True:
        data, quien = server.recvfrom(1024)
        print "Se recibió", data, "de", quien

def keyPressed():
    print "key pressed", key
    if key == 'm':
       output = call('make -C ./c', shell=True)
       print output
    else:
        call("./c/ejemplo_udp")