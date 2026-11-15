"""
Ejercicio 03. Consulta de información personal
Desarrollar un programa que permita consultar información registrada en un diccionario y controlar los errores cuando se intente acceder a una clave inexistente.

• Crear una función consultar_dato(persona, clave) que permita consultar el valor de una clave solicitada mediante consola.
• Utilizar try/except para capturar KeyError cuando se intente acceder a una clave inexistente.
• Si la clave existe, mostrar su nombre y valor; de lo contrario, mostrar: "Error: La clave ingresada no existe en el diccionario".
• Realizar al menos cinco consultas (tres válidas y dos inválidas), garantizando que el programa continúe ejecutándose después de cada error.
"""

persona = { "nombre": "Xavier", "apellido_paterno": "Rodriguez", "apellido_materno": "Gonzales", "dni": "63325345", "edad": 28, "correo": "xavier.rodriguez@gmail.com", "telefono": "987654321", "direccion": "Av. Los Olivos 450", "ciudad": "Lima", "profesion": "Ingeniero de Software", "empresa": "Tech Solutions", "salario": 4500.00, "estado_civil": "Soltero" }

def consultar_dato():
    while True:

        clave = input("Ingrese la clave que desea consultar:").strip().lower()
        try:
            consulta = persona[clave]
        except KeyError:
            print(f"Error: La clave {clave} ingresada no existe en el diccionario")
        else:
            print (f"\n{clave} es: {consulta}")
            break


consultar_dato()