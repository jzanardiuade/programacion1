"""
-----------------------------------------------------------------------------------------------
Título: TP07-02 | BINARIO A DECIMAL 
Fecha:
Autor: Joaquin Zanardi

Descripción: Desarrollar una función que reciba un número binario y lo devuelva convertido a base decimal.
-----------------------------------------------------------------------------------------------
"""

def binary_to_decimal(binary):
    decimal = 0
    for i, digit in enumerate(reversed(str(binary))):
        decimal += int(digit) * 2**i
    return decimal

print(binary_to_decimal(1010))
