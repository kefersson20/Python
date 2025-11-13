#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".

#Digite uma frase (digite "fim" para encerrar): Radar

#"Radar" é palíndromo

#Digite uma frase (digite "fim" para encerrar): Bom dia!

#"Bom dia!" não é palíndromo

#Digite uma frase (digite "fim" para encerrar): Ame o poema

#"Ame o poema" é palíndromo

#Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!

#"A Daniela ama a lei? Nada!" é palíndromo

#Digite uma frase (digite "fim" para encerrar): fim


import string

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break

    # Remove espaços e pontuação, e deixa tudo em minúsculo
    frase_limpa = "".join(c.lower() for c in frase if c.isalnum())

    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
