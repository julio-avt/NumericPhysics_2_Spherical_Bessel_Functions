# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:35:06 2021

@author: Julio C. Torreblanca
"""
from collections import deque
from numpy import sin, cos
from scipy.special import spherical_jn
from prettytable import PrettyTable



def bessel_esf_up(l: int, x: float) -> float:
    """Esta función utiliza una relación de recurrencia para calcular el valor
    numérico de la función de bessel esférica siguente a partir de las dos 
    anteriores"""

    
    j = [sin(x)/x, sin(x)/x**2 - cos(x)/x]
    
    for i in range (1,l):
        j_sig = (2*i+1)/x * j[i] - j[i-1]
        j.append(j_sig)
    
    return j[l]
    
def tabla_bessel_up(x: float):
    """Esta función imprime una tabla con los valores numéticos para las
    primeras 25 funciones de bessel esféricas calculadas por la relación de 
    recurrencia up y también ponr la función de bessel integrada por la 
    librería scipy. Además las compara y obtiene el error relativo."""
    
    tabla = PrettyTable()
    tabla.title = (f"Bessel esférico método up: x = {x}")
    tabla.field_names = ['j_l', 'Up', 'Scipy', 'Error relativo']

    for i in range(0, 26):
        error = abs(bessel_esf_up(i, x) - spherical_jn(i, x))/spherical_jn(i, x)
        tabla.add_row([f"j_{i}",
                    f"{bessel_esf_up(i, x):<.8e}",
                    f"{spherical_jn(i, x):<.8e}", 
                    f"{error:<.8e}"])    
    print(tabla)
    
    
def bessel_esf_down(l: int, x = 1) -> float:
    """Esta función utiliza el algoritmo de Miller para obtener obtener 
    los valores numéricos de las primeros l<50 funciones de Bessel esféricas"""
    
    n = 25
    j = deque([1,2])#En la posición 0 siempre tendremos al j_99 y en 1 al j_100
    
    
    for i in range(0,n):
        j_ant = (2*(n - i) + 1)/x * j[0] - j[1]
        j.appendleft(j_ant)        
        
    normalizacion = (sin(x)/x)/j[0]
    j[l] = j[l]*normalizacion
    return j[l]     

def tabla_bessel_down(x: float):
    """Esta función imprime una tabla con los valores numéricos para las
    primeras 25 funciones de bessel esféricas calculadas por el algoritmo de 
    Miller."""
    
    tabla = PrettyTable()
    tabla.title = (f"Bessel esférico método down: x = {x}")
    tabla.field_names = ['j_l', 'Down', 'Scipy', 'Error relativo']

    for i in range(0, 26):
        error = abs(bessel_esf_down(i, x) - spherical_jn(i, x))/spherical_jn(i, x)
        tabla.add_row([f"j_{i}",
                    f"{bessel_esf_down(i, x):<.15e}",
                    f"{spherical_jn(i, x):<.15e}", 
                    f"{error:<.15e}"])    
    print(tabla)
              
def bessel_esf_down_ajuste(x: float) -> deque:
    """Esta función utiliza una el algoritmo de Miller para obtener obtener 
    los valores numéricos de las primeros 25 funciones de Bessel esféricas 
    con un error relativo menor a 10^(-10)"""
    
    n = 25  #Se inicia en 25 pq queremos los primeros 25 valores
    error = 1
    j = deque([1,2])
    
    while error > 10**(-10):
        for i in range(0,n):
            j_ant = (2*(n - i) + 1)/x * j[0] - j[1]
            j.appendleft(j_ant)   
        
        normalizacion = (sin(x)/x)/j[0]
        for i in range(0,26):
            j[i] = j[i]*normalizacion
        
        error = abs( ( j[25] - spherical_jn(25, x) )/ spherical_jn(25, x) )
        n += 1
        print(n)
    return j

def tabla_bessel_down_ajuste(x: float):
    """Esta función imprime una tabla con los valores numéricos para las
    primeras 25 funciones de bessel esféricas calculadas por el algoritmo de 
    Miller con un error relativo menor a 10^(-10)"""
    
    tabla = PrettyTable()
    tabla.title = (f"Bessel esférico método down con ajuste: x = {x}")
    tabla.field_names = ['j_l', 'Down', 'Scipy', 'Error relativo']
    j = bessel_esf_down_ajuste(x)
    
    for i in range(0, 26):
        error = abs( (j[i] - spherical_jn(i, x)) / spherical_jn(i, x) )
        tabla.add_row([f"j_{i}",
                    f"{j[i]:<.10e}",
                    f"{spherical_jn(i, x):<.10e}", 
                    f"{error:<.10e}"])    
    print(tabla)        

          
    
def tabla_up_vs_down(x: float):
    """Esta función imprime una tabla que compara los valores numérocos
    para las primeras 25 funciones de bessel calculadas por el método up 
    y por el método down ajustado"""
    
    tabla = PrettyTable()
    tabla.title = (f"Bessel up vs down: x = {x}")
    tabla.field_names = ['l', 'j_l up', 'j_l down', 'Error']
    j = bessel_esf_down_ajuste(x)
    
    for i in range(0, 26):
        error = abs( bessel_esf_up(i, x) - j[i] ) / ( abs(bessel_esf_up(i, x)) + abs(j[i]) )
        tabla.add_row([f"{i}",
                    f"{bessel_esf_up(i,x):<.10e}",
                    f"{j[i]:<.10e}", 
                    f"{error:<.10e}"])    
    print(tabla)   

#Aquí se obtienen las respuestas del inciso a
tabla_bessel_up(0.1)
tabla_bessel_down(0.1)
tabla_bessel_up(1)
tabla_bessel_down(1)
tabla_bessel_up(10)
tabla_bessel_down(10)

#Aquí se obtienen las respuestas del inciso b
tabla_bessel_down_ajuste(0.1)
tabla_bessel_down_ajuste(1)
tabla_bessel_down_ajuste(10)

#Aquí se obtienen las respuestas del inciso c
tabla_up_vs_down(0.1)
tabla_up_vs_down(1)
tabla_up_vs_down(10)