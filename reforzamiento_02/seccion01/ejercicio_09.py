nombre = "Elizabeth Rios"
print("Nombre:" , nombre)
peso = 56.0
print("Peso: {} kg" .format(peso))
estatura = 1.75
print("Estatura: {} m" .format(estatura))
imc = peso / (estatura ** 2)
print(f"IMC calculado: {imc:.2f}")
if peso < 18.5:
    print("Clasificación: Bajo peso")
if peso >= 18.5 and peso < 25:
    print("Clasificación: Peso normal")
if peso >= 25 and peso < 30:
    print("Clasificación: Sobrepeso")
if peso >30:
    print("Clasificación: Obesidad")