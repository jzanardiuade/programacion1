"""
-----------------------------------------------------------------------------------------------
Título: TP02-09 | INTERCALACIÓN DE ELEMENTOS
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Intercalar los elementos de una lista entre los elementos de otra. La intercalación podrá realizarse utilizando el método 
insert o mediante la técnica de rebanadas (slicing), y nunca se creará una lista nueva, sino que se modificará la primera. 
Por  ejemplo,  si  lista1 =  [8, 1, 3] y  lista2  =  [5, 9,  7],  lista1  deberá  quedar  como  [8,  5, 1, 9,  3, 7].  Las  listas  pueden  tener 
distintas longitudes.
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

lista1 = [2, 2, 2]
lista2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(len(lista2)):
    lista1.insert(i*2+1, lista2[i])

print(lista1)