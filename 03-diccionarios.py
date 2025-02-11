# Estructura de datos quen os permite almacenar valores de diferente tipo(enteros, cadenas de texto, decimales)
#e incluso listas y otros diccionarios.

#La principal característica de los diccionarios es que los datos se almacenan asociados a una clave de tal forma
#que se crea una asociación de tipo clave:valor para cada elemento almacenado. 

#Los elementos almacenados no están ordenados. El orden es indiferente.

miDiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}

#para ver un valor determinado imprimes usando el nombre del diccionario y la clave.
print(miDiccionario["Francia"])

#agregar nuevos elementos
miDiccionario["Italia"]="Lisboa"

#para imprimir el diccionario entero
print(miDiccionario)

#modificar un  elemento una vez añadido
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#eliminar elementos: palabra clave del
del miDiccionario["Reino Unido"]
print(miDiccionario)

#Diccionario con valores mixtos

miDiccionario2={"Alemania":"Berlín", 23:"Jordan","Mosqueteros":3}
print(miDiccionario2)

#Diccionario con tuplas
mitupla = ["España", "Francia","Reino Unido","Alemania"]

#asignar como clave los datos de una tupla. Aunque también se podrían asignar como valor.
miDiccionario3 = {mitupla[0]:"Madrid",mitupla[1]:"París",mitupla[2]:"Londres",mitupla[3]:"Berlín"}
print(miDiccionario3)

#Asociar una tupla entera a un diccionario.
miDiccionario4 = {23:"Jordan", "Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]} 
print(miDiccionario4)

#guardar un diccionario dentro de otro diccionario:
miDiccionario5 = {23:"Jordan", "Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario5)
print("anillos")

#devolver las claves:
print(miDiccionario5.keys())

#devolver valores:
print(miDiccionario5.values())

#devolver la cantidad de valores de un diccionario.
print(len(miDiccionario5))

