def superposicio(llista1, llista2):
    return bool(set(llista1) & set(llista2))
#Programa_Principal
llista_a = [1, 4, 5, 7]
llista_b = [7, 90, 2, 1]

resultado = superposicio(llista_a, llista_b)

print(resultado)