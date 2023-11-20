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




#%%
# 2. Crea una tupla con los elementos del 3 al 7 (índices del 2 al 6) de la tupla creada anteriormente
# Imprime la tupla


#%%
# 3. Crea una tupla con 5 numeros consecutivos del 0 al 4
# Imprime la tupla



#%%
# 4. A partir de la lista de tuplas paises_capitales, crea un diccionario
# Las claves serán los paises y los valores las capitales (puedes utilizar dict() directamente)
# Imprime el diccionario resultante





#%%
# 5. Añade la clave "Italia" con el valor "Roma" al diccionario
# Imprime el diccionario




#%%
# 6. Itera el diccionario e imprime sus claves

  




#%%  
# 7. Itera el diccionario e imprime sus valores

 


#%%   
# 8. Combina el diccionario con este otro, actualizando los valores de las claves existentes y 
# añadiendo los nuevos valores. Imprime el diccionario





#%%
# 9. Elimina la clave "España" del diccionario
# Imprime el diccionario







#%%
# 10. A partir de la lista de tuplas paises_capitales, crea un diccionario
# Las CLAVES serán las CAPITALES y los VALORES los PAISES
# Imprime el diccionario resultante




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