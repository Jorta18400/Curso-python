# -*- coding: utf-8 -*-
"""
Ejercicios 01
Asignatura: Métodos computacionales y Sistemas de Información Geográfica
Máster de Geofísica y Meteorología (Universidad de Granada)
Curso 2021-2022
Autor: José Vicente Pérez Peña
Contacto: vperez@ugr.es
"""




#%% Ej. 01
# Crea 4 variables de tipo entero, decimal, cadena de texto y boleano
# Imprime el valor de cada variable
# Imprime el tipo de cada variable

entero=33
decimal=33.0
cadena="Treinta y tres"
booleano=True

print('Los tipos de cada una de las variables se presentan a continuación:')
print('entero: ', type(entero))
print('decimal: ', type(decimal))
print('cadena: ', type(cadena))
print('booleano: ', type(booleano))

#%% Ej. 02
# Crea un programa que genere dos numeros aleatorios decimales entre 0 y 100
# El programa deberá imprimir que número es mayor

import random as rand

#Aquí genero los números, la función uniform genera aleatorios en un rango definido
var1=rand.uniform(0,100)
var2=rand.uniform(0,100)


#Voy a imprimir también va1 y var2 para asegurarme de que se representa el mayor
print(var1, '\t', var2)
print('El valor mayor es: ', max(var1,var2))

#%% Ej. 03
# Calcula el seno y el coseno de un angulo de pi/2 radianes

import math

seno=math.sin(math.pi*0.5)
coseno=math.cos(math.pi*0.5)
print('seno: ', seno, '\n coseno: ', coseno)



#%% Ej. 04
# Calcula el seno y el coseno de un ángulo de 40 grados

import math

seno=math.sin(math.radians(40))
coseno=math.cos(math.radians(40))
print('seno: ', seno, '\n coseno: ', coseno)



#%% Ej. 05
# Calula el siguiente polinómio para x = 5 y x = 10
# y = e^(x^2 + 5)

import math as m
#Descomentar el que se vaya a usar
#x=5
x=10
y=m.e**(x**2+5)
print(y)


#%% Ej. 06
# Calcula el volumen en m3 de 3 esferas de radios 2.3, 4.6 y 6 metros respectivamente
# Imprime los valores resultantes

import math as m
radio1=2.3
radio2=4.6
radio3=6

volumen1=(4*m.pi*radio1**3)/3
volumen2=(4*m.pi*radio2**3)/3
volumen3=(4*m.pi*radio3**3)/3

print('Volumen de la primera esfera: ', volumen1)
print('Volumen de la segunda esfera: ', volumen2)
print('Volumen de la tercera esfera: ', volumen3)

#%% Ej. 07
# Transforma los volúmenes del ejercicio anterior a valores enteros de cm3
# Imprime los valores resultantes

#Meto el código anterior para sacar los volúmenes
import math as m
radio1=2.3
radio2=4.6
radio3=6

volumen1=(4*m.pi*radio1**3)/3
volumen2=(4*m.pi*radio2**3)/3
volumen3=(4*m.pi*radio3**3)/3

def m3acm3(m3):
    cm3=m3*10**(6)
    cm3=int(cm3)
    return cm3

volumen1=m3acm3(volumen1)
volumen2=m3acm3(volumen2)
volumen3=m3acm3(volumen3)

print('Volumen de la primera esfera: ', volumen1)
print('Volumen de la segunda esfera: ', volumen2)
print('Volumen de la tercera esfera: ', volumen3)   



#%% Ej. 08
# Crea un programa que genere un número aleatorio entero entre 0 y 100
# El programa deberá imprimir si el número es PAR o IMPAR

import random as rand

num=rand.randint(0,100)

#El símbolo % obtiene el resto de una división

if(num%2==0):
    print('Número par')
else:
    print('Número impar')

print(num)

#%% Ej. 09
# Crea un programa que genere un número aleatorio entero entre 0 y 20
# El programa deberá imprimir si el número es o no PRIMO

import random as rand

num=rand.randint(0,20)
#Defino una función pa ver si es primo
def esprimo(num):
    if(num==0):  #El 0 no es primo
        return False
    elif(num==1): #El 1 es primo
        return True
    else:
        for i in range(2,num): #Establezco un for de 2 a n-1, si es divisible por alguno no es primo
            if(num%i==0):
                return False
        return True

Primo=esprimo(num)
if Primo==True:
    print('El número aleatorio (',num,') es primo')
else:
    print('El número aleatorio (',num,') no es primo')

#%% Ej. 10
# Crea un programa para calcular el interés de un deposito bancario
# El programa generára una cantidad inicial aleatoria entre 0 y 10000
# Calcula el interés anual por el depósito de la cantidad para 5 años
# Si la cantidad es menor de 100E no habrá interes
# Si la cantidad está entre 100 y 1000E aplica un interés del 0.5%
# Si la cantidad está entre 1000 y 5000E aplica un interés del 1%
# Si la cantidad es mayor de 5000 aplica un interés del 2.5%
# Imprime la cantidad final del depósito a los 5 años(sumando los intereses) 

import math as m
import random as rand

dineros=rand.randint(0,10000)
print('Inicialmente tienes: ', dineros, 'dineros')

años=5
for i in range(1,años+1): #Tengo que poner el +1 porque range llega hasta n-1
    if(100<dineros<=1000):
        dineros=dineros+(dineros*0.5/100)
    elif(1000<dineros<=5000):
        dineros=dineros+(dineros*1/100)
    elif(5000<dineros):
        dineros=dineros+(dineros*2/100)
print('Finalmente tienes: ', int(dineros), 'dineros')


# %%
