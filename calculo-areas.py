#coding: utf8
#David Ortega Garcia
#01/03/2018
from match import pi
from subprocess import call
call('clear')

print """
Calculadora de areas:
---------------------
T)Triangulo
C)Círculo
"""

figura=input ("que figura quiere calcular(Escriba T o C)?")

if((figura!='T')(figura!='C')):
    print "No se puede calcular esa figura"
else:
    if(figura=='T'):
        base=input ("Escriba la base:")
        altura==input ("Escriba la altura:")
        
        if((base<=0)or(altura<=0)):
            print "No se puede calcular con numeros negativos"
        else:
            print "Un triangulo de base",base,"y altura",altura,"tiene un area de",base*altura/2
    else:
        radio=input("Escriba el radio:")
        
        if(radio<=0):
            print "No se puede calcular con numeros negativos"
        else:
            print "Un circulo de radio",radio,"tiene un area de",2*pi*radio 
