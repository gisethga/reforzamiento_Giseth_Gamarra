"""
Ejercicio 08. Generación y análisis de números aleatorios mediante módulos
Desarrollar un programa que permita generar, ordenar y analizar números aleatorios mediante funciones organizadas en un módulo independiente.
Requisitos:
• Crear un archivo operaciones.py con tres funciones: generar una lista de 30 números enteros aleatorios entre 0 y 100, ordenar una lista de menor a mayor y obtener su número mayor.
• Utilizar el módulo random de Python para generar los números aleatorios.
• Crear un archivo main.py que importe y ejecute las funciones de operaciones.py.
• Mostrar en consola la lista original, la lista ordenada y el número mayor obtenido.
• Conservar los elementos y el orden de la lista original después de realizar el ordenamiento.
"""

import random

def generar_lista():
    lista = []

    for i in range(30):
        numero = random.randint(0, 100)
        lista.append(numero)

    return lista

def ordenar_lista(lista):
    return sorted(lista)

def obtener_mayor(lista):
    return max(lista)