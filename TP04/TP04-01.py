"""
-----------------------------------------------------------------------------------------------
Título: TP04-01 | CADENA CAPICÚA
Fecha:
Autor: Joaquin Zanardi

Descripción: Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. 
Escribir además un programa que permita verificar su funcionamiento. 

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def es_capicua(cadena):
    return cadena == cadena[::-1]

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

cadena = input("Ingrese una cadena de caracteres: ")

if es_capicua(cadena):
    print("La cadena ingresada es capicúa.")

