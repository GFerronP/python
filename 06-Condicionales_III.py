edad = -7

if 0 < edad < 100:  # se pueden usar operadores concatenados para reducir código
    print("Edad es correcta")
else:
    print("Edad incorrecta")


# programa para evaluar el salario de una empresa con concatenación

salario_presidente = int(input("Introduce salario presidente: "))
print("Salario presidente: "+str(salario_presidente))

salario_director = int(input("Introduce salario director: "))
print("Salario director: "+str(salario_director))

salario_jefe_area = int(input("Introduce salario Jefe Área: "))
print("Salario Jefe Área: "+str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario presente: "))
print("Salario administrativo: "+str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")