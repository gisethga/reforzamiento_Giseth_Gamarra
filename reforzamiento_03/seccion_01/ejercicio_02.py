"""
Ejercicio 02. Registro de calificaciones
Un docente necesita consultar los resultados de un grupo de estudiantes.
1. Crear un diccionario donde cada clave sea el nombre del estudiante y cada valor sea su nota final.
2. Mostrar los estudiantes aprobados (nota mayor o igual a 11).
3. Calcular el promedio general e identificar el nombre y la nota del estudiante con mayor
calificación.
4. Indicar cuántos estudiantes desaprobaron.
Datos iniciales sugeridos: notas = {"Ana": 16, "Luis": 10, "María": 18, "Pedro": 8, "Rosa": 14}.
"""

estudiantes_notas = {
    "Juan": 15,
    "Mariela": 20,
    "Lucia": 17,
    "Claudia": 18,
    "Fausto": 10
}
desaprobados = {}

suma = 0
nota_maxima = 0
mejor_alumno = ""
print("Los estudiantes y sus notas son:{}".format(estudiantes_notas))
print("Los estudiantes aprobados son:")
for nota in estudiantes_notas:
 if estudiantes_notas[nota] >= 11:
    print(nota)
 else:
    desaprobados[nota] = estudiantes_notas[nota]

 suma += estudiantes_notas[nota]

 if estudiantes_notas[nota] > nota_maxima:
     nota_maxima = estudiantes_notas[nota]
     mejor_alumno = nota


promedio= suma / len(estudiantes_notas)
print("El promedio general es: {}".format(promedio))
print("El alumno con la mayor calificación es {} con una nota de: {}".format(mejor_alumno, nota_maxima))
print("Los estudiantes desaprobados son: {}".format(len(desaprobados)))
