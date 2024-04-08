"""
-----------------------------------------------------------------------------------------------
Título: TP01-02 | FECHA VÁLIDA 
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Desarrollar  una  función  que  reciba tres  números  enteros  positivos  correspondientes  al  día,  mes  y  año  de  una  fecha,  y 
verifique si corresponden a una fecha válida. Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años 
bisiestos.  La  función  debe devolver True  o  False  según  la  fecha  sea  correcta o  no.  Realizar  también  un  programa  para 
verificar el comportamiento de la función. 
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
def mes_es_valido(mes):
    return mes >= 1 and mes <= 12

def mes_tiene_31_dias(mes):
    return mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12

def es_año_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def es_fecha_valida(dia, mes, año):
    if not mes_es_valido(mes):
        return False

    if mes == 2:
        if es_año_bisiesto(año):
            return dia >= 1 and dia <= 29
        else:
            return dia >= 1 and dia <= 28

    elif mes_tiene_31_dias(mes):
        return dia >= 1 and dia <= 31

    elif not mes_tiene_31_dias(mes):
        return dia >= 1 and dia <= 30

    else:
        return False
    
def imprimir_resultado_fecha_valida(dia, mes, año):
    if es_fecha_valida(dia, mes, año):
        print(f"La fecha {dia}/{mes}/{año} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{año} no es válida.")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

imprimir_resultado_fecha_valida(dia, mes, año)
