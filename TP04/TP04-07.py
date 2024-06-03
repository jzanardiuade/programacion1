"""
-----------------------------------------------------------------------------------------------
Título: TP04-07 | PUNTO CADA 3 DÍGITOS
Fecha:
Autor: Joaquin Zanardi

Descripción: Escribir una función que reciba una cadena que contiene un número entero de muchos dígitos y devuelva una cadena con 
el mismo número, pero con los puntos de las separaciones de miles. Por ejemplo, si recibe 1234567890, debe devolver 
1.234.567.890

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

def agregar_puntos(numero):
    largo = len(numero)
    puntos = largo // 3
    if largo % 3 == 0:
        puntos -= 1
    nuevo_numero = ""
    for i in range(largo):
        nuevo_numero += numero[i]
        if (largo - i) % 3 == 1 and i != largo - 1:
            nuevo_numero += "."
    return nuevo_numero

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

numero = input("Ingrese un número entero de muchos dígitos: ")

print(agregar_puntos(numero))


