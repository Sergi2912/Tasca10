"""
def sumar_llista(llista):

    return sum(llista)


def multiplicar_llista(llista):

    resultat = 1

    for num in llista:

        resultat *= num

    return resultat

print(sumar_llista([1,2,3,4])) 

print(multiplicar_llista([1,2,3,4])) 
"""


def llegir_llista():
    a = '0'
    l = []
    while a != '!!':
        a = input("Introdueixi un element de la llista i '!!' per acabar: ")
        if a == '!!':
            return l
        else:
            l.append(int(a))

def sumar_llista(l):
    s = 0
    for e in l:
        s += e
    print("La suma de tots els elements de la llista {}, és {}".format(l, s))

# Principal
llista = llegir_llista()
sumar_llista(llista)
