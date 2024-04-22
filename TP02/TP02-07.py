"""
-----------------------------------------------------------------------------------------------
Título: TP02-07 | VERIFICAR ORDEN DE ELEMENTOS
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Escribí un programa donde se declare dentro del mismo código una lista con todas las materias que estás cursado en la 
facultad (no es necesario cargarla con input). A continuación, programar un bucle para listar por pantalla dichas 
materias, cada materia en una línea.  
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

def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Programa de prueba
lista1 = [1, 2, 3]
lista2 = ['b', 'a']

print(ordenada(lista1))
print(ordenada(lista2))