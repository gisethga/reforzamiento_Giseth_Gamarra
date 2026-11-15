"""
Ejercicio 09. Operaciones matemáticas mediante módulos
Desarrollar un programa en Python que permita calcular diferentes operaciones matemáticas a partir de un número ingresado por el usuario, organizando las funciones en un módulo independiente.
Requisitos:
• Crear un archivo calculos.py con tres funciones que reciban un número y retornen su raíz cuadrada (utilizando math), su cuadrado y su cubo, respectivamente.
• Crear un archivo main.py que importe y utilice las funciones de calculos.py.
• Solicitar mediante consola un número y validar que sea numérico y mayor o igual que cero.
• Mostrar el número ingresado y los resultados de las tres operaciones.
• Realizar al menos tres pruebas con valores diferentes, incluyendo una entrada no válida.
Nota: Los cálculos deberán implementarse en calculos.py; main.py se encargará de solicitar el dato, comprobar su validez y presentar los resultados. No utilizar librerías externas
"""

import math

def raiz_cuadrada(numero):
        raiz = math.sqrt(numero)
        return raiz

def cuadrado(numero):
        cuadrado_rslt = numero ** 2
        return cuadrado_rslt

def cubo(numero):
        cubo_rslt = numero ** 3
        return cubo_rslt