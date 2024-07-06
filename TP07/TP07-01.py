"""
-----------------------------------------------------------------------------------------------
Título: TP07-01 | DÍGITOS DE UN ENTERO
Fecha:
Autor: Joaquin Zanardi

Descripción: Escribir una función que devuelva la cantidad de dígitos de un número entero, sin utilizar cadenas de caracteres.
-----------------------------------------------------------------------------------------------
"""

def digit_count(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count

print(digit_count(12345))