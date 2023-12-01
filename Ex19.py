"""
def es_palindrom(cadena)
    return cadena ==[ ::-1]

print(es_palindrom("Soc del Ramis")) # Retorna True
print(es_palindrom("Prova")) # Retorna False

if
"""


def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False