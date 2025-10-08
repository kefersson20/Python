#3 - Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em laranja e as impressões de seu código em branco.

# Lê a idade do participante
idade = int(input("Digite sua idade: "))

# Lê se já jogou pelo menos 3 jogos de tabuleiro (True ou False)
jogou_tres = input("Já jogou pelo menos 3 jogos de tabuleiro? ") == "True"

# Lê a quantidade de vitórias
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica as condições: idade entre 16 e 18, jogou pelo menos 3 jogos e venceu pelo menos 1
apto = (idade >= 16 and idade <= 18) and jogou_tres and (vitorias >= 1)

# Exibe o resultado final
print("Apto para ingressar no clube de jogos de tabuleiro:", apto)
