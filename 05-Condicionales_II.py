print("Verificación de acceso")
edad_usuario = int(input("Introduce tu edad, por favor: "))

if edad_usuario<18: #es correcto, pero aquí no indicamos qué pasa si la condición es falsa, por eso usamos ELSE
	print("No puede pasar")
else: 
	print("Puedes pasar")
#Else siempre debe ir emparejado de un if, es decir, no podría haber dos elses con un if.
print("El programa ha finalizado")

#Para poner varias condiciones ELIF

print("Verificando el acceso")
edad_usuario1 = int(input("Introduce tu edad, por favor: "))

if edad_usuario1<18:
	print("No puedes pasar")
elif edad_usuario>100:
	print("Edad incorrecta")
else: 
	print("Puedes pasar")

print("El programa ha finalizado")


