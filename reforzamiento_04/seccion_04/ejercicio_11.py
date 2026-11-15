"""
Ejercicio 11. Decorador para conteo y validación de argumentos
Desarrollar un programa que utilice un decorador para contar y validar los argumentos recibidos por una función encargada de sumar números enteros.
Requisitos:
• Crear un decorador llamado conteo_parametros que reciba argumentos mediante *args y **kwargs.
• Mostrar la cantidad total de argumentos recibidos, incluyendo posicionales y argumentos con nombre.
• Crear una función que calcule la suma de todos los números recibidos.
• Validar que todos los argumentos sean enteros, excluyendo valores booleanos.
• Si algún argumento no es válido, mostrar: "Solo se admiten números enteros. No se podrá realizar la suma", sin ejecutar la función.
• Si todos son válidos, ejecutar la función decorada y mostrar el resultado.
• Al finalizar cada ejecución, mostrar: "La función decoradora terminó de ejecutarse correctamente".
• Realizar al menos tres pruebas: solo argumentos posicionales, combinación de *args y **kwargs, y un caso con valores no válidos.
Nota: El decorador realizará el conteo y la validación de argumentos antes de permitir la ejecución de la función decorada
V. MANEJO DE FECHAS
"""

def conteo_parametros(funcion):
    def funcionC(*args, **kwargs):
        total_argumentos = len(args) + len(kwargs)
        print(f"Cantidad total de argumentos recibidos: {total_argumentos}")

        lista_valores = list(args) + list(kwargs.values())

        son_validos = True
        for valor in lista_valores:
            if type(valor) is not int:
                son_validos = False
                break
        if not son_validos:
            print("Solo se admiten números enteros. No se podrá realizar la suma")
            resultado = None
        else:
            resultado = funcion(*args, **kwargs)
            print(f"Resultado de la suma: {resultado}")

        print("La función decoradora terminó de ejecutarse correctamente\n")
        return resultado
    return funcionC

@conteo_parametros
def sumar_enteros(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

# 3. Ejecución de las pruebas solicitadas
print("\n--- PRUEBA 1 ---")
sumar_enteros(10, 20, 30, 40)

print("\n--- PRUEBA 2 ---")
sumar_enteros(5, 15, num1=25, num2=55)

print("\n--- PRUEBA 3 ---")
sumar_enteros(10, "hola", num1=True)