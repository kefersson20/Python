#A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.


# livros_csv.py
livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    # adicione seus 10+ livros aqui
]

with open("meus_livros.csv", "w", encoding="utf-8") as arq:
    arq.write("Título,Autor,Ano de publicação,Número de páginas\n")

    for titulo, autor, ano, pags in livros:
        arq.write(f"{titulo},{autor},{ano},{pags}\n")
