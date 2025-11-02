#Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:

#A lista elementos

#A soma dos valores da lista

#A média dos valores da lista


import random

# Gera aleatoriamente um número entre 5 e 20
num_elementos = random.randint(5, 20)

# Gera uma lista com 'num_elementos' valores entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcula a soma e a média dos valores da lista
soma = sum(elementos)
media = soma / num_elementos

# Exibe os resultados
print("Quantidade de elementos:", num_elementos)
print("Lista de elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", media)
