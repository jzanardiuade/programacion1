"""
-----------------------------------------------------------------------------------------------
Título: TP02-08 | LISTA NORMALIZADA 
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Escribir  una  función  que  reciba  una  lista  de  números  enteros  como  parámetro  y  la  normalice,  es  decir  que  todos  sus 
elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar 
también  un  programa  que  permita  verificar  el  comportamiento  de  la  función.  Por  ejemplo,  normalizar([1,  1,  2])  debe 
devolver [0.25, 0.25, 0.50].
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
def normalize_list(numbers):
    total = sum(numbers)
    normalized_list = []
    for num in numbers:
        normalized_list.append(num / total)
    return normalized_list

numbers = [1, 1, 2]
normalized_numbers = normalize_list(numbers)
print(normalized_numbers)