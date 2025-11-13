#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Dica: usando listas você não precisa fazer um "if" para cada mês.

#Digite uma data de nascimento: 29/10/1973

#Você nasceu em  29 de Outubro de 1973.


# Lista com os nomes dos meses (incluindo um espaço vazio no índice 0 para facilitar o mapeamento 1:Janeiro, 2:Fevereiro...)
meses = [
    "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Solicita a data de nascimento ao usuário
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Divide a string da data em dia, mês e ano
# Usamos split('/') para separar os elementos pelo caractere '/'
partes_data = data_nascimento.split('/')
dia = partes_data[0]
mes_numero = int(partes_data[1]) # Converte o mês para um número inteiro para usar como índice
ano = partes_data[2]

# Obtém o nome do mês a partir da lista usando o número como índice
nome_mes = meses[mes_numero]

# Imprime a data formatada
print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")
