#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores

#Digite a palavra objetivo: amor

#Anagramas: ["amor", "mora", "ramo", "Roma"] 


frase = input("Digite uma frase: ")
palavra = input("Digite a palavra objetivo: ")

# normaliza tudo em minúsculas
frase = frase.lower()
palavra = palavra.lower()

# ordena os caracteres da palavra objetivo
ordenada_objetivo = sorted(palavra)

# separa as palavras da frase
palavras = frase.split()

# encontra anagramas
anagramas = [p for p in palavras if sorted(p) == ordenada_objetivo]

print(f"Anagramas: {anagramas}")
