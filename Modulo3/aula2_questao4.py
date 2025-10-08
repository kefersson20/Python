#4 - Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se 4 - Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras: pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:

# Lê a classe do personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")

# Lê os pontos de força
forca = int(input("Digite os pontos de força (de 1 a 20): "))

# Lê os pontos de magia
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Inicializa a variável de validação como False
valido = False

# Verifica as condições para cada classe
if classe == "guerreiro":
    valido = (forca >= 15) and (magia <= 10)
elif classe == "mago":
    valido = (forca <= 10) and (magia >= 15)
elif classe == "arqueiro":
    valido = (forca > 5 and magia > 5) and (forca <= 15 and magia <= 15)

# Exibe o resultado final
print("Pontos de atributo consistentes com a classe escolhida:", valido)
