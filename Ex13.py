def numero_mayor(): 
    a = int(input("Introdueixi un nombre "))
    b = int(input("Introdueixi un nombre "))
    if a>b:
        print("El nombre major entre {}, i {} és {}".format(a, b, a))
    elif b>a:
        print("El nombre major entre {}, i {} és {}".format(a, b, b))
    else: 
        print("Els nombres son iguals {} i {}".format(a, b))
    
def menu_principal():
    print("1. Comparar nombres")
    print("2. Sortir")
    return int(input("Introdueixi un nombre "))

#Programa principal 
opció = 1
while opció>0:
    opció = menu_principal()
    match opció:
        case 1: 
            numero_mayor()
        case 2:
            opció=-1
        case other: 
            print("Opció no vàlida")
