import random

"""
-----------------------------------------------------------------------------------------------
Título: TP02-04 | ELEMENTOS REPETIDOS
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Escribir funciones para: 
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa a través del teclado. 
b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no 
debe modificar la lista. 
c. Recibir  una  lista  como  parámetro  y  devolver  una  nueva  lista  con  los  elementos  únicos  de  la  lista  original,  sin 
importar el orden
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


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def generate_random_list(n):
    return [random.randint(1, 100) for _ in range(n)]

def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                return True
    return False

def get_unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst

def main():
    n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    random_lst = generate_random_list(n)
    print(random_lst)
    print(has_duplicates(random_lst))
    print(get_unique_elements(random_lst))