import argparse
import requests
import csv
import os
from bs4 import BeautifulSoup


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scraper de eventos do Sympla por cidade"
    )

    parser.add_argument(
        "cidade",
        help="Slug da cidade no Sympla (ex: sao-paulo-sp, fortaleza-ce)"
    )

    parser.add_argument(
        "--output",
        choices=["terminal", "csv"],
        default="terminal",
        help="Formato de saída dos dados (default: terminal)"
    )

    return parser.parse_args()


def scrape_sympla(cidade):
    url = f"https://www.sympla.com.br/eventos/{cidade}"
    response = requests.get(
        url,
        timeout=10,
        # O User Agent é uma espécie de "identificação" pro site: quem acessou o site nesse caso foi o sympla-scraper-v3
        headers={"User-Agent": "sympla-scraper-v3"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.select("a.sympla-card")

    eventos = []

    for card in cards:
        title_tag = card.find("h3")
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = card.get("href")

        eventos.append({
            "Título": title,
            " Link": link
        })

    return eventos

def print_terminal(eventos, cidade):
    print(f"[INFO] Cidade: {cidade}")
    print(f"[INFO] Eventos encontrados: {len(eventos)}\n")

    for evento in eventos:
        print(f"- {evento['Título']}")
        print(f"  {evento[' Link']}\n")

def salvar_csv(eventos,cidade):
    # Cria a pasta data. Se já existir, faz nada
    os.makedirs("data", exist_ok=True)
    caminho = f"data/eventos_{cidade}.csv"

    # O python e o csv fazem quebras de linhas automáticas. O newline = "" impede o python de quebrar linhas, deixando só o csv lidar com isso
    # O "w" permite escrever no arquivo. Se não existir, cria, e se já existir,sobrescreve
    with open(caminho, mode="w", newline="", encoding="utf-8-sig") as arquivo:
        # O DictWriter escreve dicionários. fieldnames define ordem das colunas e nomes do cabeçalho
        writer = csv.DictWriter(
            arquivo,
            fieldnames=["Título", " Link"]
        )
        # Escreve o cabeçalho
        writer.writeheader()
        #Escreve o dict eventos. Não é mais necessário o for
        writer.writerows(eventos)

    print(f"[INFO] CSV salvo em {caminho}")


def main():
    args = parse_args()
    eventos = scrape_sympla(args.cidade)

    if args.output == "terminal":
        print_terminal(eventos, args.cidade)

    elif args.output == "csv":
        salvar_csv(eventos, args.cidade)


if __name__ == "__main__":
    main()


           
