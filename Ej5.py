# -*- coding: utf-8 -*-
"""
Ejercicios con cadenas de texto
Asignatura: Métodos computacionales y Sistemas de Información Geográfica
Máster de Geofísica y Meteorología (Universidad de Granada)
Curso 2022-2023
Autor: José Vicente Pérez Peña
Contacto: vperez@ugr.es
"""

# Para los siguientes ejercicios, utiliza esta cadena de texto.

mi_cadena = "El veloz muerciélago hidú, comía feliz cardillo y kiwi. La cigüeña tocada el saxofon derás del palenque de paja."

# 1. Crea una cadena con todos los carécteres en minúscula, imprime la cadena resultante



#%%
# 2. Crea unan cadena con todos los carácteres en mayúscula, imprime la cadena resultante



#%%
# 3. Crea una cadena donde sustituyas las "z" (zetas) por "s" (eses), imprime la cadena resultante




#%%
# 4. Crea una lista con las posiciones de la cadena en las que esté la letra "e" 
# (no distingas entre mayúsculas y minúsculas). Imprime la lista resultante




#%%
# 5. Imprime el número de vocales de la cadena. No distingas entre mayusculas y minusculas.
# Imprime el número de elementos de esta lista.



#%%
# 6. Crea una lista con todas las palabras de la cadena de texto.
# Imprime el número de elementos de esta lista.





#%%
# 7. Con la lista creada anteriormente, imprime el número de palabras con n carácteres
# Ten en cuenta que los signos de puntuación "." y "," NO pertecenen a los carácteres de una palabra. 
# Ej. 
# "1 palabra de 1 carácter"
# "4 palabras de 2 carácteres"
# "1 palabra de 3 carácteres"
# Etc.



    





#%%
# 8. A patir de la cadena de texto "valores", obten una lista de números enteros
# Imprime la lista resultante





#%%
# 9. A patir de la cadena de texto "valores", obten una lista de números decimales
# Imprime la lista resultante





#%%
# 10. A patir de la cadena de texto "valores", obten una lista con los valores decimales de la cadena
# Imprime la lista resultante


'''
Como ahora sólo quiero una lista con los valores numéricos, hago una variante de los procedimientos anteriores
Diferencias:
- Tiene en cuenta que habrá un error cuando intente convertir de cadena de texto a float 
- No se usa compresión de listas sino un for normal para que se pueda repetir la detección de error
sin que se detenga la conversión de la cadena 
Nota: he supuesto que con "valores decimales" hace referencia a todos los valores que puedan ser convertidos a float
'''



#En caso de que lo que se pida es que sólo se conviertan los valores que tienen decimales el procedimiento sería:
    
    





#=========================================================================
# Resultados esperados:
# Si realizas los ejercicios correctamente, deberás imprimir lo siguiente

#Ej. 01:  ----------------------------------------
#el veloz muerciélago hidú comía feliz cardillo y kiwi. la cigüeña tocada el saxofon derás del palenque de paja. 1234567890
#
#Ej. 02:  ----------------------------------------
#EL VELOZ MUERCIÉLAGO HIDÚ COMÍA FELIZ CARDILLO Y KIWI. LA CIGÜEÑA TOCADA EL SAXOFON DERÁS DEL PALENQUE DE PAJA. 1234567890
#
#Ej. 03:  ----------------------------------------
#El veloz muerciélago hidú comía feliz cardillo y kiwi. la cigüeña tocada el saxofon derás del palenque de paja. 1234567890
#El Veloz Muerciélago Hidú Comía Feliz Cardillo Y Kiwi. La Cigüeña Tocada El Saxofon Derás Del Palenque De Paja. 1234567890
#
#Ej. 04:  ----------------------------------------
#Murcielago     
#    Murcielago
#Murcielago
#
#Ej. 05:  ----------------------------------------
#El velos muerciélago hidú comía felis cardillo y kiwi. La cigüeña tocada el saxofon derás del palenque de paja. 1234567890
#
#Ej. 06:  ----------------------------------------
#[0, 4, 11, 33, 62, 73, 85, 91, 97, 101, 104]
#
#Ej. 07:  ----------------------------------------
#[6, 19, 27, 45, 67, 79, 81]