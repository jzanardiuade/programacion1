"""
-----------------------------------------------------------------------------------------------
Título: TP00-07 | FORMAS DE PAGO 
Fecha: 17-3-2024
Autor: Joaquin Zanardi

Descripción:
Escribir un programa que, ingresado el precio de lista de un producto, muestre cuanto le costará al cliente según todas 
las  opciones  de  pago  disponibles  (si  es  en  cuotas  además  del  precio  final  debe  mostrar  el  valor  de  cada  cuota).  Los 
descuentos o recargos según las formas de pago son los siguientes: 
En efectivo aplicar 10% de descuento 
Tarjeta 1 pago mantener el precio de lista 
Tarjeta 3 pagos recargar 5% 
Tarjeta 6 pagos recargar 10% 
Tarjeta 12 pagos recargar 15% 
Una vez mostrados los valores, el algoritmo debe esperar un nuevo ingreso, y sólo debe finalizar si se ingresa un precio 
de 0 pesos (en dicho caso debe terminar sin calcular nada). Se pide usar un tipo de bucle que evite tener que escribir el 
input dos veces. 

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



#
# PROCESOS
#

while True:
    precioDeLista = float(input("Ingrese el precio de lista del producto: "))
    if precioDeLista == 0:
        break
    print('En efectivo: ', precioDeLista * 0.9)
    print('Tarjeta 1 pago: ', precioDeLista)
    print('Tarjeta 3 pagos: ', precioDeLista * 1.05)
    print('Tarjeta 6 pagos: ', precioDeLista * 1.10)
    print('Tarjeta 12 pagos: ', precioDeLista * 1.15)