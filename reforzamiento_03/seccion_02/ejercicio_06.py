"""
Ejercicio 06. Análisis de ventas semanales
Una tienda registra las ventas de siete días y necesita un resumen mediante funciones.
1. Crear una función que calcule el total vendido durante la semana.
2. Crear otra función que calcule el promedio diario de ventas.
3. Crear una función que identifique la venta máxima y otra que cuente cuántos días superaron el
promedio.
4. Mostrar los cuatro resultados e indicar qué representa cada uno.
Datos iniciales sugeridos: ventas = [150, 220, 180, 300, 175, 260, 190].
"""
ventas = [150, 220, 180, 300, 175, 260, 190]
def total(lista):
    total = 0
    for numero in lista:
        total += numero
    return total
resultado_total = total(ventas)
print(f"Total de ventas: S/{resultado_total:.2f}")

def promedio(lista):
    promedio = 0
    for numero in lista:
        promedio += numero
    promedio = promedio / len(lista)
    return promedio
resultado_promedio = promedio(ventas)
print(f"Promedio de ventas: S/ {resultado_promedio:.2f}")


def maxima(lista):
    return max(lista)
resultado_max = maxima(ventas)
print(f"la maxima venta es: S/ {resultado_max:.2f}")

def dia_mayor_promedio(lista, valor_promedio):
    dia = []
    for numero in lista:
        if numero > valor_promedio:
            dia = lista.index(numero)+1
    return dia
resul_dmp= dia_mayor_promedio(ventas, resultado_promedio)
print("El día que supera el promedio de ventas es: {}".format(resul_dmp))