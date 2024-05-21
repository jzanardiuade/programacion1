import random
import math

"""
-----------------------------------------------------------------------------------------------
Título: TP05-04 | RAIZ CUADRADA CON MANEJADOR DE EXCEPCIONES
Fecha:
Autor:

Descripción:
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del módulo math. Escribir un programa que 
utilice esta función para calcular la raíz cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número negativo.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import math


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

try:
    num = float(input("Ingrese un número: "))
    if num < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        raiz = math.sqrt(num)
        print(f"La raíz cuadrada de {num} es {raiz}")
except ValueError as e:
    print(e)