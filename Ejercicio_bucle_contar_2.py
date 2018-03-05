# coding:utf8
# David Ortega Garcia
# 02/03/2018

# Inicializaciones
salir = "N"
limite= input ("Hasta que limite amo?:")
num=1

if (limite<=0):
    salir="S"
while ( salir=="N" ):
    # Hago cosas
    print num

    # Incremento
    num=num+1
    # Activo indicador de salida si toca
    if ( num>limite ): # Condición de salida
        salir = "S"
