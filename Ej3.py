# -*- coding: utf-8 -*-
"""
Ejercicios con listas I
Asignatura: Métodos computacionales y Sistemas de Información Geográfica
Máster de Geofísica y Meteorología (Universidad de Granada)
Curso 2022-2023
Autor: José Vicente Pérez Peña
Contacto: vperez@ugr.es
"""
# El siguiente código crea una lista llamada colores con un número aleatorio de elementos
# No te preocupes sino entiendes el código (de hecho si lo entiendes es tienes un conocimiento 
# bastante aceptable de Python y te estarás aburriendo muchisimo en las clases)


# Con la lista colores, realiza las siguientes cuestiones:
# Sustituye "pass" con tu código

# 1. Imprime el número de elementos de la lista colores

# 2. Imprime los 5 primeros elementos de la lista colores


# 3. Imprime los 3 ultimos elementos de la lista colores


#%%

# 4. Añade el elemento "fucsia" al final de lista colores e imprime los 3 ultimos elementos de la misma


#%%
# 5. Imprime el número de veces que aparece el color "rojo" en la lista colores



#%%
# 6. Crea otra lista con los 10 primeros elementos de la lista colores, imprime la lista



#%%
# 7. Crea otra lista con los 3 primeros elementos y los 3 últimos de la lista colores, imprime la lista 


#%%
# 8. Itera la lista, y cada vez que se encuentre el color "azul", imprime:
# "Hurra", he encontrado n colores azules!!! (sustituye n por el número de veces de la lista)
# Ejemplo: para una lista como está:
# colores_test = ["azul", "verde", "azul", "rojo", "verde", "azul"]
# Deberá imprimirse:
# "Hurra", he encontrado 1 colores azules!!!
# "Hurra", he encontrado 2 colores azules!!! 
# "Hurra", he encontrado 3 colores azules!!!




#%%
# 9. Crea un código que elija un color aleatorio de la lista. Si ese color es "rojo", "verde" o "azul", imprime
# "color RGB", si es "blanco" o "negro", imprime "color BN", y si es amarillo o naranja, imprime "otro color".




#%%
# 10. Imprime las posiciones de la lista donde aparezca el color "blanco"




# Cuando completes el script, si has contestado correctamente a todos los puntos deberá imprimirse:

#Ej. 01:  ----------------------------------------
#63
#
#Ej. 02:  ----------------------------------------
#['verde', 'rojo', 'azul', 'naranja', 'blanco']
#
#Ej. 03:  ----------------------------------------
#['negro', 'verde', 'naranja']
#
#Ej. 04:  ----------------------------------------
#['verde', 'naranja', 'fucsia']
#
#Ej. 05:  ----------------------------------------
#9
#
#Ej. 06:  ----------------------------------------
#['verde', 'rojo', 'azul', 'naranja', 'blanco', 'blanco', 'negro', 'verde', 'amarillo', 'amarillo']
#
#Ej. 07:  ----------------------------------------
#['verde', 'rojo', 'azul', 'verde', 'naranja', 'fucsia']
#
#Ej. 08:  ----------------------------------------
#"Hurra", he encontrado 1 colores azules!!!
#"Hurra", he encontrado 2 colores azules!!!
#"Hurra", he encontrado 3 colores azules!!!
#"Hurra", he encontrado 4 colores azules!!!
#"Hurra", he encontrado 5 colores azules!!!
#"Hurra", he encontrado 6 colores azules!!!
#"Hurra", he encontrado 7 colores azules!!!
#"Hurra", he encontrado 8 colores azules!!!
#
#Ej. 09:  ----------------------------------------
#Color RGB
#
#Ej. 10:  ----------------------------------------
#[4, 5, 11, 15, 21, 31, 48, 51, 55]