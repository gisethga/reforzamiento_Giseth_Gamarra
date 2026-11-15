var1 = 15.8
print("Primer valor decimal:", var1)
var2 = 5.7
print("Segundo valor decimal:", var2)
conv1 = int(var1)
print("Primer entero:", conv1)
conv2 = int(var2)
print("Segundo entero:", conv2)
if conv1 % conv2 == 0:
    print("¿El primer número es múltiplo del segundo?: Sí")
else:
    print("¿El primer número es múltiplo del segundo?: no")
cociente = conv1 // conv2

residuo = conv1 % conv2
print(f"Residuo: {residuo:.2f}")
print(f"Cociente:  {cociente:.2f}")


