#Vamos descobrir as músicas mais populares do Spotify nos últimos 10 anos! 

#Crie uma conta no Kaggle, uma das principais plataformas de ciência de dados e aprendizado de máquina. Em disciplinas avançadas vamos trabalhar com bases de dados provenientes de lá!

#Baixe o arquivo spotify-2023.csv no final da página que apresenta os dados.

#No Python, abra o arquivo para leitura e imprima as cinco primeiras linhas

#Para abrir o arquivo, defina o parâmetro encoding='latin-1'

#Após compreender a estrutura do arquivo (divisão em colunas, caracter separador de coluna, etc.) passamos para a etapa de extração de informações.

# spotify_top10.py
import csv
import os

arquivo = r"C:\Users\Kefersson\Documents\Desenvolve\Python\Modulo7\spotify-2023.csv"

resultado = {}
anos_desejados = list(range(2012, 2023))

with open(arquivo, "r", encoding="latin-1") as f:
    leitor = csv.reader(f)

    next(leitor)  # pular cabeçalho

    for linha in leitor:
        # ignorar linhas com campos entre aspas contendo vírgula
        if any('"' in campo for campo in linha):
            continue

        try:
            track = linha[0]
            artist = linha[1]
            artist_count = int(linha[2])
            ano = int(linha[3])
            streams = int(linha[8])
        except (ValueError, IndexError):
            continue  # linha inválida

        if ano not in anos_desejados:
            continue

        if ano not in resultado or streams > resultado[ano][3]:
            resultado[ano] = [track, artist, ano, streams]

lista_final = [resultado[ano] for ano in anos_desejados]
print(lista_final)
