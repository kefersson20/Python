#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

#Digite uma frase: O rato roeu a roupa do rei

#Frase modificada: * r*t* r*** * r**p* d* r**


frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

nova_frase = "".join("*" if c in vogais else c for c in frase)
print("Frase modificada:", nova_frase)
