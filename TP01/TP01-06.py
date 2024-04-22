"""
-----------------------------------------------------------------------------------------------
Título: TP01-06 | CONCATENAR BÁSICO
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva el número que resulte de 
concatenar ambos valores. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades 
de Python no vistas en clase, ni tampoco concatenar strings mediante la conversión de número a cadena.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def concatenate_numbers(num1, num2):
    power_of_10 = 1
    while power_of_10 <= num2:
        power_of_10 *= 10
    return num1 * power_of_10 + num2

print(concatenate_numbers(1234, 567))