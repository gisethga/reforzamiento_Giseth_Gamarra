temperatura_1 = 21.5
temperatura_2 =  18.2
fahrenheit_1 = (temperatura_1 * (9 / 5)) + 32
fahrenheit_2 = (temperatura_2 * (9 / 5)) + 32
kelvin_1 = (temperatura_1 + 273.15)
kelvin_2 = (temperatura_2 + 273.15)
diferencia = (temperatura_1 - temperatura_2)
print("Temperatura 1: {} °C" .format(temperatura_1))
print("Fahrenheit: {}° F" .format(fahrenheit_1))
print("Kelvin: {} K" .format(kelvin_1))
print("                               ")
print("Temperatura2: {} °C".format(temperatura_2))
print(f"Fahrenheit: {fahrenheit_2:.2f} °F ")
print(f"Kelvin: {kelvin_2:.2f} K")
print(f"Diferencia de temperaturas: {diferencia:.2f} °C")

