"""
WHILE
Bucle indeterminado, por que  a priori no sabemos cuántas veces se ejecutará el código

Sintaxis:

While condición:
    Cuerpo del bucle.

Hay que tener cuidado con los bucles infinitos, y limitar bien la condición.

"""
import math

# En este ejemplo no se ve cómo la indeterminación porque le hemos puesto un límite claro.
i = 1

while i <= 10:
    print("Ejecución " + str(i))
    i += 1

print("Terminó la ejecución")

# Con el ejemplo de preguntar la edad y con la condición de que tiene que ser válida, se crearía uno indetemrinado.

edad = int(input("Introduzca su edad: "))

while edad <= 0 or edad>100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo. ")
    edad = int(input("Introduzca su edad: "))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante: ", edad)
print("Edad del aspirante: " + str(edad))

# Cómo hacer que un bucle no se convierta en en infinito
# Vamos a calcular la raíz cuadrada de un número (que tiene que ser positivo)
# importar clases.

print("Programa de calculo de raíz cuadrada")

numero = int(input("Introduce un número por favor: "))
intentos = 0

while numero<0:
    if intentos ==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;
    numero = int(input("Introduce un número por favor: "))

    if numero < 0:
        intentos +=1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raíz cuadrada de ", numero, "es ", solucion)

# En este el código no se sabe cuántas veces se va a ejecutar, pero sí que como máximo serán tres.
