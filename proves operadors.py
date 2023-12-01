def llegir_llistes():
    a = '1'
    l=[]
    while a!='a':
        a=int(input("Introdueixi un número diferent a 'a': "))
        if a !='a':
            l.append(int(a))
        else:
            return l

#Programa principal
a = llegir_llista():
b = llegir_llista():
c=[]
for i in range(len(a)):
    c.append(a[i]*b[i])
print("La multiplicació de la llista {} per la llista {} és {}".format(a,b,c))










print(a)
a[2]=15
print(b)

a = [2, 3, 4]
b = [2, 5, 6, 10]
a **=b # = a menys b
print(a)









"""a=int(input("Introdueixi el primer valor: "))
b=int(input("Introdueixi el segon valor: "))
a = b
print(a)
a=10
print(b)
"""




