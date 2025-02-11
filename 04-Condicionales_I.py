#uso condicional if

def evaluacion(nota):
	valoracion = "aprobado"
	if nota<5:
		valoracion = "suspenso"
	return valoracion

print(evaluacion(4))

#uso del if con entrada por teclado

nota_alumno = input("Introduce la nota del alumno:") #los datos metidos por teclado se consideran siempre Strings, hay que hacer un casting
#la función input puede admitir parámetros

def evaluacion(nota):
    valoracion = "aprobado"
    if nota<5:
        valoracion = "suspenso"
    return valoracion
print(evaluacion((int)(nota_alumno))) #el casting


