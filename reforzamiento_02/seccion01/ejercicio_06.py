nombre_cliente = "Juan Perez"
print("Cliente:",nombre_cliente)
nombre_producto = "Coca Cola"
print("Producto:",nombre_producto)
precio_unitario = 2.50
print(f"Precio unitario: S/ {precio_unitario:.2f}")
cantidad = 2
print("Cantidad:",cantidad)
subtotal = cantidad * precio_unitario
print(f"Subtotal: S/ {subtotal:.2f}")

if (cantidad >= 3):
    descuento = (subtotal * 0.10)
    print(f"Descuento: S/ {descuento:.2f}")
if (cantidad < 3):
    descuento = 0
    print(f"Descuento: S/ {descuento:.2f}")
print(f"Total a pagar: S/ {(subtotal - descuento):.2f}")



