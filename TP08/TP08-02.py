"""
-----------------------------------------------------------------------------------------------
Título: TP08-02 | DESCOMPOSICIÓN DE EMAIL
Fecha:
Autor: Joaquin Zanardi

Descripción: Desarrollar un programa que utilice una función que reciba como parámetro una cadena de caracteres conteniendo una 
dirección  de  correo  electrónico  y  devuelva  una  tupla  con  las  distintas  partes  que  componen  dicha  dirección.  Ejemplo: 
alguien@uade.edu.ar -> (alguien, uade, edu, ar) (T)
-----------------------------------------------------------------------------------------------
"""

def email_decomposition(email):
    local_part, domain = email.split('@')
    domain_parts = domain.split('.')
    email_parts = (local_part,) + tuple(domain_parts)
    
    return email_parts

email = "jzanardi@uade.edu.ar"
print(email_decomposition(email))