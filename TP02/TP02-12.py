"""
-----------------------------------------------------------------------------------------------
Título: TP02-12 | ATENCIÓN DE PACIENTES EN CLÍNICA 
Fecha:23/3/2024
Autor: Joaquin Zanardi

Descripción:
Resolver el siguiente problema, diseñando las funciones a utilizar: 
Una  clínica  necesita  un  programa  para  atender  a  sus  pacientes.  Cada  paciente  que  ingresa  se  anuncia  en  la  recepción 
indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un 
0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita: 
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en 
el orden que llegaron a la clínica. 
b. Realizar la búsqueda de  un número de  afiliado e  informar cuántas veces  fue  atendido por turno y cuántas por 
urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.
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


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

pacientes = []
afiliado = 0
while afiliado != -1:
    afiliado = int(input("Ingrese el número de afiliado: "))
    if afiliado != -1:
        tipo = int(input("Ingrese 0 si es urgencia o 1 si es con turno: "))
        pacientes.append((afiliado, tipo))

urgencias = [paciente for paciente in pacientes if paciente[1] == 0]
turnos = [paciente for paciente in pacientes if paciente[1] == 1]

print("Pacientes atendidos por urgencia:")
for paciente in urgencias:
    print(paciente[0])

print("Pacientes atendidos por turno:")
for paciente in turnos:
    print(paciente[0])
