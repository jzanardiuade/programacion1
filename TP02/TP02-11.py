"""
-----------------------------------------------------------------------------------------------
Título: TP02-11 | AZAR Y ELEMENTOS IMPARES
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Generar una lista  con números al azar entre 1 y 100 y crear una nueva lista con los elementos de  la primera que  sean 
impares. Imprimir las dos listas por pantalla. 
• Programa TP02-11A: El proceso deberá realizarse utilizando listas por comprensión. 
• Programa TP02-11B: El proceso deberá realizarse utilizando la función incorporada filter(). (investigarla)
"""

#-----------------------------------------------------------------------------------------------
#Pendientes:
#-----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

lista = [random.randint(1, 100) for i in range(10)]
impares = list(filter(lambda x: x % 2 != 0, lista))
print(impares)