"""
-----------------------------------------------------------------------------------------------
Título: TP00-03 | COBRO Y VUELTO 
Fecha: 17-3-2024
Autor: Joaquin Zanardi

Descripción:
Escribir un programa básico de caja, donde se ingrese el precio total de la compra, luego se ingrese el monto con el cual 
el cliente abona la compra, y finalmente informe con un mensaje si no es suficiente con lo que abonó o, caso contrario, 
informe el vuelto que se le debe dar al cliente.

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
precioTotalCompra = int(input("Ingrese el precio total de compra: "))
montoDePago = int(input("Ingrese el monto con el que el cliente pagó: "))

#
# PROCESOS
#
if montoDePago < precioTotalCompra:
    print("El monto ingresado no es suficiente")
else:
    print("El vuelto es de " + str(montoDePago - precioTotalCompra))