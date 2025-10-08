#2 - Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 

#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

#86 graus Fahrenheit são 30 graus Celsius.

# Lê a temperatura em Fahrenheit
fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))

# Converte Fahrenheit para Celsius
celsius = int((fahrenheit - 32) * (5/9))

# Exibe o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")