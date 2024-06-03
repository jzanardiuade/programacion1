"""
-----------------------------------------------------------------------------------------------
Título: 
TP03-03 | MATRIZ ALEATORIA SIN REPETICIONES
Fecha: 
Autor: Joaquin Zanardi

Descripción:
Desarrollar  un  programa  para  rellenar  una matriz  de  N  x  N  con  números  enteros  al  azar  comprendidos en  el  intervalo 
[0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("\n")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------


n = int(input("Ingrese el tamaño de la matriz: "))
matriz = [[0 for i in range(n)] for j in range(n)]

numersGenerados = []
for i in range(n):
    for j in range(n):
        randomNum = random.randint(0, n**2)
        while randomNum in numersGenerados:
            randomNum = random.randint(0, n**2)
        numersGenerados.append(randomNum)
        matriz[i][j] = randomNum
        
imprimir_matriz(matriz)
