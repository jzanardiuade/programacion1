"""
-----------------------------------------------------------------------------------------------
Título: TP02-03 | ELEMENTOS NUMÉRICOS
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Desarrollar  cada  una  de  las  siguientes  funciones  y  escribir  un  programa  que  permita  verificar  su  funcionamiento, 
imprimiendo lo que devuelve cada función luego de invocar a cada una de ellas: 

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar 
de dos dígitos. 

b. Calcular y devolver el producto de todos los elementos de la lista anterior. 

c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la 
función lo recibe como parámetro. No utilizar listas auxiliares. 

d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa 
es [50, 17, 91, 17, 50].  
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

def crear_lista():
    lista = []
    for i in range(random.randint(10, 99)):
        lista.append(random.randint(1000, 9999))
    return lista

def eliminar_apariciones_de(n, lista):
    while n in lista:
        lista.remove(n)
    return lista
            
def lista_es_capicua(lista):
    return lista == lista[::-1]
    # es_capicua = True
    # for i in range(len(lista)):
    #     es_capicua = es_capicua and lista[i] == lista[len(lista)-i-1]
    # return es_capicua

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#---------------------------------------------
# -------------------------------------------------

lista_capicua = [50, 20, 10, 20, 50]
lista_no_capicua = [50, 20, 10, 30, 50]

print(lista_es_capicua(lista_capicua))
print(lista_es_capicua(lista_no_capicua))

## para testear eliminacion
# lista = crear_lista()
# lista_copia = lista[:]
# while len(lista) == len(lista_copia):
#     numero_a_eliminar = random.randint(1000, 9999)
#     print('-------------------------------------------------')
#     lista = crear_lista()
#     print(lista)
#     lista_copia = eliminar_apariciones_de(numero_a_eliminar, lista[:])
#     print(lista_copia)
# print(f'Numero eliminado: {numero_a_eliminar}')