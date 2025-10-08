#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:

#Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)

#A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).




#Entrada

#Saída

#Digite o nome do produto 1:calça

#Digite o preço unitário do produto 1:199.90

#Digite a quantidade do produto 1: 3

#Digite o nome do produto 2:camisa

#Digite o preço unitário do produto 2:49.95

#Digite a quantidade do produto 2:10

#Digite o nome do produto 3:cinto

#Digite o preço unitário do produto 3:25

#Digite a quantidade do produto 3:3

#Total: R$1,174.20

# Lê os dados do primeiro produto
nome1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o preço unitário do produto 1:"))
qtd1 = int(input("Digite a quantidade do produto 1: "))

# Lê os dados do segundo produto
nome2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o preço unitário do produto 2:"))
qtd2 = int(input("Digite a quantidade do produto 2: "))

# Lê os dados do terceiro produto
nome3 = input("Digite o nome do produto 3:")
preco3 = float(input("Digite o preço unitário do produto 3:"))
qtd3 = int(input("Digite a quantidade do produto 3: "))

# Calcula o preço total da compra
total = (preco1 * qtd1) + (preco2 * qtd2) + (preco3 * qtd3)

# Exibe o resultado com separador de milhar e duas casas decimais
print(f"Total: R${total:,.2f}")
