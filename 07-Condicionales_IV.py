#  operadores lógicos AND (y si además), OR (o si no) e IN

# vamos a crear un programa que mire si un alumno tiene derecho a beca
#  comparando distancia>40 km , número de hermanos>2, salario familiar <=20000. Que cumplan esos tres
"""
print("Programa de becas Año 2017")

distancia_escuela = int(input("Introduce la distanci a la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario familiar: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

#  Si queremos reducir los requisitos,y que por ejemplo el salario familiar sea determinante:

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
"""
#  se pueden concatenar todos los operadores lógicos queraís.

#  uso del IN
# Ejemplo de un alumno que tiene que escoger entre varias asignaturas
print("Asignaturas optativas año 2017")
print(" Asignaturas oprativas: Informática gráfica - Pruebas de software  Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida: ")
asignatura = opcion.lower()

if asignatura in ("informática gráfica","pruebas de software","usabilidad y accesibilidad"):
    print("Asignatura elegida: "+asignatura)
else:
    print("La asignatura escogida no está contemplada")

#  Hay que tener en cuenta que a la hora de buscar es case sensitive, tildes, etc
# Para solucionar esto usaremos las funciones LOWER() y UPPER()

