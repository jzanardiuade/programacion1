"""
-----------------------------------------------------------------------------------------------
Título: TP01-01 | MAYOR ENTRE TRES NÚMEROS 
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor 
estricto).  En  caso  de  no  existir  el  mayor  estricto  devolver  -1.  No  utilizar  operadores  lógicos  (and,  or,  not).  Desarrollar 
también  un  programa  para  ingresar  los  tres  valores,  invocar  a  la  función  y  mostrar  el  máximo  hallado,  o  un  mensaje 
informativo si éste no existe. 

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def tieneUnIgual(max, a, b):
    if max == a:
        return True
    if max == b:
        return True
    return False

def esMayorEstricto(num1, num2, num3):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
        
    if mayor == num1:
        if tieneUnIgual(mayor, num2, num3):
            return -1
    if mayor == num2:
        if tieneUnIgual(mayor, num1, num3):
            return -1
    if mayor == num3:
        if tieneUnIgual(mayor, num1, num2):
            return -1
    return mayor

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor = esMayorEstricto(num1, num2, num3)
print(f"El mayor número es: {mayor}")
