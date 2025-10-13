#Transforme em código o fluxograma a seguir

# Leitura da quantidade de números
n = int(input("Digite a quantidade de números: "))

# Inicializa a variável maior
maior = 0

# Enquanto ainda houver números para ler
while n > 0:
    x = float(input("Digite um número: "))

    # Verifica se o número atual é maior que o maior armazenado
    if x > maior:
        maior = x

    # Decrementa o contador
    n = n - 1

# Exibe o maior número encontrado
print("O maior número é:", maior)
