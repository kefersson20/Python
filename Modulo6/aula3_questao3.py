#Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

#Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]

#Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

import random

# Gera lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:", lista)

# Identifica o intervalo com mais números negativos
# Aqui vamos considerar intervalos de tamanho 3 (como exemplo)
tam_intervalo = 3
maior_qtd_negativos = -1
inicio_maior_intervalo = 0

for i in range(len(lista) - tam_intervalo + 1):
    intervalo = lista[i:i + tam_intervalo]
    qtd_negativos = sum(1 for n in intervalo if n < 0)
    if qtd_negativos > maior_qtd_negativos:
        maior_qtd_negativos = qtd_negativos
        inicio_maior_intervalo = i

# Remove o intervalo da lista original
del lista[inicio_maior_intervalo:inicio_maior_intervalo + tam_intervalo]

print("Lista editada:", lista)
