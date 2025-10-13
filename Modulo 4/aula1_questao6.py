#Exercício de maratona:  https://www.beecrowd.com.br/judge/pt/problems/view/1094

#Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 

#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).

#Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas

# Leitura da quantidade de experimentos
N = int(input())

# Inicializa contadores
total_coelhos = 0
total_ratos = 0
total_sapos = 0

# Processa cada experimento
for i in range(N):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]

    if tipo == 'C':
        total_coelhos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'S':
        total_sapos += quantia

# Total geral de cobaias
total = total_coelhos + total_ratos + total_sapos

# Calcula percentuais
percent_coelhos = (total_coelhos / total) * 100
percent_ratos = (total_ratos / total) * 100
percent_sapos = (total_sapos / total) * 100

# Imprime os resultados
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percent_coelhos:.2f} %")
print(f"Percentual de ratos: {percent_ratos:.2f} %")
print(f"Percentual de sapos: {percent_sapos:.2f} %")
