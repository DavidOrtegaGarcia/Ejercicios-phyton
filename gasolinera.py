# coding: utf8
# David Ortega Garcia
# 22/02/2018

print "Tipos de gasolinas:"
print """
************************************** 
1)Super-Normal (1,5€)
2)Super-Turbo (1,55€)
3)Sin Plomo-Normal (1,6€)
4)Sin Plomo-Con aditivos (1,65€)
5)Diesel-Normal (1,7€)
6)Diesel-Fast&Furius (1,75€)
**************************************
"""

gasolina=input ("Elija el tipo de gasolina:")
litros=input ("Diga cuantos litros quiere:")

if (litros!=0):
    if (gasolina==1):
        print "El precio es", 1.5*litros,"€"
    if (gasolina==2):
        print "El precio es", 1.55*litros,"€"
    if (gasolina==3):
        print "El precio es", 1.6*litros,"€"
    if (gasolina==4):
        print "El precio es", 1.65*litros,"€"
    if (gasolina==5):
        print "El precio es", 1.7*litros,"€"
    if (gasolina==6):
        print "El precio es", 1.75*litros,"€"
else:
    print "El numero de litros no es correcto"
