#Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
#Dica: use a biblioteca random.

#def embaralhar_palavras(frase):

    #### Escreva a função


# Exemplo de uso:

#frase = "Python é uma linguagem de programação"

#resultado = embaralhar_palavras(frase)

#print(resultado)

# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"


import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        if len(palavra) > 3:
            # separa o primeiro e último caractere
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = palavra[0] + "".join(meio) + palavra[-1]
        else:
            nova_palavra = palavra
        resultado.append(nova_palavra)

    return " ".join(resultado)


# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Exemplo possível: "Ptohyn é uma lignaugem de prarmoagãço"
