def menu_principal():
    print("""
      Menu principal
        1.Calculadora enters
        2.Calculadora reals
        3.Sortir
        """)
    a=int(input("Elegeixi una opció "))
    return a

def calculadora_enters():
   print("Calculadora d'enters") 
   op = 1 
   while op>0: 
      print("""
            Menú Enters
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Sortir
        """)
      op = int(input("Eligeixi una opció: "))
      match op: 
        case 1: # Sumar
            x = int(input("Introduiexi el primer número: "))
            y = int(input("Introduiexi el segon número: "))
            print("{} + {}".format(x, y, x+y))
        case 2: #Restar
            x = int(input("Introdueixi el primer número: "))
            y = int(input("Itrodueixi el segon número: "))
            print("{} - {}".format(x, y, x-y))
        case 3: # Multiplicar 
            x = int(input("Introdueixi el primer número: "))
            y = int(input("Introdueixi el segon número: "))
            print("{} * {} = {}".format(x, y, x*y))
        case 4: # Dividir
            x = int(input("Introdueixi el primer número"))
            y = int(input("Introdueixi el segon número"))
            print("{} / {} = {}".format(x, y, x/y))
        case 5: # Sortir 
            print("Adéu, ja tornaràs a la calculadora incicial \n\n")
            op=-1      
def calculadora_reals():
   print("Calculadora de reals")
   op = 1 
   while op>0: 
      print("""
            Menú Enters
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Sortir
        """)
      op = int(input("Eligeixi una opció: "))
      match op: 
        case 1: #Sumar
            x = float(input("Introduiexi el primer número: "))
            y = float(input("Introduiexi el segon número: "))
            print("{} + {}".format(x, y, x+y))
        case 2: #Restar
            x = float(input("Introdueixi el primer número: "))
            y = float(input("Itrodueixi el segon número: "))
            print("{} - {}".format(x, y, x-y))
        case 3: # Multiplicar 
            x = float(input("Introdueixi el primer número: "))
            y = float(input("Introdueixi el segon número: "))
            print("{} * {} = {}".format(x, y, x*y))
        case 4: # Dividir
            x = float(input("Introdueixi el primer número"))
            y = float(input("Introdueixi el segon número"))
            print("{} / {} = {}".format(x, y, x/y))
        case 5: # Sortir 
            print("Adéu, ja tornaràs a la calculadora incicial \n\n")
            op=-1 

  #Funcions de canvis de base
#De decimal a binari, octal i hexadecimal
def dectobin(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en binari
    return bin(numero)
def dectooct(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en octal
    return oct(numero)
def dectohex(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en hexadecimal
    return hex(numero)
# De binari a octal, decimal i hexadecimal
def bintodec(numero):
    #Prec: numero sigui una cadena de caràcters
    #Post: Escriu el valor de l'enter en decimal
    a=int(numero,2)
    return dectooct(a)
def bintohex(numero):
    #Prec: numero sigui una cadena de caràcters i en binari
    #Post: escriu el numero en hexadecimal
    a=int(numero,2)
    return dectohex(a) 
#Octal a binari, decimal i hexadecimal
def octtobin (numero):
    a=int(numero, 8)
    return dectobin(a)
def octtodec(numero):
    a = int(numero, 8)
    return a
def occtohex(numero):
    a=int(numero, 8)
    return dectohex (a)


# Hexadecimal a binari, octal i decimal
def hextonum(hex): # Aquesta funció passa qualsevol hexadecimal a un numero
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
    }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posicio = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * valor
        decimal +=pnum
        posicio += 1
    return decimal
def hextobin(numero):
    a=int(numero,16)
    return dectobin(a)
def hextooct(numero):
    a=int(numero,16)
    return dectooct(a)
def hextodec(numero):
    a = int(hextodec2(numero))
    return a

def canvi_de_base():
    print("Canvi de base")
    op3 = 1
    while op3>0:
        print(""""
            Canvi de base
            1. Binari
            2. Octal
            3. Hexadecimal
            4. Sortir
            """)
        
        op3 = int(input("Elige la opción: "))
        match op3:
            case 1: #Binari
                b = input("Introdueixi un número binari ")
                o = dectooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El número binari {} és: \n oct -> {} dec -> {} \n hex -> {}".format(b,o,d,h))
            case 2: #Octal
                o = input("Introdueixi un número binari ")
                b = octtobin(o)
                d = octtodec(o)
                h = occtohex(o)
                print("El número binari {} és: \n oct -> {} dec -> {} \n hex -> {}".format(b,o,d,h))
            case 3: #Hexadecimal
                d = input("Introdueixi un número binari ")
                b = dectobin(d)
                o = dectooct(d)
                h = dectohex(d)
            case 4: #Hexadecimal to
                h = input("Introdueixi un número binari ")
                b = hextooct(b)
                o = hextodec(b)
                d = hextobin(b)
                print("El número binari {} és: \n oct -> {} dec -> {} \n hex -> {}".format(b,o,d,h))
            case 5: #Sortir
                print("Adeu, ja tornaras a la calculadora inicial \n\n")
                op=-1



#Programa principal
a = 1 
while a > 0: 
    a = menu_principal()
    match a: 
        case 1: 
            calculadora_enters()
        case 2: 
            calculadora_reals()
        case 3:
            canvi_de_base()
        case 4: 
            a = -1 
        case other:  
            print("Opció no vàlida!")



