#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

#Chave de criptografia: gere um valor n aleatório entre 1 e 10

#Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

#nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

#chave_aleatoria = 5

#nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']

import random

def encrypt(nomes):
    """
    Criptografa uma lista de strings usando a cifra de César com uma chave aleatória.

    Args:
        nomes: Uma lista de strings a serem criptografadas.

    Returns:
        Uma tupla contendo a lista de nomes criptografados e a chave (n) utilizada.
    """
    # 1. Gerar um valor n aleatório entre 1 e 10 (inclusive).
    n = random.randint(1, 10)
    
    nomes_criptografados = []
    
    # Definir o intervalo de caracteres visíveis.
    UNICODE_START = 33
    UNICODE_END = 126
    RANGE_SIZE = UNICODE_END - UNICODE_START + 1

    for nome in nomes:
        nome_criptografado = ""
        for char in nome:
            # Obter o valor Unicode do caractere.
            char_val = ord(char)
            
            # Verificar se o caractere está no intervalo permitido.
            if UNICODE_START <= char_val <= UNICODE_END:
                # Aplicar o deslocamento (c + n) e garantir que ele permaneça no intervalo 
                # usando a operação de módulo para "ciclar" os caracteres.
                # Primeiro, normaliza o valor para o intervalo [0, RANGE_SIZE - 1].
                normalized_val = char_val - UNICODE_START
                # Aplica o shift e o módulo.
                shifted_val = (normalized_val + n) % RANGE_SIZE
                # Converte de volta para o valor Unicode original do intervalo.
                new_char_val = shifted_val + UNICODE_START
                # Converte o novo valor Unicode de volta para caractere.
                new_char = chr(new_char_val)
            else:
                # Se o caractere estiver fora do intervalo visível, ele não é alterado.
                new_char = char
            
            nome_criptografado += new_char
        nomes_criptografados.append(nome_criptografado)
        
    # Retorna a lista de nomes criptografados e a chave.
    return nomes_criptografados, n

# Exemplo de uso:
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print(f"Chave de criptografia gerada: {chave_aleatoria}")
print(f"Nomes originais: {nomes}")
print(f"Nomes criptografados: {nomes_cript}")
