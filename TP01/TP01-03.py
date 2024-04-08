"""
-----------------------------------------------------------------------------------------------
Título: TP01-03 | GASTO DE TRANSPORTE SUBT
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que 
dicho  medio  de  transporte  utiliza  un  esquema  de  tarifas  decrecientes  (detalladas  en  la  tabla  de  abajo)  se  solicita 
desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el 
total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.

Cantidad de viajes      Valor de 1 pasaje 
1 a 20                  150
21 a 30                 20% de descuento 
31 a 40                 30% de descuento 
41 o más                40% de descuento

"""

#----------------------------------------------------------------------------------------------
#Pendientes:
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def calcular_gasto_con_limite(valor_pasaje, cantidad_de_viajes):
    if cantidad_de_viajes < 1:
        return 0
    if cantidad_de_viajes > 20:
        return (valor_pasaje * 20)
    return (valor_pasaje * cantidad_de_viajes)

def calcular_gasto_sin_limite(valor_pasaje, cantidad_de_viajes):
    if cantidad_de_viajes < 1:
        return 0
    return (valor_pasaje * cantidad_de_viajes)

def aplicar_descuento(descuento, gasto):
    return gasto * (1 - descuento)

def calcular_gasto_total(valor_pasaje, cantidad_de_viajes):
    sin_descuento = 0.0
    descuento_20 = 0.2
    descuento_30 = 0.3
    descuento_40 = 0.4

    gasto_total = 0
    cantidad_viajes_a_calcular = cantidad_de_viajes
    gasto_total += aplicar_descuento(sin_descuento, calcular_gasto_con_limite(valor_pasaje, cantidad_viajes_a_calcular))
    cantidad_viajes_a_calcular -= 20
    gasto_total += aplicar_descuento(descuento_20, calcular_gasto_con_limite(valor_pasaje, cantidad_viajes_a_calcular))
    cantidad_viajes_a_calcular -= 10
    gasto_total += aplicar_descuento(descuento_30, calcular_gasto_con_limite(valor_pasaje, cantidad_viajes_a_calcular))
    cantidad_viajes_a_calcular -= 10
    gasto_total += aplicar_descuento(descuento_40, calcular_gasto_sin_limite(valor_pasaje, cantidad_viajes_a_calcular))
    return gasto_total

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

valor_pasaje = 150
cantidad_de_viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
print("El gasto total en viajes fue de: $", calcular_gasto_total(valor_pasaje, cantidad_de_viajes))

