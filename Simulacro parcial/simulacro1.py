"""
-----------------------------------------------------------------------------------------------
Título: 
Fecha: 
Autor: Nombre alumno (matrícula)

Descripción:

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
def generarLanzamientos():
    """
    Devuelve una lista de números aleatorios simulando lanzamientos del juego de ruleta.
    """
    lanz = []
    cantNumeros = int(input('Ingrese la cantidad de lanzamientos [de 10 a 30]: '))
    while True:
        if cantNumeros < 10 or cantNumeros > 30:
            cantNumeros = int(input('El valor ingresado es inválido, vuelva a intentar [de 10 a 30]: '))
        else:
            break
    for i in range(cantNumeros):
        lanz.append(random.randint(0, 36))
    return lanz
    
    


def informarVecesGanaBanca(lanzamientos):
    """
    A partir de la lista de valores de lanzamientos recibida,
    devuelve la cantidad de veces que salió el O (cero).
    """
    cantCeros = 0
    for i in lanzamientos:
        if i == 0:
            cantCeros += 1
    return cantCeros


def informarCuandoGanaBanca(lanzamientos):
    """
    A partir de la lista de valores de lanzamientos recibida,
    devuelve en qué números de lanzamiento salió el 0 (cero).
    """
    cuandoGana = []
    for i in range(len(lanzamientos)):
        if lanzamientos[i] == 0:
            cuandoGana.append(i+1)
    return cuandoGana


def informarOtrasEstadisticas(lanzamientos):
    """
    A partir de la lista de valores de lanzamientos recibida,
    devuelve 3 estadísticas, sobre valores pares, impares y promedio.
    """

    ...
    cantPares, pares = recibirPares(lanzamientos) 
    cantImpares, impares = recibirImpares(lanzamientos)
    return cantPares, pares, cantImpares, impares, promedioLista(lanzamientos)

def recibirPares(lanzamientos):
    pares = [i for i in lanzamientos if i % 2 == 0]
    return len(pares), pares

def recibirImpares(lanzamientos):
    impares = [i for i in lanzamientos if i % 2 != 0]
    return len(impares), impares

def promedioLista(lanzamientos):
    suma = 0
    for i in lanzamientos:
        suma += i
    return suma/len(lanzamientos)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#----------------------------------------------------------------------------------------------
lanzamientos = [] # Esta lista se utiliza en el programa principal para almacenar los números generados del juego de ruleta


#-------------------------------------------------
# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Generar lanzamientos simulados de ruleta")
        print("[2] Informar veces que gana la banca")
        print("[3] Informar en qué lanzamientos gana la banca")
        print("[4] Mostrar otras estadísticas")
        print("---------------------------")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3","4"): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

    if opcion == "0": # Opción salir del programa
        exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    elif opcion == "1":   # Opción 1
        lanzamientos = generarLanzamientos()
        print('Lanzamientos:\n', lanzamientos)

        
    elif opcion == "2":   # Opción 2
        ganadasBanca = informarVecesGanaBanca(lanzamientos.copy())
        print(f'La banca gana ', ganadasBanca, ' veces')
        
    elif opcion == "3":   # Opción 3
        cuandoGanaBanca = informarCuandoGanaBanca(lanzamientos.copy())
        if len(cuandoGanaBanca) > 0:
            print('La banca gana en los lanzamientos ', cuandoGanaBanca)
        else:
            print('La banca no gana en ningún lanzamiento')
        
    elif opcion == "4":   # Opción 4
        cantPares, pares, cantImpares, impares, promedio = informarOtrasEstadisticas(lanzamientos.copy())
        print('Lanzamientos pares: ', cantPares, ' ', pares)
        print('Lanzamientos impares: ', cantImpares, ' ', impares)
        print('Valor promedio:', promedio)

    print()
    input("\nPresione ENTER para volver al menú.")
    print("\n\n")

