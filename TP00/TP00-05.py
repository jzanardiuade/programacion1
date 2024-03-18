"""
-----------------------------------------------------------------------------------------------
Título: TP00-05 | COMPRA TOTAL Y CANTIDAD 
Fecha: 17-3-2024
Autor: Joaquin Zanardi

Descripción:
En un mercado los clientes pueden comprar sólo una unidad de cada producto. Realizar un programa que pida uno por 
uno los precios de los productos comprados por el cliente, y que al ingresar un precio igual a cero muestre el total  que 
debe abonar por la compra y la cantidad de productos comprados.

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
prices = []
while True:
    price = float(input("Ingrese el precio del producto (ingrese 0 para finalizar): "))
    if price == 0:
        break
    prices.append(price)

#
# PROCESOS
#
total = sum(prices)
cantidad = len(prices)

print("Total a abonar:", total)
print("Cantidad de productos comprados:", cantidad)