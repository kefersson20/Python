#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.

#Exemplo de interação:

#Adivinhe o número entre 1 e 10: 5

#Muito alto, tente novamente!

#Adivinhe o número entre 1 e 10: 3

#Correto! O número é 3.

import random

# gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# loop até o usuário acertar
while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    if palpite > numero_secreto:
        print("Muito alto, tente novamente!")
    elif palpite < numero_secreto:
        print("Muito baixo, tente novamente!")
    else:
        print(f"Correto! O número é {numero_secreto}.")
        break  # encerra o loop
