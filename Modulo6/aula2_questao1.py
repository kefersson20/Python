#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:

#A lista ordenada, sem modificar a lista original

#A lista original

#O índice do maior valor da lista

#O índice do menor valor da lista

import random

# Gera 20 valores inteiros aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Cria uma cópia ordenada (sem modificar a lista original)
lista_ordenada = sorted(lista)

# Encontra os índices do maior e do menor valor
indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

# Exibe os resultados
print("Lista ordenada (sem modificar a original):", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor da lista:", indice_maior)
print("Índice do menor valor da lista:", indice_menor)
