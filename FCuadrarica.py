# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 14:27:23 2021

@author: Julio C. Torreblanca
"""
#import numpy as np
from prettytable import PrettyTable



def raices_1( a:float , b: float, c: float ) -> list:
    """Esta función calcula las raíces de la ecuación cuadrática
    ax^2 + bx + c = 0 usando la fórmula 1 y regresa los valores de las 
    raices"""
    
    
    x1 = (-b + (b**2 - 4*a*c)**(1/2) )/ (2*a)
    x2 = (-b - (b**2 - 4*a*c)**(1/2) )/ (2*a)
    return x1,x2
    
    
def raices_2( a , b, c ) -> list:
    """Esta función calcula las raíces de la ecuación cuadrática
    ax^2 + bx + c = 0 usando la fórmula 2 y regresa los valores de las raices
    en forma de lista"""
    
    
    x1 = (-2 * c)/( b + (b**2 - 4*a*c)**(1/2) )
    x2 = (-2 * c)/( b - (b**2 - 4*a*c)**(1/2) )
    return x1,x2
    


#########Ahora imprimiremos las raíces ejemplo
a = 1
b = 1
c = 2
r1,r2 = raices_1(a,b,c)
s1,s2 = raices_2(a,b,c)

print(f"Las raíces usando la fórmula (1) son: x_1 = {r1:<.8} y x_2 = {r2:<.8}")
print(f"Las raíces usando la fórmula (2) son: x_1 = {s1:<.8} y x_2 = {s2:<.8}")

print("\n\n\n")



###########Esta parte evalua el inciso (b)
tabla = PrettyTable() #Define la tabla
tabla.title = "Raíces de la ecuación x^2 + x + 10^(-n) = 0" # Agrega el título a la tabla
tabla.field_names = ["n","x_1","x'_1","|x_1-x'_1|","x_2", "x'_2","|x_2-x'_2|"]# Le damos nombre a los compos 
n = 19 #valor del exponente máximo de c = 10^(-n) #n=19,a=10,b=1000000,c=2*-i
a = 10
b = 1000000
for i in range(1,n+1):
    c = 2**(-i)
    r1,r2 = raices_1(a,b,c)
    s1,s2 = raices_2(a,b,c)
    
    tabla.add_row([i,
                  f"{r1:<.3e}",f"{s1:<.3e}",f"{abs(r1-s1):<.3e}",
                  f"{r2:<.3e}",f"{s2:<.3e}",f"{abs(r2-s2):<.3e}"])#Inserta un elemento a la tabla

print(tabla)