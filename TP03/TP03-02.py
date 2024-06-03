"""
-----------------------------------------------------------------------------------------------
Título: TP03-02 | GENERACIÓN DE MATRICES CON PATRONES
Fecha: 
Autor: Joaquin Zanardi

Descripción:
Para cada una de las siguientes matrices, desarrollar una función que la genere. 
Escribir un programa con un menú que invoque a cada una de ellas y muestre por pantalla la matriz obtenida. El tamaño 
de las matrices debe establecerse como N x N solicitando el valor por teclado, y las funciones deben servir para cualquier 
valor ingresado. Antes de volver al menú detener el programa y continuar con ENTER. 

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

def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print()
    print()

def matrizA(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(2 * i + 1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

def matrizB(n):
    '''
        0 0 0 27
        0 0 9 0
        0 3 0 0
        1 0 0 0
    '''
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i + j == n - 1:
                fila.append(3 ** j)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

def matrizC(n):
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

# Menú de opciones
print("Seleccioná una opción:")
print("Matriz a")
print("Matriz b")
print("Matriz c")
print("Matriz d")
print("Matriz e")
print("Salir")
opcion = ""
n = 0

while opcion != "Salir":
    opcion = input("Opción: ")
    n = int(input("Ingresá el tamaño de la matriz: "))

    if opcion == "a":
        matriz = matrizA(n)
        imprimirMatriz(matriz)
    elif opcion == "b":
        matriz = matrizB(n)
        imprimirMatriz(matriz)
    elif opcion == "c":
        matriz = matrizC(n)
        imprimirMatriz(matriz)
    
    else:
        print("Opción inválida")

    
