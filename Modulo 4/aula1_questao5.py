#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.

#(idade1 + idade2 + idade3 + … + idade_n)/N


# Leitura da quantidade de respondentes
N = int(input("Digite a quantidade de respondentes: "))

# Inicializa a soma
soma = 0

# Loop para ler as idades
for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i+1}: "))
    soma += idade  # soma = soma + idade

# Calcula a média
media = soma / N

# Exibe a média das idades
print("A média das idades é:", media)
