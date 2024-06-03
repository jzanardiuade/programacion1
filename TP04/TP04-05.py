"""
-----------------------------------------------------------------------------------------------
Título: TP04-05 | TEMPORIZADOR
Fecha:
Autor: Joaquin Zanardi

Descripción: Desarrollar un programa que pida un valor de minuto, y un valor de segundo. A partir de esos valores mostrar un reloj 
digital  en  formato  de  display  MM:SS  (cada  valor  siempre  en 2  dígitos).  El  display  deberá  ir en  cuenta  regresiva  cada 1 
segundo hasta llegar a 00:00. Cuando llegue a cero deberá detenerse y mostrar el mensaje “<<<< TIEMPO >>>>” 

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from time import sleep

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))
segundos_totales = minutos * 60 + segundos

for i in range(segundos_totales, -1, -1):
    minutos = i // 60
    segundos = i % 60
    print(f"{minutos:02}:{segundos:02}")
    sleep(1)

print("<<<< TIEMPO >>>>")


