#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

# Solicita a distância e o peso ao usuário
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

# Define o valor base por kg de acordo com a distância
if distancia <= 100:
    valor_por_kg = 1.00
elif distancia <= 300:
    valor_por_kg = 1.50
else:
    valor_por_kg = 2.00

# Calcula o valor do frete
valor_frete = peso * valor_por_kg

# Adiciona taxa extra se o peso for superior a 10 kg
if peso > 10:
    valor_frete += 10.00

print(f"O valor do frete é: R${valor_frete:.2f}")
