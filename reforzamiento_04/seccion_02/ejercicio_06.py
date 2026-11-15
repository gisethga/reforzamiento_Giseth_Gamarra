"""
Ejercicio 06. Cálculo de bonificaciones según el tipo de empleado
Una empresa necesita calcular las remuneraciones de sus trabajadores considerando diferentes
porcentajes de bonificación según su modalidad de contratación.
Requisitos:
• Crear una clase Empleado con los atributos nombre y sueldo_base, inicializados mediante un
constructor.
• Implementar un método calcular_sueldo_final() que retorne el sueldo base.
• Crear una clase EmpleadoTiempoCompleto que herede de Empleado y sobrescriba
calcular_sueldo_final() para aplicar una bonificación del 15 %.
• Crear una clase EmpleadoMedioTiempo que también herede de Empleado y sobrescriba el
mismo método para aplicar una bonificación del 5 %.
• Implementar un método p ara mostrar los datos del empleado, su modalidad de contratación y
su sueldo final.
• Crear al menos dos objetos de cada clase hija, utilizando diferentes nombres y sueldos.
• Mostrar los resultados de todos los empleados registrados.
Nota: Las bonificaciones deberán calcularse mediante los métodos de cada clase hija, sin modificar el
sueldo base.
"""

class empleado():
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo_final(self):
        return self.sueldo_base

    def mostrar_datos(self):
        print(f"Sueldo Final: S/{self.calcular_sueldo_final():.2f}")

class EmpleadoTiempoCompleto(empleado):

    def calcular_sueldo_final(self):
        bonificacion = 1.15 * self.sueldo_base
        return bonificacion

    def mostrar_datos(self):
        print(f"Empleado: {self.nombre} tiene como sueldo S/.{self.sueldo_base}")
        print("Modalidad: Tiempo Completo")
        super().mostrar_datos()
        print("-" * 30)

class EmpleadoMedioTiempo(empleado):

    def calcular_sueldo_final(self):
        bonificacion = 1.05 * self.sueldo_base
        return bonificacion

    def mostrar_datos(self):
        print(f"Empleado: {self.nombre} tiene como sueldo S/.{self.sueldo_base}")
        print("Modalidad: Medio Tiempo")
        super().mostrar_datos()
        print("-" * 30)

emp1 = EmpleadoTiempoCompleto("Ana Gómez", 2500)

emp2 = EmpleadoTiempoCompleto("Carlos Ruiz", 3200)

emp3 = EmpleadoMedioTiempo("Luis Torres", 1200)
emp4 = EmpleadoMedioTiempo("María Silva", 1500)


empleados = [emp1, emp2, emp3, emp4]


for empleado in empleados:
    empleado.mostrar_datos()