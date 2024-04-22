"""
-----------------------------------------------------------------------------------------------
Título: TP02-06 | ELEMENTOS ELIMINADOS
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Escribí un programa donde se declare dentro del mismo código una lista con todas las materias que estás cursado en la 
Eliminar  de  una  lista  de  números  enteros  aquellos  valores  que  se  encuentren  en  una  segunda  lista.  Imprimir  la  lista 
original, la lista de valores a eliminar y la lista resultante. La función deben modificar la lista original sin crear una copia 
modificada.
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

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]

valores_a_eliminar = [2, 4, 6, 8]

for valor in valores_a_eliminar:
    if valor in lista_original:
        lista_original.remove(valor)

print("Lista original:", lista_original)
print("Valores a eliminar:", valores_a_eliminar)
print("Lista resultante:", lista_original)