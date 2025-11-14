#Vamos fazer o jogo da forca! Antes de programar: 

#Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.

#Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.

#Escreva um programa em Python para executar o jogo, de acordo com as definições:

#Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;

#Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;

#No início exiba o número de letras na palavra como underscores;

#Permita que o jogador insira letras para adivinhar a palavra;

#Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;

#Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;

#Limite o número de tentativas para 6 (as partes do enforcado).

import random

# ---------------------------------------------
# Função para imprimir o estágio do enforcado
# ---------------------------------------------
def imprime_enforcado(erros, enforcados):
    print(enforcados[erros])


# ---------------------------------------------
# Carregar palavras do arquivo "gabarito_forca.txt"
# ---------------------------------------------
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip().lower() for linha in f.readlines() if linha.strip()]

# Escolher uma palavra aleatória
palavra = random.choice(palavras)
progresso = ["_" for _ in palavra]
erros = 0


# ---------------------------------------------
# Carregar estágios do enforcado
# ---------------------------------------------
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    conteudo = f.read().strip()

# Cada estágio é separado por linhas em branco → split("\n\n")
enforcados = [est.strip() for est in conteudo.split("\n\n")]


# ---------------------------------------------
# Início do jogo
# ---------------------------------------------
print("\n=== JOGO DA FORCA ===")
print("A palavra tem", len(palavra), "letras.")
print(" ".join(progresso))

while erros < 6 and "_" in progresso:
    letra = input("\nDigite uma letra: ").lower().strip()

    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra!")
        continue

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                progresso[i] = letra
        print("Boa! Progresso:", " ".join(progresso))

    else:
        erros += 1
        print("\nLetra incorreta!")
        imprime_enforcado(erros, enforcados)
        print("Erros:", erros)

# ---------------------------------------------
# Fim do jogo
# ---------------------------------------------
if "_" not in progresso:
    print("\n🎉 Parabéns! Você venceu!")
else:
    print("\n💀 Você perdeu! A palavra era:", palavra)
