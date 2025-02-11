# range se ha convertido en un tipo de dato en Python.
# permite utilizar el bucle for con conteos numéricos.
# notaciones especiales de print

# imrprime 3 veces el hola, porque es la cantidad de elementos que hay en la lista
# los imprime con salto de página.
for i in ["Pildoras", "Informáticas", 3]:
    print ("Hola")
# si queremos que los imprima todos en la misma línea sería
for i in ["Pildoras", "Informáticas", 3]:
    print ("Hola", end=" ") #como decirle que no haga salto de línea.
#si a ese end le añadimos espacios, meterá espacios
print()
for i in ["Pildoras", "Informáticas", 3]:
    print ("Hola", end="    ")
print()
#si con el for queremos recorrer un string, lo hará carácter a carácter
for i in "pildorasinformáticas":
    print("Hola", end=" ") #lo imprimirá tantas veces como carácteres tenga el string

#podemos comprobar por ejemplo si un correo es correcto (forma sencilla).
print()
email = False
for i in "juan@pildorasinformaticas.es":
    if (i == "@"):
        email=True
if email == True:
    print("Email es correcto")
else:
    print("Email no es correcto")

# cuando analizamos un booleano si queremos decir que la variable es igual a True
# se puede simplificar con usando solo el nombre de la variable.
email = False
for i in "juanpildorasinformaticas.es":
    if i == "@":
        email = True
if email:
    print("Email es correcto")
else:
    print("Email no es correcto")

# hay que distinguir entre el operador de asignación = , con la comparación ==
# para hacer un programa que sea genérico para todos los correos
# también se podría afinar la comprobación, añadiendo
# que tiene que tener al menos un punto (no hay correos sin un punto al menos)
contador = 0
miEmail = input("Introduce tu dirección de emai: ")
for i in miEmail:
    if i == "@" or i == ".":
        contador += 1
if contador == 2:
    print("Email es correcto")
else:
    print("Email no es correcto")

# en el ejemplo anterior falla la lógica, porque si tiene dos puntos y ninguna @ será correcto
# el programa se puede ir afinando para que se a más parecido
# a la realidad.


# range permite usar el bucle for con contadores, o casi como si lo fueran.
# crearia como una especie de array.

for i in range(5):
    print("hola")
for i in range(5):
    print(i)