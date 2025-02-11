"""
Los bucles sirven para repetir una o varias líneas de código varias veces
Es una forma de simplificar código.
Tipos de bucles:
Determinados:
Se ejecutan un número determinado de veces. Se sabe a priore cuántas veces se va a ejecutar
Indeterminados:
Se ejecutan un número indeterminado de veces, y no se sabe a priori cuántas, el número de veces dependera
de la ejecución del programa.

"""

#Bucle determinado: FOR
#SINTAXIS:
# for variable in elemento a recorrer:
#   cuerpo del bucle (identación obligagtoria)
"""
la variable por convención se llama i y si son anidados j, aunque puedes llamarlos cómo quieras.
"""

#aquí le pedimos que imprima una cantidad de veces lo que hay en el print
#el número de veces está detemrinado por la cantidad de valores dentro de la lista.
for i in [1,2,3]:
    print("Hola")
for i in ["primavera","verano","otoño","invierno"]:
    print("hola")

#aquí lo que le pedimos es que imprima el valor de i, que será lo que haya dentro del elemento a recorrer.
for i in ["primavera", "verano", "otoño","invierno"]:
    print(i)