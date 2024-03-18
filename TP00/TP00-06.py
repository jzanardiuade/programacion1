"""
-----------------------------------------------------------------------------------------------
Título: TP00-06 | PROMEDIO DE CURSO 
Fecha: 17-3-2024
Autor: Joaquin Zanardi

Descripción:
Realizar  un  programa  donde  se  vayan  ingresando  las  calificaciones  de  los  alumnos  de  un  curso.  Luego  de  ingresar  la 
calificación del último alumno, se ingresará un -1 para terminar la carga. El programa informará entonces la calificación 
promedio del curso

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
...


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

#
# ENTRADA DE DATOS
#

calificaciones = []
while True:
    calificacion = int(input("Ingrese la calificación del alumno: "))
    if calificacion == -1:
        break
    calificaciones.append(calificacion)

#
# PROCESOS
#
    
promedio = sum(calificaciones) / len(calificaciones)
print('El promedio del curso es de', promedio)
