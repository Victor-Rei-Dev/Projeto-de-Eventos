import requests
from bs4 import BeautifulSoup
import csv

def coletar_eventos_sympla(cidade):
    url = f"https://www.sympla.com.br/eventos/{cidade}"
    response = requests.get(url)
    #o soup basicamente "fragmenta" o código html em espaços navegáveis
    soup = BeautifulSoup(response.text, "html.parser")

    eventos = []
    # esse for procura a classe .sympla-card, dentro de um <a>
    for card in soup.select("a.sympla-card"):
        titulo_tag = card.find("h3")
        #o get() obtém o valor do href em string
        link = " " + card.get("href")

        #se o titulo_tag e o link tiverem valores diferentes de None, o if é executado
        if titulo_tag and link:
           # extrai o texto do h3 removendo espaços em branco nas extremidades
            titulo = titulo_tag.get_text(strip=True)
            #eventos se torna uma lista de dicionários
            eventos.append({
                "titulo": titulo,
                "link": link
                            })
    return eventos

eventos = coletar_eventos_sympla("fortaleza-ce")
# salva em CSV. o w quer dizer que podemos escrever no documento, o enconding é o tipo de "notação"
with open("eventos.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
    #define que o writer irá escrever na variável arquivo
    writer = csv.writer(arquivo)
    #transforma a linha em um lista. cada bloco dessa linha corresponde a uma posição na lista.
    writer.writerow(["Título", " Link"])

    for evento in eventos:
        writer.writerow([evento["titulo"], evento["link"]])

# conta todos elementos de eventos
print(f"{len(eventos)} eventos salvos em eventos.csv")
