"""
Ejercicio 04. Sistema de préstamos para empleados
Una empresa necesita implementar un sistema que permita registrar los datos de sus trabajadores y
determinar si cumplen los requisitos para acceder a un préstamo.
Requisitos:
• Crear una clase Persona con los atributos nombre, edad, sueldo mensual y meses trabajados,
inicializados mediante un constructor.
• Crear métodos para la clase para mostrar sus datos, verificar si es mayor de edad y calcular
una bonificación del 20 % de su sueldo únicamente si es mayor de edad.
• Crear una clase PersonaPrestamo que herede de Persona y evalúe si el empleado tiene más de
25 años y más de 12 meses trabajados.
• Si cumple ambas condiciones, calcular un préstamo equivalente a 10 veces su sueldo mensual,
sino mostrar que no puede acceder al préstamo.
• Probar al menos tres objetos de PersonaPrestamo, incluyendo empleados que cumplan y no
cumplan con los requisitos
• Mostrar en terminal los datos de cada empleado, su bonificación y el resultado de la evaluación
del préstamo
"""

class persona:

    #Constructor
    def __init__(self, nombre, edad, sueldo_mensual, meses_trabajados):
        #atributos inicializados en el constructor
        self.nombre = nombre
        self.edad = edad
        self.sueldo_mensual = sueldo_mensual
        self.meses_trabajados = meses_trabajados

    #metodos

    def mostrar_datos(self):
        print("{} tiene {} años".format(self.nombre, self.edad))
        print("Su sueldo actual es S/{:.2f} y tiene {} meses trabajando".format(self.sueldo_mensual, self.meses_trabajados))

    def calcular(self):
        if self.edad > 17:
            bonif = self.sueldo_mensual * 0.20
        else:
            bonif = 0

        print("Su bonificación es S/{:.2f}".format(bonif))

class persona_prestamo(persona):

    def evalua(self):
        if self.edad > 25 and self.meses_trabajados > 12:
            prestamo = self.sueldo_mensual * 10
            print("Sí! Cuenta con la posibilidad de un prestamos por hasta S/{:.2f} como máximo".format(prestamo))
            return prestamo
        else:
            print("No es posible acceder a un prestamo")
            return 0



print("\n--Prueba 1--")
prueba = persona_prestamo ("Teresa",42,5500,13)
prueba.mostrar_datos()
prueba.calcular()
prueba.evalua()
print("\n--Prueba 2--")
prueba = persona_prestamo ("María",33,3500,5)
prueba.mostrar_datos()
prueba.calcular()
prueba.evalua()
print("\n--Prueba 3--")
prueba = persona_prestamo ("Juana",26,1800,18)
prueba.mostrar_datos()
prueba.calcular()
prueba.evalua()