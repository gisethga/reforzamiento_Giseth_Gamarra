var_sueldo = 500
print("Sueldo inicial: S/",var_sueldo)
if var_sueldo % 2 == 0:
    print("Clasificación: Número par")
if var_sueldo % 2 != 0:
    print("Clasificación: Número impar")
var_bono = var_sueldo * 0.12
print(f"Bono (12%): S/ {var_bono:.2f}")
sueldo_total = var_sueldo + var_bono
print(f"Sueldo total: {sueldo_total:.2f}")
print("Residuo de dividir entre 7:",(var_sueldo % 7))
