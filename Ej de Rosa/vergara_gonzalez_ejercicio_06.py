# -*- coding: utf-8 -*-
"""
Ejercicios con tuplas y diccionarios
Asignatura: Métodos computacionales y Sistemas de Información Geográfica
Máster de Geofísica y Meteorología (Universidad de Granada)
Curso 2022-2023
Autor: José Vicente Pérez Peña
Contacto: vperez@ugr.es
"""

# Ejercicios con tuplas y diccionarios
# Creacción de tuplas y manipulación de diccionarios
import random
random.seed(12345)

# 1. Crea una tupla a partir de la siguiente lista
# Imprime la tupla
print("Ej. 01:  " + "-"*50)
frutas = ["manzana", "plátano", "cereza", "higo", "limón", "granada", "caqui", "naranja", "frambuesa"]

tupla1= tuple(frutas)
print(tupla1)



#%%
# 2. Crea una tupla con los elementos del 3 al 7 (índices del 2 al 6) de la tupla creada anteriormente
# Imprime la tupla
print("\nEj. 02:  " + "-"*50)

tupla2=tupla1[2:7]
print(tupla2)


#%%
# 3. Crea una tupla con 5 numeros consecutivos del 0 al 4
# Imprime la tupla
print("\nEj. 03:  " + "-"*50)

tupla3= tuple([n for n in range(5)])
print(tupla3)



#%%
# 4. A partir de la lista de tuplas paises_capitales, crea un diccionario
# Las claves serán los paises y los valores las capitales (puedes utilizar dict() directamente)
# Imprime el diccionario resultante
print("\nEj. 04:  " + "-"*50)
paises_capitales = [("España", "Madrid"), ("Francia", "Paris"), ("Portugal", "Lisboa"), 
                    ("Grecia", "Atenas"), ("Alemania", "Berlin")]

diccionario4= dict(paises_capitales)
print(diccionario4)





#%%
# 5. Añade la clave "Italia" con el valor "Roma" al diccionario
# Imprime el diccionario
print("\nEj. 05:  " + "-"*50)
diccionario4['Italia']='Roma'
print(diccionario4)



#%%
# 6. Itera el diccionario e imprime sus claves
print("\nEj. 06:  " + "-"*50)


print(diccionario4.keys())
for i in diccionario4:
    print(i)
    
  




#%%  
# 7. Itera el diccionario e imprime sus valores
print("\nEj. 07:  " + "-"*50)


for i in diccionario4:
    print(diccionario4[i])
 


#%%   
# 8. Combina el diccionario con este otro, actualizando los valores de las claves existentes y 
# añadiendo los nuevos valores. Imprime el diccionario
print("\nEj. 08:  " + "-"*50)
otro_dict = {"España":"Granada", "Marruecos":"Rabat", "Egipto":"El Cairo"}

diccionario4.update(otro_dict)
print(diccionario4)





#%%
# 9. Elimina la clave "España" del diccionario
# Imprime el diccionario
print("\nEj. 09:  " + "-"*50)

diccionario4.pop('España')
print(diccionario4)






#%%
# 10. A partir de la lista de tuplas paises_capitales, crea un diccionario
# Las CLAVES serán las CAPITALES y los VALORES los PAISES
# Imprime el diccionario resultante
print("\nEj. 10:  " + "-"*50)

diccionario10= dict((a,b) for b,a in paises_capitales)
print(diccionario10)



#=========================================================================
# Resultados esperados:
# Si realizas los ejercicios correctamente, deberás imprimir lo siguiente:
#
#Ej. 01:  --------------------------------------------------
#('manzana', 'plátano', 'cereza', 'higo', 'limón', 'granada', 'caqui', 'naranja', 'frambuesa')
#
#Ej. 02:  --------------------------------------------------
#('cereza', 'higo', 'limón', 'granada', 'caqui')
#
#Ej. 03:  --------------------------------------------------
#(0, 1, 2, 3, 4)
#
#Ej. 04:  --------------------------------------------------
#{'España': 'Madrid', 'Francia': 'Paris', 'Portugal': 'Lisboa', 'Grecia': 'Atenas', 'Alemania': 'Berlin'}
#
#Ej. 05:  --------------------------------------------------
#{'España': 'Madrid', 'Francia': 'Paris', 'Portugal': 'Lisboa', 'Grecia': 'Atenas', 'Alemania': 'Berlin', 'Roma': 'Italia'}
#
#Ej. 06:  --------------------------------------------------
#España
#Francia
#Portugal
#Grecia
#Alemania
#Roma
#
#Ej. 07:  --------------------------------------------------
#Madrid
#Paris
#Lisboa
#Atenas
#Berlin
#Italia
#
#Ej. 08:  --------------------------------------------------
#{'España': 'Granada', 'Francia': 'Paris', 'Portugal': 'Lisboa', 'Grecia': 'Atenas', 'Alemania': 'Berlin', 'Roma': 'Italia', 'Marruecos': 'Rabat', 'Egipto': 'El Cairo'}
#
#Ej. 09:  --------------------------------------------------
#{'Francia': 'Paris', 'Portugal': 'Lisboa', 'Grecia': 'Atenas', 'Alemania': 'Berlin', 'Roma': 'Italia', 'Marruecos': 'Rabat', 'Egipto': 'El Cairo'}
#
#Ej. 10:  --------------------------------------------------
#{'Madrid': 'España', 'Paris': 'Francia', 'Lisboa': 'Portugal', 'Atenas': 'Grecia', 'Berlin': 'Alemania'}