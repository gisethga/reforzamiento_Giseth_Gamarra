"""
Ejercicio 01. Control de inventario
Una tienda necesita identificar los productos que tienen pocas existencias.
1. Crear una lista con los nombres de cinco productos y otra con sus cantidades disponibles,
respetando el mismo orden.
2. Mostrar cada producto junto con su cantidad.
3. Identificar los productos con menos de cinco unidades y calcular el total de unidades
registradas.
4. Mostrar un mensaje si ningún producto tiene stock bajo.
Datos iniciales sugeridos: productos = ["Arroz", "Azúcar", "Aceite", "Leche", "Fideos"]; cantidades
= [8, 3, 12, 2, 6].
"""

# Lista inicial de productos
list_prdt = ["Chocolate", "Leche", "Azucar", "Paneton", "Mantequilla"]
list_cant = [20, 50, 4, 10, 20]
prdt_sstck = []
cant_sstck = []

# Mostrar los productos registrados
i = 0
ttl_und = 0
print("Productos con stock:")
for cantidad in list_cant:
    if list_cant[i] < 5:
        prdt_sstck.append(list_prdt[i])
        cant_sstck.append(list_cant[i])
    else:
        print("{}: {} unidades".format(list_prdt[i], list_cant[i]))
    ttl_und += list_cant[i]
    i += 1
print("Total de unidades disponibles: {}".format(ttl_und))

i1 = 0
if len(prdt_sstck) == 0:
    print("Contamos con stock")
else:
    print("Productos con menos de 5 unidades:")
    for comprar in prdt_sstck:
        print("{}: {} unidades".format(prdt_sstck[i1], cant_sstck[i1]))
        i1 += 1