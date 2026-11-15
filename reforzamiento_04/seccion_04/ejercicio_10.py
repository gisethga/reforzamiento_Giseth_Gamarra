"""
Ejercicio 10. Decorador para multiplicación de números
Crea un programa que utilice un decorador para mostrar mensajes antes y después de ejecutar una función encargada de multiplicar números.
Requisitos:
• Crear un decorador que permita recibir y transmitir argumentos mediante *args y **kwargs.
• Antes de ejecutar la función decorada, imprimir: "Está por ejecutarse la función"
• Crear una función que multiplique seis números, recibiendo tres como argumentos posicionales y tres como argumentos con nombre.
• Retornar y mostrar el resultado de la multiplicación y, después de ejecutar la función, mostrar: "La función ha sido ejecutada correctamente"
• Ejecutar la función decorada al menos tres veces utilizando diferentes valores numéricos
"""

def funcionDecoradora(funcion):
    def funcionC(*args, **kwargs):
        print("Esta por ejecutarse la función")
        resultado = funcion(*args, **kwargs)
        print(f"Resultado de la multiplicación: {resultado}")
        print("La función ha sido ejecutada correctamente\n")
        return resultado
    return funcionC

@funcionDecoradora
def multiplicar(a, b, c, d=1, e=1, f=1):
    return a * b * c * d * e * f

print("\n--- PRUEBA 1 ---")
multiplicar(2, 3, 4, d=5, e=6, f=7)

print("\n--- PRUEBA 2 ---")
multiplicar(1, 2, 3, d=4, e=5, f=10)

print("\n--- PRUEBA 3 ---")
multiplicar(10, 10, 2, d=2, e=5, f=1)