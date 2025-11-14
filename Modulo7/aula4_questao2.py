#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

#Bom

#dia

#meu

#nome

#é

#Davi


import re

# 1. Ler o conteúdo do arquivo frase.txt
with open("frase.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# 2. Remover caracteres não alfabéticos, exceto espaços (para separar palavras)
texto_limpo = re.sub(r'[^A-Za-zÀ-ÖØ-öø-ÿ ]+', '', texto)

# 3. Separar em palavras
palavras = texto_limpo.split()

# 4. Salvar cada palavra em uma linha no arquivo palavras.txt
with open("palavras.txt", "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")

# 5. Ler e imprimir o conteúdo de palavras.txt
with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())
