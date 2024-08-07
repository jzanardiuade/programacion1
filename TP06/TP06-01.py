"""
-----------------------------------------------------------------------------------------------
Título: TP06-01 | APELLIDOS POR PAÍS
Fecha:
Autor: Joaquin Zanardi

Descripción: Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, 
Nombre" y guarde en el archivo ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la cadena 
"IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo ESPAÑA.TXT los terminados en "EZ". Descartar el 
resto. Ejemplo: 
Arslanian, Gustavo -> ARMENIA.TXT 
Rossini, Giuseppe -> ITALIA.TXT 
Pérez, Juan  -> ESPAÑA.TXT 
Smith, John  -> descartar 
El archivo de entrada puede ser creado mediante el Block de Notas o Notepad++. No escribir un programa para 
generarlo. 
-----------------------------------------------------------------------------------------------
"""

# comentario
names_file = open("nombres.txt", "r")
for line in names_file:
    print(line)
    apellido, nombre = line.split(", ")

    if apellido[-3:] == "ian":
        file = open("ARMENIA.TXT", "a")
        file.write(f'{apellido}, {nombre}\n')
        file.close()
    elif apellido[-3:] == "ini":
        file = open("ITALIA.TXT", "a")
        file.write(f'{apellido}, {nombre}\n')
        file.close()
    elif apellido[-2:] == "ez":
        file = open("ESPAÑA.TXT", "a")
        file.write(f'{apellido}, {nombre}\n')
        file.close()
    else:
        pass