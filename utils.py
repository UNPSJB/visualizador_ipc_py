# encoding: utf-8
"""
Utilidades para ejecutar comandos.
"""
from subprocess import call, check_output, CalledProcessError
from thread import start_new_thread
from functools import partial
from threading import Thread

PLATAFORMA = check_output("uname -sm", shell=True).strip().lower().replace(' ', '.')

class ThreadCall(Thread):
    def __init__(self, command, shell=False):
        Thread.__init__(self)
        self.command = command
        self.shell = shell

    def __call__(self, *args, **kwargs):
        self.start(*args, **kwargs)

    def run(self):
        self.output = call(self.command, shell=self.shell)
        if self.output != 0:
            print "Error calling {}".format(self.command)

def bash(command):
    """
    Ejecuta un comando en un sub-proceso shell.
    """



def run_and_show_results(command, shell=False):
    result = call(command, shell=shell)
    if result != 0:
        print "Error calling {} => {}".format(command, result)

def call_in_thread(command, shell=False):
    """
    Ejecuta un comando en un hilo
    """
    command = command.format(plataforma=PLATAFORMA)
    start_new_thread(run_and_show_results, (command, shell))


def run(command, shell=False):
    """
    Llama a un proceso command en un thread y espera su
    finalización. Si es != 0 muestra el código con fines
    de depuración.
    """
    command = command.format(plataforma=PLATAFORMA)
    return partial(call_in_thread, command, shell)

