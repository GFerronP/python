"""
Instrucciones que se pueden usar con los bucles for y while

Continue: Ignora una vuelta de bucle y pasa a la siguiente
Pass: Devuelve null en cuanto se lee en el interior de
es cómo si no se ejecutara el bucle. Se usa en contadas ocasiones.
Se suele usar a la hora de definir clases (cuanndo quieres que esa nula)
O como cuando desarrollador vas a dejar para luego el desarrollo de un bucle.

else: tiene el mismo uso que dentro de un codicional IF


"""
# Ejemplo de continue.
for letra in "Python":
    if letra == "h":
        continue
    print("Viendo la letra: " + letra)

# Imagina que quieres contar el número de carácteres que tiene un string
nombre = "Pildoras Informáticas"

# la opcion len nos devuelve la longitud del string. Pero como el espacio en blanco se considera carácter.
print(len(nombre))

# podemos usar un bucle for para evitar que se cuenten los espacios.

contador = 0
for letra in nombre:
    if letra == " ":
        continue
    contador += 1

print("El númeoro de letras es: ", contador)
"""
# Ejemplo pass, de momento no es útil:
while True:
    pass

class Miclase:
    pass
"""
# uso de else

email = input("Introduce tu email, por favor: ")
for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print(arroba)

# la instrucción else se va a ejecutar una vez que el bucle esté vacío, es decir,
# una vez que el bucle halla ejecutado todas sus vueltas
# En general el uso de pass y else suele ser límitado, pero hay que saberlo.
