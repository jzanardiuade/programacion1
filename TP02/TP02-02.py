"""
-----------------------------------------------------------------------------------------------
Título: TP02-02 | MES NÚMERO A TEXTO
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Escribir una función que reciba un número de mes y devuelva una cadena con el nombre del mes. 
Probar la función desde un programa principal con un input para la entrada del número de mes, luego la llamada a la 
función con dicho número como argumento, y finalmente un print de lo que la función devuelve.
"""

#-----------------------------------------------------------------------------------------------
#Pendientes:
#-----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def nombre_de_mes(n):
    if n < 1 or n > 12:
        return 'Mes invalido'
    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ]
    return meses[n-1]

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
numero_mes = int(input('Ingrese un numero de mes: '))
print(nombre_de_mes(numero_mes))