"""
Ejercicio 12. Cálculo de antigüedad laboral
Desarrollar un programa en Python que calcule la antigüedad laboral de un empleado, utilizando automáticamente la fecha actual del sistema, y determine si corresponde aplicar un aumento salarial
Requisitos:
• Crear una función calcular_antiguedad() que reciba la fecha de ingreso y calcule los años completos de servicio utilizando datetime y la fecha actual del sistema
• Crear una función calcular_aumento() que reciba el sueldo actual y los años de antigüedad
• Aplicar un aumento del 20 % si el empleado tiene más de 3 años trabajando, sino mantener su sueldo
• Solicitar mediante consola el nombre, sueldo actual y fecha de ingreso del empleado
• Mostrar el nombre, fecha de ingreso, fecha actual, años de antigüedad, sueldo original, porcentaje aplicado, monto del aumento y sueldo final
• Realizar al menos tres pruebas con empleados de distinta antigüedad, incluyendo casos con y sin aumento.
Nota: Ingresar la fecha en formato DD/MM/AAAA. Obtener automáticamente la fecha actual mediante datetime. Mostrar los importes con solo dos decimales
"""

from datetime import datetime

def calcular_antiguedad(fecha_ingreso):
    fecha_actual = datetime.now()
    anios = fecha_actual.year - fecha_ingreso.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_ingreso.month, fecha_ingreso.day):
        anios -= 1

    return anios

def calcular_aumento(sueldo_actual, anios_antiguedad):
    if anios_antiguedad > 3:
        porcentaje = 20
        monto_aumento = sueldo_actual * 0.20
    else:
        porcentaje = 0
        monto_aumento = 0.0

    sueldo_final = sueldo_actual + monto_aumento
    return porcentaje, monto_aumento, sueldo_final

nombre = input("Ingrese el nombre del empleado: ")
sueldo = float(input("Ingrese el sueldo actual: "))
fecha_ingreso = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ")

fecha_ingreso_dt = datetime.strptime(fecha_ingreso, "%d/%m/%Y")
fecha_actual_dt = datetime.now()

antiguedad = calcular_antiguedad(fecha_ingreso_dt)
porcentaje, aumento, sueldo_final = calcular_aumento(sueldo, antiguedad)

print(f"\nEl empleado {nombre}, ingreso a laborar {fecha_ingreso_dt.strftime('%d/%m/%Y')}")
print(f"Al día de hoy {fecha_actual_dt.strftime('%d/%m/%Y')}, tiene {antiguedad} años de antiguedad")
print(f"Su sueldo es de S/{sueldo:.2f} y tiene un aumento porcentual de {porcentaje}%")
print(f"El monto aumentado es de S/{aumento:.2f}; su sueldo final es de S/{sueldo_final:.2f}")
