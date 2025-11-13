#Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 


def validar_cpf(cpf):
    # remove pontuação
    numeros = [int(d) for d in cpf if d.isdigit()]

    if len(numeros) != 11:
        return False

    # cálculo do primeiro dígito
    soma1 = sum([numeros[i] * (10 - i) for i in range(9)])
    resto1 = soma1 % 11
    dig1 = 0 if resto1 < 2 else 11 - resto1

    # cálculo do segundo dígito
    soma2 = sum([numeros[i] * (11 - i) for i in range(9)]) + dig1 * 2
    resto2 = soma2 % 11
    dig2 = 0 if resto2 < 2 else 11 - resto2

    # verifica se os dígitos conferem
    return numeros[9] == dig1 and numeros[10] == dig2


cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

if validar_cpf(cpf):
    print("Válido")
else:
    print("Inválido")
