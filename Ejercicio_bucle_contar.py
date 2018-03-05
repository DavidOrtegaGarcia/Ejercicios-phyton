# coding:utf8
# David Ortega Garcia
# 02/03/2018
# Inicializaciones
salir = "N"
num= 1

while ( salir=="N" ):
    # Hago cosas
    print num

    # Incremento
    num=num+1
    # Activo indicador de salida si toca
    if ( num>50): # Condición de salida
            salir = "S"
