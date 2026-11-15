departamento = ['Lima', 'Cusco', 'Arequipa', 'Piura', 'Ica', 'Puno']
print("Lista original:", departamento)
departamento_reemplazo = 'Piura'
print("Departamento a reemplazar:", departamento_reemplazo)
nueva_departamento = "Tumbes"
print("Nuevo departamento:", nueva_departamento)
if departamento_reemplazo in departamento:
    indice = departamento.index(departamento_reemplazo)
    departamento[indice] = nueva_departamento
    print("Lista actualizada:", departamento)
else:
    print("No fue encontrado")

print("Cantidad de departamentos:", len(departamento))

