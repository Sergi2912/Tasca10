#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Joc del MasterMind versió reduïda

import random

# Elegim un codi de 4 xifres entre 0 i 9
codi="".join(list(map(lambda x: str(x), random.sample(range(0,9), 4))))
print (""" Això és el teu primer Mastermind
       	Has d'adivinar un número de 4 xifres diferents.
       	""")
latevaproposta = input("Introduexi un codi de 4 xifres: ")
# Fins que no ho adivinis, no surts del programa
intents = 0
while latevaproposta != codi:
	intents += 1
	encerts = 0
	coincidencies = 0
	#Verifiquem quants encerts hi ha hagut i quantes coincidències.
	for i in range(4):
            if latevaproposta[i] == codi[i]:
            	encerts += 1
            elif latevaproposta[i] in codi:
        	    coincidencies += 1
print ("La teva proposta (", latevaproposta, ") te", encerts, "encerts i", coincidencies, "coincidències.")
	# Solicitem un altre proposta
latevaproposta = input("Torna a introduir un codi de 4 xifres: ")
print ("Felicitats! Has endevinat el codi en ", intents, "intents.")

"""
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Joc del MasterMind versió reduïda

import random

# Elegim un codi de 4 xifres entre 0 i 9
codi = "".join(map(lambda x: str(x), random.sample(range(0, 10), 4)))
print("""
Això és el teu primer Mastermind
Has d'adivinar un número de 4 xifres diferents.
""")

# Fins que no ho adivinis, no surts del programa
intents = 0
while True:
    latevaproposta = input("Introduexi un codi de 4 xifres: ")
    # Comprovem si l'entrada és vàlida
    if not latevaproposta.isdigit() or len(latevaproposta) != 4 or len(set(latevaproposta)) != 4:
        print("Entrada no vàlida. Si us plau, introdueix un codi de 4 xifres diferents.")
        continue

    intents += 1
    encerts = 0
    coincidencies = 0

    # Verifiquem quants encerts hi ha hagut i quantes coincidències.
    for i in range(4):
        if latevaproposta[i] == codi[i]:
            encerts += 1
        elif latevaproposta[i] in codi:
            coincidencies += 1

    print("La teva proposta ({}) te {} encerts i {} coincidències.".format(latevaproposta, encerts, coincidencies))

    # Comprovem si l'usuari ha encertat el codi
"""   
