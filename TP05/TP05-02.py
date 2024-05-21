import random
import math

"""
-----------------------------------------------------------------------------------------------
Título: TP05-02 | MES NÚMERO A TEXTO CON MANEJADOR DE EXCEPCIONES
Fecha:
Autor:

Descripción:
Desarrollar  una  función  que  devuelva  una  cadena  de  caracteres  con  el  nombre  del  mes  cuyo  número  se  recibe  como 
parámetro. Los nombres de los meses deberán obtenerse de una lista de cadenas de caracteres inicializada dentro de la 
función. Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a 
través de excepciones.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def numToMes(numero):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    try:
        num = int(numero)
        if num < 1:
            raise
        return meses[num-1]
    except:
        return ''



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

mes = ''
while mes == '':
     mes = numToMes(input('Ingresa un numero de mes: '))

print(mes)
