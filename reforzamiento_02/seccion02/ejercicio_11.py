estudiantes = []
cantidad_estudiantes = 4
estudiante1 = "Luis"
estudiante2 = "Mariana"
estudiante3 = "Pedro"
estudiante4 = "Teresa"
estudiantes.append(estudiante1)
estudiantes.append(estudiante2)
estudiantes.append(estudiante3)
estudiantes.append(estudiante4)

print("Estudiantes registrados: ",estudiantes)
print("Total de estudiantes registrados:: ",len(estudiantes))

if len(estudiantes) == cantidad_estudiantes:
    print("¿Coincide con la cantidad prevista?: Sí")

print("Primer estudiante: ",estudiantes[0])
print("Último estudiante: ",estudiantes[-1])
print("Orden inverso: " , list(reversed(estudiantes)))
