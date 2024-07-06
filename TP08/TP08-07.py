"""
-----------------------------------------------------------------------------------------------
Título: TP08-07 | CLAVE ENTERO Y VALOR ENTERO AL CUADRADO
Fecha:
Autor: Joaquin Zanardi

Descripción: Generar  e  imprimir  un  diccionario  donde  las  claves  sean  números enteros  entre  1 y 20  (ambos  incluidos)  y  los valores 
asociados sean el cuadrado de las claves. (D) 
-----------------------------------------------------------------------------------------------
"""

def square_dict():
    square_dict = {num: num ** 2 for num in range(1, 21)}
    return square_dict

print(square_dict())