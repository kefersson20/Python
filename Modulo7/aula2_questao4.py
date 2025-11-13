#Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:

#Pelo menos 8 caracteres de comprimento.

#Contém pelo menos uma letra maiúscula e uma letra minúscula.

#Contém pelo menos um número.

#Contém pelo menos um caractere especial (por exemplo, @, #, $).

import string

def validador_senha(senha):
    # Critérios de validação
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(c in string.punctuation for c in senha)
    tamanho_ok = len(senha) >= 8

    return all([tem_maiuscula, tem_minuscula, tem_numero, tem_especial, tamanho_ok])


# Exemplos de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # True
print(validador_senha(senha2))  # False
print(validador_senha(senha3))  # False
