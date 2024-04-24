"""
-----------------------------------------------------------------------------------------------
Título: TP02-13 | REGISTRO DE VISITAS DE SOCIOS
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Resolver el siguiente problema, utilizando funciones:  
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número de socio de cinco 
dígitos hasta ingresar un cero como fin de carga. 
Se solicita: 
a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe). 
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de 
entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron
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

def eliminarRepetidosDeLista(lista):
    lista_unicos = []
    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)
    return lista_unicos

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

socios = []
socio = 1
while socio != 0:
    socio = int(input("Ingrese el número de socio: "))
    if socio != 0:
        socios.append(socio)

socios_unicos = eliminarRepetidosDeLista(socios)

for socio in socios_unicos:
    print(f"El socio {socio} ingresó {socios.count(socio)} veces")

baja = int(input("Ingrese el número de socio que se dio de baja: "))
ingresos = socios.count(baja)
print(f"Antes de eliminar al socio {baja}: {socios}")
socios = [socio for socio in socios if socio != baja]
print(f"Después de eliminar al socio {baja}: {socios}")
print(f"Se eliminaron {ingresos} ingresos")
