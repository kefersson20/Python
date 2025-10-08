#1 - Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário.

# Lê a idade de Juliana
idade_juliana = int(input("Digite a idade de Juliana: "))

# Lê a idade de Cris
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se ambas são maiores de idade (maiores de 17 anos)
pode_entrar = idade_juliana > 17 and idade_cris > 17

# Exibe True ou False conforme a condição
print(pode_entrar)
17