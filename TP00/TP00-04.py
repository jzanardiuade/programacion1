"""
-----------------------------------------------------------------------------------------------
Título: TP00-04 | AUMENTO DE LÍMITES DE TARJETAS 
Fecha: 17-3-2024
Autor: Joaquin Zanardi

Descripción:
Un banco necesita establecer los nuevos límites de crédito de sus tarjetas. Las de tipo 1 aumentarán un 25%; las de tipo 
2 aumentarán un 35%; las de tipo 3 aumentarán un 40%, y las de cualquier otro tipo aumentarán un 50%. Desarrollar un 
algoritmo para calcular el nuevo límite según el límite actual y el tipo de tarjeta del cliente.

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

aumentos = {1: 25, 2: 35, 3: 40}
tipoTarjeta = int(input("Ingrese el tipo de tarjeta: "))
limiteActual = int(input("Ingrese el límite actual de la tarjeta: "))

#
# PROCESOS
#

if tipoTarjeta in aumentos:
    nuevoLimite = limiteActual + (limiteActual * aumentos[tipoTarjeta] / 100)
else:
    nuevoLimite = limiteActual + (limiteActual * 50 / 100)

print('El limite viejo era de', limiteActual, 'y el nuevo limite es de', nuevoLimite)