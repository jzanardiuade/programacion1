import random
import math

"""
-----------------------------------------------------------------------------------------------
Título: TP05-03 | STOP DE CÓDIGO CON MANEJADOR DE EXCEPCIONES
Fecha:
Autor:

Descripción:
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de las teclas  Ctrl-C, lo que genera una 
excepción del tipo KeyboardInterrupt. Realizar un programa para imprimir los números enteros entre 1 y 100000, y que 
solicite confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

for num in range(10000):
    try:
        print(num)
    except KeyboardInterrupt:
        input('Presiona enter para terminar: ')
        break