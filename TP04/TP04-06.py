"""
-----------------------------------------------------------------------------------------------
Título: TP04-06 | FILTRADO DE PALABRAS
Fecha:
Autor: Joaquin Zanardi

Descripción: Escribir una función filtrarPalabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva 
otra  cadena  con  las  palabras  que  tengan  N  o más  caracteres  de  la  cadena  original.  Escribir  también  un  programa  para 
verificar el comportamiento de la misma. Hacer tres versiones de la función, para cada uno de los siguientes casos: 
A. Utilizando ciclos normales y slicing. Sin utilizar el método split() 
B. Utilizando el método split() y ciclos normales
C. Utilizando el método split() y listas por comprensión
 

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

def filtrarPalabras_v1(frase, n):
    palabras = []
    palabra = ""
    for caracter in frase:
        if caracter != " ":
            palabra += caracter
        else:
            if len(palabra) >= n:
                palabras.append(palabra)
            palabra = ""
    if len(palabra) >= n:
        palabras.append(palabra)
    return " ".join(palabras)

def filtrarPalabras_v2(frase, n):
    palabras = []
    for palabra in frase.split():
        if len(palabra) >= n:
            palabras.append(palabra)
    return " ".join(palabras)

def filtrarPalabras_v3(frase, n):
    return " ".join([palabra for palabra in frase.split() if len(palabra) >= n])

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

frase = input("Ingrese una frase: ")
n = int(input("Ingrese un número: "))
print("Versión A:")
print(filtrarPalabras_v1(frase, n))
print("Versión B:")
print(filtrarPalabras_v2(frase, n))
print("Versión C:")
print(filtrarPalabras_v3(frase, n))


