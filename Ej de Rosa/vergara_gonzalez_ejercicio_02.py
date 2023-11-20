# -*- coding: utf-8 -*-
"""
Ejercicios 02
Asignatura: Métodos computacionales y Sistemas de Información Geográfica
Máster de Geofísica y Meteorología (Universidad de Granada)
Curso 2021-2022
Autor: José Vicente Pérez Peña
Contacto: vperez@ugr.es
"""
import math
import random 

#%% Ej. 01
# Imprime los múltiplos de 3 y 5 (a la vez) entre 0 y 150 (incluído)
print("\nEj. 01")
print("="*45)

for i in range (0,151):
    if i%3==0 and i%5==0:
        print(i)




#%% Ej. 02
# Crea un programa que imprima 5 veces "Hola tu_nombre" (sustituye tu_nombre por tu nombre)
print("\nEj. 02")
print("="*45)

mi_nombre='Rosa'

for i in range(0,5):
    print ("Hola {}".format(mi_nombre))





#%% Ej. 03
# Crea un programa que genere un número aletorio decimal entre 0 y 200 y lo redondee al entero más cercano
# Imprime el número decimal (con dos decimales) y el redondeado
# Ej: 3.5 4
print("\nEj. 03")
print("="*45)

import random


num=random.random()*200
numint= int(num)
print ("%.2f"%num, numint)





#%% Ej. 04
# Crea un programa que genere un número aletorio decimal entre 0 y 200 y lo redondee al entero más cercano por arriba
# Imprime el número decimal (con dos decimales) y el redondeado
# Ej: 3.22 4
print("\nEj. 04")
print("="*45)



num=random.random()*200
numred= math.ceil(num)
print ("%.2f"%num, numred)




#%% Ej. 05
# Crea un programa que genere un número aletorio decimal entre 0 y 200 y lo redondee al entero más cercano por debajo
# Imprime el número decimal (con dos decimales) y el redondeado
# Ej: 3.98 3
print("\nEj. 05")
print("="*45)


num=random.random()*200
numred= math.floor(num)
print ("%.2f"%num, numred)




#%% Ej. 06
# Crea una lista de números enteros con todos los decimales del número pi del módulo math
# Ej. decimales_pi = [1, 4, 1, 5, 9 ... etc]
# Imprime la lista resultante
print("\nEj. 06")
print("="*45)

import math

lista= list(str(math.pi))
lista.pop(0)
lista.pop(0)
print(lista)



#%% Ej. 7
# Genera una simulación MonteCarlo de un dado de n caras
# Deberás simular m tiradas (entre 1000 y 100000) de un dado de n caras (entre 4 y 8)
# Imprime el numero de caras, el número de tiradas y el % de veces que ha salido cada cara
# Ejemplo: Para un dado de 6 caras debería imprimir (las tiradas y los % cambiaran!)
# Simulación MonteCarlo 
# Dado de 6 caras, 2030 tiradas
# Cara 1: 16.6%
# Cara 2: 16.6%
# Cara 3: 16.6%
# Cara 4: 16.6%
# Cara 5: 16.6%
# Cara 6: 16.6%
print("\nEj. 7")
print("="*45)

import random

print('Simulación Montecarlo')

caras=random.randint(4, 5)  #entre 4 y 8
tiradas=random.randint(100, 100000)

print('Dado de {} caras, {} tiradas'.format(caras, tiradas))

lista= []

for i in range(0, tiradas):
    lista.append(0)
print(len(lista)) #debería ser igual a tiradas

#SIMULACIÓN DE TIRADAS
for i in range(0, tiradas):
    result= random.randint(1, caras)
    lista[result-1] += 1

#CÁLCULO E IMPRESIÓN DE PROBABILIDADES
for i in range(0, caras):
    print('Cara {}: {:.1f}%'.format(i+1, lista[i]*100/tiradas))
    






#%% Ej. 8
# El siguiente código crea una de longitud variable de letras aleatorias
# (No te preocupes si no entiendes el código, lo veremos más adelante)
# Con la lista realiza las tares de los siguientes puntos:
print("\nEj. 8")
print("="*45)
random.seed(12345)
letras = [chr(random.randrange(ord("A"), ord("Z"))) for n in range(random.randrange(100, 500)) ]


# 8.1. Imprime el número de elemento de la lista
print("\nEj. 8.1")

print('La lista tiene {} elementos'.format(len(letras)))


# 8.2. Imprime el número de veces que aparece la letra "B"
print("\nEj. 8.2")

veces= letras.count('B')
print('La letra ''B'' aparece {} veces'.format(veces))


# 8.3. Imprime los 5 últimos elementos de la lista
print("\nEj. 8.3")

print(letras[-5:])


# 8.4. Agrega tres letras "Z" al final de la lista (como 3 elementos distintos) e imprime los 6 últimos elementos de la lista
print("\nEj.8.4")

zetas= list('ZZZ')
letras= letras + zetas
print(letras[-6:])











"""
Si realizas bien los ejercicios, debería imprimirse esto (ten en cuenta que los ejercicios aleatorios pueden cambiar)

Ej. 01
=============================================
0
15
30
45
60
75
90
105
120
135
150

Ej. 02
=============================================
Hola Vicente
Hola Vicente
Hola Vicente
Hola Vicente
Hola Vicente

Ej. 03
=============================================
127.21 127

Ej. 04
=============================================
26.98 27

Ej. 05
=============================================
41.51 41

Ej. 06
=============================================
[1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]

Ej. 7
=============================================
Simulación Montecarlo
Dado de 6 caras, 8468 tiradas
Cara 1: 16.3%
Cara 2: 16.7%
Cara 3: 17.4%
Cara 4: 17.0%
Cara 5: 16.0%
Cara 6: 16.5%

Ej. 8
=============================================

Ej. 8.1
La lista tiene 313 elementos

Ej. 8.2
La letra 'B' aparece 13 veces

Ej. 8.3
['E', 'S', 'R', 'K', 'S']

Ej.8.4
['R', 'K', 'S', 'Z', 'Z', 'Z']
"""
