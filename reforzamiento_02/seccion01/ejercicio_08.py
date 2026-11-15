tp_soles = 3.75
print(f"Tipo de cambio: S/: {tp_soles:.2f} ")
monto_1 = 50.00
monto_2 = 30.00
monto_3 = 40.00

monto_1_c = monto_1 / tp_soles
monto_2_c = monto_2 / tp_soles
monto_3_c = monto_3 / tp_soles
print(f"Monto 1: S/ {monto_1:.2f} -> USD {monto_1_c:.2f} ")
print(f"Monto 2: S/ {monto_2:.2f} -> USD {monto_2_c:.2f} ")
print(f"Monto 3: S/ {monto_3:.2f} -> USD {monto_3_c:.2f} ")
total_soles = monto_1 + monto_2 + monto_3
print("                ")
print(f"Total en soles: S/ {total_soles:.2f} ")
total_cambio = total_soles / tp_soles
print(f"Total en dólares: USD {total_cambio:.2f} ")





