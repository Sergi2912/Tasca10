
def canvi(l,m,n):
     print("{}{} \n {}".format(l, m,n))
     l='Adéu, '
     m='Joan'
     n='Que vagi be'
     print("2) {}{} \n {}".format(l, m,n))
#Progrma principal
a="Hola, "
b="Ramis."
c="Com estàs?"
print("El valor de la variable abans de canviar és: {}{}\n {}".format(a))
canvi(a, b, c)
print("El valor de la variable després de canviar és: {}{} \n {}".format(a))


















""" 
def major(x,y):
    if x>y:
        return x
    else:
        return y
a = int (input("Intro el 1r número. "))
b = int (input("Intro el 2n número: "))
c = major(a,b)
print("El major de {} i {} és {}".format(a, b, c))
"""






"""def intercanvi(a,b):
    return b,a
x='a'
y='b'
print("El valor d'x és {} i el d'y és {}".format(x,y))
x,y = intercanvi(x,y)
print("Després de l'intercanvi, el valor d'x és {} i el d'y és {}".format(x,y))
"""

"""
# Aquet programa es un pas per referencia, canvi en una llista
def canvi(l):
    x =int(input("Introdueix la posició a canviar: ")) # Nombre aleatori a elegir
    l[x]=input("Introdueix el valor a inserir: ")# Es decideix avont o vols posar
#Progrma principal
a=[3, 4, 5, 6, 7, 8, "a", (1,3),[3,4],10]#Creació de la llista
print("El valor de la llista abans de canviar és: {}".format(a))# Retorna sa llista
canvi(a)#Modifica
print("El valor de la llista després de canviar és: {}".format(a))# Retorna la llista altre vegada amb els canvis
"""


"""
def canvi(l):
    l=(1,2,6, 8)
#Progrma principal
a=(3, 5, 7, 9, 10)
print("El valor de la tupla abans de canviar és: {}".format(a))
canvi(a)
print("El valor de la tupla després de canviar és: {}".format(a))
"""





"""def canvi(l):
     x =int(input("Introdueix el valor a inserir al conjunt: "))
     l.add(x)
#Progrma principal
a={3, 5, 7, 9, 10}
print("El valor de la conjunt abans de canviar és: {}".format(a))
canvi(a)
print("El valor de la conjunt després de canviar és: {}".format(a))
"""


"""def canvi(l):
     x=input("Introdueix el valor a inserir al conjunt: ")
     l[x]=int(input("Introdueinx el nou valor per aquesta clau: "))
#Progrma principal
a={'a':3, 'b':5, 'c':7, 'd':9, 'e':10}
print("El valor del diccionari abans de canviar és: {}".format(a))
canvi(a)
print("El valor del diccionari després de canviar és: {}".format(a))"""