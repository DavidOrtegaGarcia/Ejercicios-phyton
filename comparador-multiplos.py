# coding: utf8
# David Ortega Garcia
# 09/02/2018

num1= input ("Escriba un numero:")
num2= input ("Escriba otro numero:")

if ((num1==0) or(num2==0)):
    print "Error"
else:
    if (num1>num2):
        mayor=num1
        menor=num2
    else:
        mayor=num2
        menor=num1
    if (mayor%menor==0):
        print mayor,"es multiple de",menor
    else:
        print mayor,"no es multiple de",menor
