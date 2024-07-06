"""
-----------------------------------------------------------------------------------------------
Título: TP08-05 | PALABRAS ÚNICAS
Fecha:
Autor: Joaquin Zanardi

Descripción: Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de 
cada una. Finalmente mostrar las palabras ordenadas según su longitud. Los signos de puntuación no deben afectar el 
proceso. (C) 
-----------------------------------------------------------------------------------------------
"""

def unique_words():
    sentence = input("Ingrese una frase: ")
    symbols = ".,:;!?"
    clean_sentence = "".join(char for char in sentence if char not in symbols) 
    words = clean_sentence.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words, key=len)
    
    return sorted_words

print(unique_words())