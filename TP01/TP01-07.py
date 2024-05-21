"""
-----------------------------------------------------------------------------------------------
Título: TP01-07 | DÍA SIGUIENTE
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Escribir  una  función  diaSiguiente()  que  reciba  como  parámetro  una  fecha  cualquiera  expresada  por  tres  enteros 
(correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes el día siguiente al dado. Utilizando 
esta misma función, sin modificaciones ni agregados, desarrollar programas que permitan: 
• Programa TP01-07A: Sumar N días a una fecha. 
• Programa TP01-07B: Calcular la cantidad de días existentes entre dos fechas cualesquiera

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def diaSiguiente(dia, mes, anio):
    if mes == 2:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            if dia == 29:
                dia = 1
                mes += 1
            else:
                dia += 1
        else:
            if dia == 28:
                dia = 1
                mes += 1
            else:
                dia += 1
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia == 30:
            dia = 1
            mes += 1
        else:
            dia += 1
    else:
        if dia == 31:
            dia = 1
            if mes == 12:
                mes = 1
                anio += 1
            else:
                mes += 1
        else:
            dia += 1
    return dia, mes, anio

def sumarNDias(dia, mes, anio, n):
    for i in range(n):
        dia, mes, anio = diaSiguiente(dia, mes, anio)
    return dia, mes, anio

def cantidadDiasEntreFechas(dia1, mes1, anio1, dia2, mes2, anio2):
    dias = 0
    while dia1 != dia2 or mes1 != mes2 or anio1 != anio2:
        dia1, mes1, anio1 = diaSiguiente(dia1, mes1, anio1)
        dias += 1
    return dias


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

# Programa TP01-07A
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
n = int(input("Ingrese la cantidad de días a sumar: "))
dia, mes, anio = sumarNDias(dia, mes, anio, n)
print(f"La fecha resultante es: {dia}/{mes}/{anio}")
