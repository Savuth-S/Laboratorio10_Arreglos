# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8 11:49:21 2020

@author: Savuth S.
"""

###Funciones
def a_power_b(n1,n2):
    for i in range(0,n2,1):
        n1 *= n1
    return n1
    
###Programa Principal
#Declaración de variables
pot = 1
pot_cont = 0
par = 0
imp = 0

while pot > 0 or pot < 0:
    pot = int(input("Ingrese el numero que desea elevar: \n\n"))
    elv = int(input("\n\nIngrese la potencia a la que desea elevar el numero: \n\n"))
    resu = a_power_b(pot,elv)
    
    if resu % 2 == 0:
        par += 1
    else:
        imp += 1
    
    pot_cont += 1
    print("\n\nEl resultado es: "+ str(resu))

print("\n\nSe calcularon "+ str(pot_cont) +" potencias")
print("\nHubieron "+ str(par) +" resultados pares")
print("\nHubieron "+ str(imp) +" resultados imppares")