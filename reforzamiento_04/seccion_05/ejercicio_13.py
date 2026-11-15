"""
Ejercicio 13. Cálculo y seguimiento de fechas de vencimiento
Crear un programa que calcule la fecha de vencimiento de una obligación a partir de una fecha inicial y un plazo expresado en días y determina su situación respecto de la fecha actual.
Requisitos:
• Crear una función calcular_vencimiento() que reciba una fecha inicial y un plazo en días, utilizando datetime y timedelta para retornar la fecha de vencimiento.
• Crear una función evaluar_vencimiento() que compare la fecha de vencimiento con la fecha actual del sistema
• Determinar si la obligación está pendiente, vence hoy o ya venció, indicando cuántos días faltan o han transcurrido, según corresponda
• Solicitar mediante consola la fecha inicial y el plazo en días
• Mostrar la fecha inicial, el plazo, la fecha de vencimiento, la fecha actual y el resultado de la evaluación
• Realizar al menos tres pruebas: un vencimiento futuro, uno en la fecha actual y otro ya vencido.
Nota: Utilizar el formato DD/MM/AAAA para las fechas. Obtener automáticamente la fecha actual del sistema. El plazo deberá ser un número entero no negativo
"""


from datetime import datetime, timedelta


def calcular_vencimiento(fecha_inicial, plazo_dias):
    fecha_vencimiento = fecha_inicial + timedelta(days=plazo_dias)
    return fecha_vencimiento

def evaluar_vencimiento(fecha_vencimiento):
    hoy = datetime.now().date()
    vencimiento = fecha_vencimiento.date()
    diferencia_dias = (vencimiento - hoy).days
    
    if diferencia_dias > 0:
        return f"Obligación PENDIENTE. Faltan {diferencia_dias} día(s) para el vencimiento."
    elif diferencia_dias == 0:
        return "La obligación VENCE HOY."
    else:
        dias_pasados = abs(diferencia_dias)
        return f"Obligación VENCIDA. Han transcurrido {dias_pasados} día(s) desde su vencimiento."


for i in range(1, 4):
    print(f"\n    Prueba {i}    ")

    fecha_texto = input("Ingrese la fecha inicial (DD/MM/AAAA): ")
    plazo = int(input("Ingrese el plazo en días (entero no negativo): "))
    
    # Validar que el plazo sea un entero no negativo
    if plazo < 0:
        print("Error: El plazo debe ser un número entero mayor o igual a cero.")
        continue
        
    # Convertir texto a objeto datetime
    fecha_inicial_dt = datetime.strptime(fecha_texto, "%d/%m/%Y")
    fecha_actual_dt = datetime.now()
    
    # Ejecutar las funciones
    fecha_venc_dt = calcular_vencimiento(fecha_inicial_dt, plazo)
    resultado_evaluacion = evaluar_vencimiento(fecha_venc_dt)
    
    # Mostrar resultados en consola
    print("\n--- Detalle de la Obligación ---")
    print(f"Fecha inicial: {fecha_inicial_dt.strftime('%d/%m/%Y')}")
    print(f"Plazo: {plazo} día(s)")
    print(f"Fecha de vencimiento: {fecha_venc_dt.strftime('%d/%m/%Y')}")
    print(f"Fecha actual: {fecha_actual_dt.strftime('%d/%m/%Y')}")
    print(f"Estado: {resultado_evaluacion}")