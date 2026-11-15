"""
Ejercicio 07. Validación de nombres de usuario mediante módulos
Desarrollar un programa para validar nombres de usuario mediante una función definida en un módulo independiente.
Requisitos:
• Crear un archivo validaciones.py con una función que reciba el nombre de usuario como parámetro.
• Validar que el usuario tenga entre 7 y 12 caracteres y contenga únicamente letras y números.
• Retornar los siguientes mensajes según corresponda:
• Menos de 7 caracteres: "El nombre de usuario debe contener al menos 7 caracteres".
• Más de 12 caracteres: "El nombre de usuario no puede contener más de 12 caracteres".
• Caracteres no alfanuméricos: "El nombre de usuario puede contener solo letras y números".
• Retornar True cuando el nombre de usuario cumpla todas las condiciones.
• Crear un archivo main.py que importe y utilice la función de validaciones.py.
• Realizar al menos cinco pruebas con nombres válidos e inválidos y mostrar los resultados en consola.
Nota: Las validaciones deberán implementarse en validaciones.py y las pruebas ejecutarse desde main.py.
"""

def recibe_usuario(nombre):
    if not nombre.isalnum():
        print("El nombre de usuario {} solo puede contener letras y números".format(nombre))
    else:
        largo = len(nombre)
        if largo < 7:
            print("El nombre de usuario {}, debe contener al menos 7 caracteres".format(nombre))
        elif largo > 12:
            print("El nombre de usuario {}, no puede contener más de 12 caracteres".format(nombre))
        else:
            print ("True")
            return True