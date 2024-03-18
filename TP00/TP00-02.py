"""
-----------------------------------------------------------------------------------------------
Título: TP00-02 | ASIENTOS DE CONFERENCIA
Fecha: 17-3-2024
Autor: Joaquin Zanardi

Descripción:
Realizar  un  programa  que  permita  ingresar  la  cantidad  de  inscriptos  a  una  conferencia  y  la  cantidad  de  asientos 
disponibles en el auditorio. Se debe indicar si alcanzan los asientos. Si los asientos no alcanzan, indicar cuantos faltan para 
que todos los inscriptos puedan sentarse.  

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
inscriptos = int(input("Ingresa la cantidad de inscriptos: "))
cantidadAsientos = int(input("Ingresa la cantidad de asientos: "))

#
# PROCESOS
#
if inscriptos <= cantidadAsientos:
    print("Hay asientos suficientes")
else:
    print("Faltan " + str(inscriptos - cantidadAsientos) + " asientos")
