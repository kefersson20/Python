#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:

#A lista original

#Os 3 primeiros elementos

#Os 2 últimos elementos

#A lista invertida (do fim para o começo)

#Os elementos de índice par (0, 2, 4 … )

#Os elementos de índice ímpar (1, 3, 5, … )

# Script que lê uma quantidade indefinida de números e exibe informações com fatiamento

numeros = []

print("Digite números inteiros (digite 'fim' para encerrar, mínimo de 4 valores):")

# Leitura dos números
while True:
    entrada = input("Número: ")
    if entrada.lower() == "fim":
        if len(numeros) < 4:
            print("⚠️ É preciso informar pelo menos 4 números antes de encerrar!")
            continue
        else:
            break
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

# Exibindo resultados
print("\n📋 Resultados:")
print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
