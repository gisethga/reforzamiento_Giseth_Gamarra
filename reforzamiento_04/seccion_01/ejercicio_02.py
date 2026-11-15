"""
Ejercicio 02. Actualización de elementos de una lista
Desarrollar un programa que permita reemplazar elementos de una lista de números enteros, controlando los errores que puedan presentarse durante la actualización.
Requisitos:
* Crear una lista inicial con los siguientes elementos: numeros = [2, 6, 10, 4, 5, 23, 1].
* Crear una función actualizar_elemento(lista, indice, valor) que reemplace un elemento en la posición indicada.
* Solicitar mediante consola el índice del elemento que se desea modificar y el nuevo valor.
* Controlar IndexError cuando el índice esté fuera del rango válido de la lista.
* Controlar TypeError cuando el nuevo valor no sea de tipo entero.
* Controlar ValueError cuando el índice ingresado no pueda convertirse a un número entero.
* Detectar el tipo incorrecto del nuevo valor y generar explícitamente TypeError utilizando raise.
* Mostrar mensajes descriptivos que permitan identificar la causa de cada error.
* Cuando la operación sea válida, actualizar el elemento y mostrar la lista resultante.
* Realizar al menos cuatro pruebas: actualización válida, índice inexistente, índice no numérico y valor no válido.
* El programa deberá continuar funcionando después de cada operación incorrecta.
Nota: Los índices válidos serán desde 0 hasta la última posición de la lista. No se admitirán índices negativos.
"""

numeros = [2, 6, 10, 4, 5, 23, 1]

def actualizar_elemento(lista = numeros):
    print("\nLa lista original es: {}".format(lista))
    while True:
        indice = input("\nIngrese el indice que desea modificar de la lista:")
        valor = input("Ingrese el nuevo valor:")

        try:
            n_indice = int(indice)

            if n_indice < 0:
                raise IndexError

            if not valor.lstrip("-").isdigit():
                raise TypeError("El nuevo valor debe ser de tipo entero.")

            n_valor = int(valor)

            lista[n_indice] = n_valor

        except IndexError:
            print("Error Index: El índice {}, está fuera del rango de la lista, su rango es de: 0 a {}. No se admiten negativos ".format(indice, len(lista)-1))
        except TypeError as error:
            print(f"Error Type:El tipo de dato ingresado es {type(valor)}. {error}")
        except ValueError:
            print("Error Value: El indice {} no es un número entero válido".format(indice))
        else:
            print(f"La nueva lista es: {lista}")
            break


actualizar_elemento()