from operator import concat

var_nombre = "Karina"
var_apll_pat = " Ruiz"
var_apll_mat = " Almirante"
nombre_completo = concat(var_nombre,concat( var_apll_pat, var_apll_mat))

mi_saludo = "Saludo: ¡HI {}!.".format(nombre_completo)
print(mi_saludo)
print("Nombre completo: ",nombre_completo)
print("Cantidad de caracteres: {}".format(len(nombre_completo)))




