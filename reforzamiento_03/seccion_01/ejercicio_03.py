"""
Ejercicio 03. Carrito de compras
Un cliente selecciona productos de una tienda. Los precios se encuentran registrados en un
diccionario.
1. Crear un diccionario con el nombre de cada producto y su precio, y una lista con los productos
elegidos.
2. Recorrer la lista de compras y calcular el importe total usando los precios del diccionario.
3. Aplicar un descuento de 10 % si el importe total supera S/ 200.
4. Verificar que cada producto seleccionado exista en el diccionario de precios. Si no está registrado,
mostrar un mensaje informativo y continuar con los productos válidos. Al finalizar, mostrar el
subtotal, el descuento aplicado y el total a pagar.
Datos iniciales sugeridos: precios = {"Teclado": 75, "Mouse": 45, "Audífonos": 120, "USB": 35}; carrito
= ["Teclado", "Audífonos", "USB"].
Ejemplo de salida esperada:
Productos seleccionados:
Teclado: S/ 75.00
Audífonos: S/ 120.00
USB: S/ 35.00
Subtotal: S/ 230.00
Descuento (10 %): S/ 23.00
Total a pagar: S/ 207.00
"""

prdts_tienda = {
    "lapicero": 3,
    "cartulina": 1,
    "resaltador" : 2,
    "cuaderno": 5,
    "plumones": 23,
    "colores": 12
}
print("El diccionario de productos es : {}".format(prdts_tienda))
impt_total = 0
impt_total = 0
dsct = 0
productos = ["cuaderno", "lapiceros", "resaltador"]
print("La lista de productos es {}: ".format(productos))

print("Productos seleccionados:")

for producto in productos:
    try:
        prdts_tienda[producto]
    except KeyError:
        print("No se encontro el producto: {}".format(producto))
    else:
        print(f"{producto}: S/{prdts_tienda[producto]:.2f}")
        impt_total += prdts_tienda[producto]

if impt_total > 200:
    dsct = impt_total * 0.10
else:
    dsct = 0
total = impt_total + dsct
print(f"Subtotal: {impt_total:.2f}")
print(f"Descuento: {dsct:.2f}")
print(f"Total a pagar: {total:.2f}")
