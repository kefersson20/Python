#Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.

#Digite uma frase: Bom dia, meu nome é Davi.

#Frase salva em /Users/laranjeira/python-basico/frase.txt


# salva_frase.py
frase = input("Digite uma frase: ")

with open("frase.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

import os
caminho = os.path.abspath("frase.txt")
print(f"Frase salva em {caminho}")
