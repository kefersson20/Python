#5 - Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:

#A: Para mulheres, ter mais de 60 anos. Para homens, 65.

#B: Ou ter trabalhado pelo menos 30 anos

#C: Ou ter 60 anos  e trabalhado pelo menos 25.

# Lê o gênero da pessoa
genero = input("Digite seu gênero (M ou F): ")

# Lê a idade
idade = int(input("Digite sua idade: "))

# Lê o tempo de serviço
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Condição A: idade mínima (F > 60, M > 65)
condicao_idade = (genero == "F" and idade > 60) or (genero == "M" and idade > 65)

# Condição B: tempo de serviço de pelo menos 30 anos
condicao_tempo = tempo_servico >= 30

# Condição C: 60 anos de idade e pelo menos 25 de serviço
condicao_mista = idade >= 60 and tempo_servico >= 25

# Verifica se alguma das condições foi atendida
aposentadoria = condicao_idade or condicao_tempo or condicao_mista

# Exibe o resultado final
print(aposentadoria)
