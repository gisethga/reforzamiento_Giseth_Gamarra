var_str = 40
print("Primer valor: ",var_str)
var_int = 10
print("Segundo valor: ",var_int)
var_conv = int(var_str)
var_suma = var_int + var_conv
print("Suma: ",var_suma)
var_multiplicacion = var_int * var_conv
print("Multiplicacion: ",var_multiplicacion)
var_promedio = float(var_suma / 2)
print(f"El promedio es: {var_promedio:.2f}")
Rslt_Suma_Str = str(var_suma)
print("El tipo de dato es: ",type(var_conv))
print("El resultado final es: "+Rslt_Suma_Str)