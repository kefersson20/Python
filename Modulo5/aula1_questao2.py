#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n

#Biblioteca random: Função randint()

#Biblioteca math:  Função sqrt()

import random   # biblioteca para gerar números aleatórios
import math     # biblioteca para cálculos matemáticos

# solicita o valor de n ao usuário
n = int(input("Digite a quantidade de valores inteiros que deseja gerar: "))

# inicializa a soma
soma = 0

# gera n valores aleatórios entre 0 e 100 e soma todos
for i in range(n):
    valor = random.randint(0, 100)  # gera um número aleatório inteiro entre 0 e 100
    soma += valor
    print(f"Valor gerado {i+1}: {valor}")

# calcula a raiz quadrada da soma
raiz = math.sqrt(soma)

# exibe o resultado
print(f"\nA soma dos valores é: {soma}")
print(f"A raiz quadrada da soma é: {raiz:.2f}")


