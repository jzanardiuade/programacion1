"""
-----------------------------------------------------------------------------------------------
Título: TP00-08 | PROMEDIO DE TEMPERATURAS 
Fecha: 17-3-2024
Autor: Joaquin Zanardi

Descripción:
Realizar  un  programa  que  solicite  la  carga  de  las  temperaturas  de  todos  los  días  de  enero  y  al  finalizar  devuelva  la 
temperatura promedio, máxima y mínima del mes.

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

count = 1
temperaturas = []
while count < 32:
    temperatura = float(input(f"Ingrese la temperatura del día {count}: "))
    temperaturas.append(temperatura)
    count = count + 1

promedio = sum(temperaturas) / len(temperaturas)
print("Temperatura promedio del mes:", promedio)
print("Temperatura minima del mes:" ,min(temperaturas))
print("Temperatura maxima del mes:" ,max(temperaturas))