# Lê a quantidade de elementos da primeira lista
qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {qtd1} elementos da lista 1:")
lista1 = [int(input()) for _ in range(qtd1)]

# Lê a quantidade de elementos da segunda lista
qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {qtd2} elementos da lista 2:")
lista2 = [int(input()) for _ in range(qtd2)]

# Cria a lista intercalada
lista_intercalada = []
menor_tamanho = min(qtd1, qtd2)

# Intercala os elementos até o final da menor lista
for i in range(menor_tamanho):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adiciona os elementos restantes da maior lista
if qtd1 > qtd2:
    lista_intercalada.extend(lista1[menor_tamanho:])
else:
    lista_intercalada.extend(lista2[menor_tamanho:])

# Exibe o resultado final
print("Lista intercalada:", *lista_intercalada)
