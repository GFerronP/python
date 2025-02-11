miLista = ["Maria","Pepe","Marta","Antonio"]

print(miLista[:]) #imprime toda la lista
print(miLista[1])  #imprime una posición
print(miLista[-2]) #imprime una posición empezando desde el final.
print(miLista[2:]) #imprime intervalos 

miLista.append("Sandra"); #añade un elemento
print(miLista[:]) 

miLista.insert(2,"Monica") #añade un elemento en la posición indicada
print(miLista[:])

miLista.extend(["Ana","Lucía","Rebeca"]) #añadir varios datos

print(miLista[:])

print("Pepe" in miLista) #buscar dentro de la lista, devuelve true o false

print(miLista.index("Ana")); #nos dice en qué posición se encuentra 


#se pueden añadir distintos tipos de datos.

miLista.remove("Ana");
#para eliminar un dato

miLista.pop() #elimina el último elemento de un lista.

miLista2 = ["Rosa",3, True]

miLista3 = miLista + miLista2;

print(miLista3[:])


milista4 = ["Samuel","Raquel","Mamá","Papá"]*3 #para repetir una lista el número de veces indicado

print(milista4[:])
print(miLista)
print(len(miLista))
