"""
Ejercicio 05. Eliminación de un elemento de una lista
Se necesita actualizar una lista eliminando un valor específico.
1. Crear una función que reciba una lista y un valor por eliminar.
2. La función debe devolver una nueva lista sin la primera aparición de ese valor; si no existe,
devolver una lista equivalente a la original.
3. Mostrar la lista original, el valor buscado y la lista resultante.
4. Probar la función con un valor existente y otro inexistente, sin modificar la lista original.
Datos iniciales sugeridos: numeros = [10, 20, 30, 20, 40]; eliminar = 20.
"""

numeros = [10, 20, 30, 20, 40]

def borra(lista, valor):

    nueva_lista = lista.copy()
    try:
        nueva_lista.remove(valor)
    except ValueError:
        print("No se encontro el valor: {}".format(valor)),
        print("La lista original es: {}".format(lista))
    else:
        return (
            print("La lista original es: {}".format(lista)),
            print("El valor borrado es {}".format(valor)),
            print("La nueva lista es: {}".format(nueva_lista))
        )

borra(numeros, 29)

