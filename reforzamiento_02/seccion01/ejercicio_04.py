var_nota1 = 15.50
var_nota2 = 16.75
var_nota3 = 18.25
var_nota4 = 20.00
var_nota5 = 17.45
print("Notas: {}, {}, {}, {}, {} ".format(var_nota1,var_nota2,var_nota3,var_nota4,var_nota5))
var_suma = (var_nota1 + var_nota2 + var_nota3 + var_nota4 + var_nota5)
print("Suma de notas: ",var_suma)
promedio = var_suma / 5
print("Promedio: ",promedio)
diferencia = 20.00 - 15.50
print("Diferencia entre nota mayor y menor:", diferencia)
if promedio >= 11:
    print("APROBADO")
if promedio < 11:
    print("DESAPROBADO")



