"""
Ejercicio 01. División segura
Crea un programa que permita realizar divisiones entre dos números ingresados por el usuario, implementando el manejo de excepciones.
Requisitos:
• Crear una función division_segura(a, b) que reciba dos valores y realice la división.
• Solicitar ambos números mediante consola, utilizando try, except y finally para controlar los errores.
• Capturar ZeroDivisionError y mostrar: "Error: No se puede dividir entre cero".
• Capturar ValueError y mostrar: "Error: Debe ingresar valores numéricos".
• Mostrar el resultado cuando la operación sea válida y siempre imprimir "Operación finalizada".
• Realizar al menos tres pruebas: una división válida, una entre cero y una entrada no numérica, asegurando que el programa continúe después de cada error.
Nota: Controlar ZeroDivisionError y ValueError, la conversión de los datos ingresados deberá encontrarse protegida por el manejo de excepciones también.
"""

def division_segura():

    while True: #permite repetir en bucle la acción
        a = input("Ingrese el dividendo:")
        b = input("Ingrese el divisor:")
        try:
            valor_1 = int(a)
            valor_2 = int(b)
            resultado = valor_1/valor_2
        except ValueError:
                print("Error: Debe ingresar valores numéricos")
        except ZeroDivisionError:
                print("Error: No se puede dividir entre cero")
        else:
            print(f"El resultado de la division es: {resultado}")
            break
        finally:
                print("Operación finalizada")
    return resultado


division_segura()