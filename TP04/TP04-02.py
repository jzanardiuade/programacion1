"""
-----------------------------------------------------------------------------------------------
Título: TP04-02 | TEXTO CENTRADO EN PANTALLA
Fecha:
Autor: Joaquin Zanardi

Descripción: Leer  una  cadena  de  caracteres  e  imprimirla  centrada  rellenando  a  izquierda  y  derecha  con  guiones  para cubrir  toda  la 
pantalla. Suponer que la pantalla tiene 80 columnas. En el mismo programa hacer 3 versiones: una sin utilizar facilidades 
de Python, otra usando la facilidad de función o método incorporado, y otra usando la facilidad de f-strings.

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

def centrar_texto(cadena):
    largo = len(cadena)
    margen = (80 - largo) // 2
    print("-" * margen + cadena + "-" * margen)

def centrar_texto_v2(cadena):
    print(cadena.center(80, "-"))

def centrar_texto_v3(cadena):
    print(f"{cadena:-^80}")


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

cadena = input("Ingrese una cadena de caracteres: ")

centrar_texto(cadena)
centrar_texto_v2(cadena)
centrar_texto_v3(cadena)

