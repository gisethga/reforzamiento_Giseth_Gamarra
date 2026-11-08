"""
Ejercicio 04. Suma de dígitos y comparación
Se tienen dos números enteros positivos y se desea analizar la suma de sus dígitos.
1. Crear una función que reciba un entero positivo y devuelva la suma de sus dígitos.
2. Utilizarla para analizar dos números predefinidos.
3. Mostrar cuál de los dos tiene mayor suma de dígitos, o indicar que existe un empate.
4. Mostrar cuáles de los dos números tienen una suma de dígitos menor
"""
from unittest import result


def sumar(numeros):
    numeros_texto = str(abs(numeros))
    largo = len(numeros_texto)
    digito = []
    i=0
    while i < largo:
        digito.append(int(numeros_texto[i]))
        i += 1
    #print(sum(digito))
    return sum(digito)

a = 583
b = 241
uno = sumar(a)
dos = sumar(b)
if uno > dos:
    print("La suma de {} es mayor que {}".format(a, b))
    print("La suma de {} es {}".format(b, dos))
elif uno < dos:
    print("La suma de {} es menor que {}".format(a, b))
    print("La suma de {} es {}".format(a, uno))
else:
    print("La suma de {} y {} son iguales".format(a, b))
    print("La suma de {} es {}".format(a, uno))
    print("La suma de {} es {}".format(b, dos))


