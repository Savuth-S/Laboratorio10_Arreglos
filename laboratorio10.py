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

while pot > 0 or pot < 0:
    pot = int(input("Ingrese el numero que desea elevar: \n\n"))
    elv = int(input("\n\nIngrese la potencia a la que desea elevar el numero: \n\n"))
    
    print("\n\nEl resultado es: "+ str(a_power_b(pot,elv)))