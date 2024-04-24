"""
-----------------------------------------------------------------------------------------------
Título: TP02-10 | ELEMENTOS IMPARES
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Utilizar la técnica de listas por comprensión para construir una lista con todos los números impares comprendidos entre 
100 y 200.
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

impares = [i for i in range(100, 201) if i % 2 != 0]
print(impares)