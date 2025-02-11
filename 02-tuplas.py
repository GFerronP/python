#tuplas son listas inmutables. No se pueden modificar después de la creación
#se puede extraer porciones, pero el resultado es una nueva tupla
#Se pueden hacer búsquedas, hacer index
#Se permite comprobar si un elemento se encuentra en la tupla.

#son más rápidas a la hora de ejecutarlas, ya que ocupan menos especio.
#formatean Strings
#Pueden utilizarse como claves en un diccionario (las listas no).

#Las tuplas van entre paréntesis aunque se pueden omitir es recomendable usarlos. nombreTupla=(elemento1, elemento2, etc);

miTupla = ("Juan", 13,1,1995,13)

print(miTupla[2])

#convertir en lista

miLista = list(miTupla)

print(miLista[:])

#convertir en tupla

miTupla2 = tuple(miLista)

print(miTupla2[:])

#nos dice en qué posición se encuentra 
print(miTupla.index("Juan")); 


#comprobar si está dentro de la tupla

print("Juan" in miTupla)

#contar cuantas vece se encuentra un elemento de una tupla

print(miTupla.count(13))

#comprobar la longitud de una tupla

print(len(miTupla))

#tupla unitaria 

mituplaU = ("Juan",)
print(len(mituplaU))

#empaquetado de tupla

tuplaE = "Osen",5,1,1983

print(tuplaE)


#desempaquetado de tupla

tuplaD = ("Osen",5,1,1983)

nombre, dia, mes, anio = tuplaD

print(nombre);
print(anio);
print(dia);
print(mes)



