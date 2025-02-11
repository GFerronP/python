for i in range(5):
    print(i)

# empieza en 0
# hay una notación útil para unir texto con la variable
# sería la notación f. el nombre de la variable iría entre llaves.
print()
for i in range(5):
    print(f"valor de la variable {i}")

# si quitamos la f, python no entendería que por i nos referimos a la variable
print()
for i in range(5):
    print("valor de la variable {i}")

# con el uso de range se pueden usar intervalos, se puede contar hacia atrás,etc
#para ir hacia atrás se usa la función reverse()
print()
for i in range(5,10):
    print(i)
print()
for i in reversed([2,3,4,5,6]):
    print(i, end=" ")

# admite un tercer parametro que indicaría de cuanto en cuanto debe ir contando
print()
for i in range(5,50,5):
    print(i)
# la función len devuelve la longitud de una lista, string,etc, y se podría usar con range.
#ejemplo
print()
valido = False
email = input("introduce tu email: ")
for i in range(len(email)):
    if email[i] == "@":
        valido = True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")