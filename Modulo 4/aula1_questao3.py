#Transforme em código o fluxograma a seguir

# Leitura das 3 notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# Cálculo da média
m = (n1 + n2 + n3) / 3

# Verifica a situação do aluno
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

# Finaliza
print("Fim")
