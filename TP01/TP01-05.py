"""
-----------------------------------------------------------------------------------------------
Título: TP01-05 | OBLONGOS Y TRIANGULARES
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Escribir dos funciones separadas que reciban un número natural y devuelvan verdadero o falso según el número sea de 
alguna de las siguientes categorías: 
Función oblongo(): Informa si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener 
multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3. 
Función triangular(): Informa si un número es triangular. Un número se define como triangular si puede expresarse 
como la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número 
triangular porque se obtiene sumando 1+2+3+4. 

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


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

def oblongo(num):
    for i in range(1, num):
        if i * (i + 1) == num:
            return True
    return False

def triangular(num):
    total = 0
    i = 1
    while total < num:
        total += i
        i += 1
    return total == num

num = 6
print("El número", num, "es oblongo:", oblongo(num))