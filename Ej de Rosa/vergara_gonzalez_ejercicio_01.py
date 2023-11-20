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
print("Ej. 01")
print("="*45)

entero= 20
decimal= 69.69
cadena= "Hoy hace calor"
hacecalor= True
print("Valores y tipo de las variables:\n")
print(entero, "\t",  type(entero), "\n", decimal, "\t",  type(decimal), "\n",  cadena, "\t",  type(cadena), "\n", hacecalor, "\t",  type(hacecalor))



#%% Ej. 02
# Crea un programa que genere dos numeros aleatorios decimales entre 0 y 100
# El programa deberá imprimir que número es mayor
print("Ej. 02")
print("="*45)

import random as rnd

a=0
b=100
random1= rnd.random()*(b-a)+a
random2= rnd.random()*(b-a)+a
if random1 >= random2:
    print("el número mayor es: \t", random1)
else: print("el número mayor es: \t", random2)


print(str(random1) + "  es mayor que " + str(random2)) #PARA AÑADIR STRING CON ALGO MÁS TODO TIENE Q SER STRING
print("{:.2f} es mayor que {:.2f}".format(random1, random2))

#%% Ej. 03
# Calcula el seno y el coseno de un angulo de pi/2 radianes
print("Ej. 03")
print("="*45)

import math as m
seno= m.sin(m.pi*0.5)
coseno= m.cos(m.pi*0.5)
print(seno, coseno)





#%% Ej. 04
# Calcula el seno y el coseno de un ángulo de 40 grados
print("Ej. 04")
print("="*45)

import math as m
radianes= m.radians(40)
seno= m.sin(radianes)
coseno= m.cos(radianes)
print(seno, coseno)





#%% Ej. 05
# Calula el siguiente polinómio para x = 5 y x = 10
# y = e^(x^2 + 5)
print("Ej. 05")
print("="*45)

x=10
y= m.e**(x**2 + 5)
print(y)  
#x= 5 y= 10686474581524.445
#x= 10 y=3.989519570547194e+45 




#%% Ej. 06
# Calcula el área en m3 de 3 esferas de radios 2.3, 4.6 y 6 metros respectivamente
# Imprime los valores resultantes
print("Ej. 06")
print("="*45)

#Como pone las unidades en m3 supongo que ha sido un error y quería decir volumen
import math as m
r1=2.3
r2=4.6
r3=6

#creo que la forma más cómoda de hacerlo es con funciones, pero creo que no lo hemos dado aún
#También se puede hacer poniendo vol1= (4/3)*m.pi*r1**3 y así sucesivamente con cada radio
def vol(radio):
    volumen=(4/3)*m.pi*radio**3
    return volumen
vol1= vol(2.3)
vol2= vol(4.6)
vol3= vol(6)
print("Volúmenes en m^3:")
print(vol1, "\t", vol2, "\t", vol3)




#%% Ej. 07
# Transforma las áreas del ejercicio anterior a valores enteros de cm3
# Imprime los valores resultantes
print("Ej. 07")
print("="*45)

#copio y pego el código anterior para ejecutar esta celda
import math as m
r1=2.3
r2=4.6
r3=6
def vol(radio):
    volumen=(4/3)*m.pi*radio**3
    return volumen
vol1= vol(2.3)
vol2= vol(4.6)
vol3= vol(6)

#defino una función que transforma el dato recibido de m3 a cm3, y en números enteros
#Para no usar funciones también se pueden calcular los nuevos volúmenes uno a uno como vol1cm= vol1*10**6
def pasocm3 (volumenm):
    volumencm= volumenm*10**6
    volumencm= int(volumencm)
    return volumencm
vol1cm= pasocm3(vol1)
vol2cm= pasocm3(vol2)
vol3cm= pasocm3(vol3)
print("Volúmenes en cm^3:")
print(vol1cm, "\t", vol2cm, "\t", vol3cm)


#%% Ej. 08
# Crea un programa que genere un número aleatorio entero entre 0 y 100
# El programa deberá imprimir si ele número es PAR o IMPAR
print("Ej. 08")
print("="*45)

import random as rnd
a=0
b=100
numrandom= rnd.random()*(b-a)+a
numrandom2= rnd.randrange(0,100) #SI LO PONE ASÍ HASTA 100 NO INCLUYE EL 100
#para que sea numero random entero:
intrandom= int(numrandom)
print(intrandom)
if intrandom % 2==0:  
    print ("el número random es par")
else:
    print("el número random es impar")

#TB SIRVE ESTO:
if not (intrandom % 3):
    print(intrandom, 'no multiplo')
else:
    print(intrandom, 'multiplo')


#%% Ej. 09
# Crea un programa que genere un número aleatorio entero entre 0 y 20
# El programa deberá imprimir si el número es o no PRIMO
print("Ej. 09")
print("="*45)

import random as rnd
a=0
b=20
numrandom= rnd.random()*(b-a)+a
#para que sea numero random entero:
intrandom= int(numrandom)
print(intrandom)
if intrandom==3 or intrandom ==5 or intrandom==7 or intrandom==1 or intrandom==2:
    print ("el número random es primo")
elif intrandom % 2!=0 and intrandom % 3!=0 and intrandom % 5!=0 and intrandom % 7!=0:
    print ("el número random es primo")
else:
    print("el número random no es primo")









#%% Ej. 10
# Crea un programa para calcular el interés de un deposito bancario
# El programa generára una cantidad inicial aleatoria entre 0 y 10000
# Calcula el interés anual por el depósito de la cantidad para 5 años
# Si la cantidad es menor de 100E no habrá interes
# Si la cantidad está entre 0 y 1000E aplica un interés del 0.5%
# Si la cantidad está entre 1000 y 5000E aplica un interés del 1%
# Si la cantidad es mayor de 5000 aplica un interés del 2.5%
# Imprime la cantidad final del depósito a los 5 años(sumando los intereses) 
print("Ej. 10")
print("="*45)

import random as rnd
import math 
a=0
b=10000
numrandom= rnd.random()*(b-a)+a
print("Cantidad inicial aleatoria: \t", "%.2f"%numrandom) #imprimo sólo dos decimales porque son los que tienen sentido monetariamente hablando
años=5


#Definimos el interés según la cantidad aleatoria inicial
interes=0
if numrandom>=100 and numrandom<=1000:
    interes= 0.005
elif numrandom>1000 and numrandom <=5000:
    interes= 0.01
elif numrandom>5000:
    interes= 0.025
    
deposito= rnd.random()*(b-a)+a
#otra forma mejor:
if deposito <100:
    interes=0
elif deposito <1000:
    interes=0.005
elif deposito<5000:
    interes=0.01
else:
    interes=0.025
    

#La cantidad final en el depósito será la cantidad inicial más el interés acumulado con los años
cantfinal= numrandom + numrandom*interes*años
print("Cantidad final con intereses: \t", "%.2f"%cantfinal)
    
    








