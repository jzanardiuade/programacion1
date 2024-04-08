"""
-----------------------------------------------------------------------------------------------
Título: TP01-04 | BILLETES SEGÚN VUELTO
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Un comercio de electrodomésticos necesita para su línea  de  cajas un programa que  le indique  al cajero el cambio que 
debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero 
recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que 
se minimice la cantidad de billetes. Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10. Emitir 
un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $3170 y se abona con $5000, el 
vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 billete de $200, 1 billete de $100 y 3 billetes de $10.
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

def calcular_billetes_5000(vuelto):
    billetes_5000 = vuelto // 5000
    return billetes_5000

def calcular_billetes_1000(vuelto):
    billetes_1000 = vuelto // 1000
    return billetes_1000

def calcular_billetes_500(vuelto):
    billetes_500 = vuelto // 500
    return billetes_500

def calcular_billetes_200(vuelto):
    billetes_200 = vuelto // 200
    return billetes_200

def calcular_billetes_100(vuelto):
    billetes_100 = vuelto // 100
    return billetes_100

def calcular_billetes_50(vuelto):
    billetes_50 = vuelto // 50
    return billetes_50

def calcular_billetes_10(vuelto):
    billetes_10 = vuelto // 10
    return billetes_10



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))

vuelto = dinero_recibido - total_compra
if vuelto < 0:
    print("El dinero recibido es insuficiente")
else:
    billetes_5000 = calcular_billetes_5000(vuelto)
    vuelto = vuelto - billetes_5000 * 5000
    billetes_1000 = calcular_billetes_1000(vuelto)
    vuelto = vuelto - billetes_1000 * 1000
    billetes_500 = calcular_billetes_500(vuelto)
    vuelto = vuelto - billetes_500 * 500
    billetes_200 = calcular_billetes_200(vuelto)
    vuelto = vuelto - billetes_200 * 200
    billetes_100 = calcular_billetes_100(vuelto)
    vuelto = vuelto - billetes_100 * 100
    billetes_50 = calcular_billetes_50(vuelto)
    vuelto = vuelto - billetes_50 * 50
    billetes_10 = calcular_billetes_10(vuelto)
    vuelto = vuelto - billetes_10 * 10

    print(f"El vuelto debe contener:")
    print(f"{billetes_5000} billetes de $5000")
    print(f"{billetes_1000} billetes de $1000")
    print(f"{billetes_500} billetes de $500")
    print(f"{billetes_200} billetes de $200")
    print(f"{billetes_100} billetes de $100")
    print(f"{billetes_50} billetes de $50")
    print(f"{billetes_10} billetes de $10")
