"""
-----------------------------------------------------------------------------------------------
Título: TP04-04 | RELOJ 
Fecha:
Autor: Joaquin Zanardi

Descripción: Desarrollar un programa que pida un valor de hora, un valor de minuto, y un valor de segundo. A partir de esos valores 
mostrar un reloj digital en formato de display HH:MM:SS (cada valor siempre en 2 dígitos). El display deberá avanzar cada 
1 segundo como cualquier reloj digital (es decir que cuando los segundos superen los 59 volverán a 00 y se agregará un 
minuto, etc. Y lo mismo entre los minutos y las horas) 

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

hora = int(input("Ingrese la hora: "))
minuto = int(input("Ingrese el minuto: "))
segundo = int(input("Ingrese el segundo: "))

while True:
    print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
    sleep(1)
    segundo += 1
    if segundo == 60:
        segundo = 0
        minuto += 1
        if minuto == 60:
            minuto = 0
            hora += 1
            if hora == 24:
                hora = 0
                minuto = 0
                segundo = 0



