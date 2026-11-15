from validaciones import recibe_usuario

prueba_1 = recibe_usuario("Ros@")
prueba_2 = recibe_usuario("R0sa")
prueba_5 = recibe_usuario("ana12")
prueba_3 = recibe_usuario("Rosaura112026")
prueba_4 = recibe_usuario("Rosaura")


from operaciones import generar_lista as paso_uno, ordenar_lista as paso_dos, obtener_mayor as paso_tres


lista_original = paso_uno()
print("\nLista original: {}".format(lista_original))

lista_ordenada = paso_dos(lista_original)
print("Lista ordenada (menor a mayor):{}".format(lista_ordenada))

numero_mayor = paso_tres(lista_original)
print(f"El número mayor es: {numero_mayor}")


from calculos import raiz_cuadrada, cuadrado, cubo

valor = input("\nIngrese un número entero positivo:")
if not valor.isdigit():
    print("Debe ingresar solo números")
elif int(int(valor)) < 0:
    print("Por favor ingrese un número mayor o igual a cero")
else:
    print(f"El número ingresado es {valor}")
    test_raiz = raiz_cuadrada(int(valor))
    print(f"La raiz cuadrada de {valor} es {float(test_raiz):.2f}")
    test_2 = cuadrado(int(valor))
    print(f"El cuadrado de {valor} es {test_2}")
    test_3 = cubo(int(valor))
    print(f"Elcubo de {valor} es {test_3}")