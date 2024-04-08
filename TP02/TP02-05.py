"""
-----------------------------------------------------------------------------------------------
Título: TP02-05 | ELEMENTOS AL CUADRADO 
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Crear  una  lista  con  los  cuadrados  de  los  números  entre  1  y  N  (ambos  incluidos),  donde  N  se  ingresa  desde  el  teclado. 
Luego se solicita imprimir los últimos 10 valores de la lista. 
"""

#-----------------------------------------------------------------------------------------------
#Pendientes:
#-----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def cuadrados_hasta(n):
    cuadrados = []
    for i in range(1, n + 1):
        cuadrados.append(i**2)
    return cuadrados

def imprimir_ultimos_n_numeros(n, lista):
    if len(lista) < n:
        for i in range(len(lista)):
            print(f"{i+1})", lista[i])
    else:
        for i in range(len(lista)-n, len(lista)):
            print(f"{i-(len(lista)-n-1)})", lista[i])

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

cuadrados = []
numero = int(input("Ingrese un número: "))

cuadrados = cuadrados_hasta(numero)
imprimir_ultimos_n_numeros(2, cuadrados)