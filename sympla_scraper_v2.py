import argparse
import requests
from bs4 import BeautifulSoup


def parse_args():
    # Cria um objeto parser. O description aparece no -help do cmd
    parser = argparse.ArgumentParser(
        description="Scraper de eventos do Sympla por cidade"
    )

    # Adiciona o primeiro argumento. O nome da variável dele é cidade, e mesma coisa, o help aparece no -help do cmd
    parser.add_argument(
        "cidade",
        help="Slug da cidade no Sympla (ex: sao-paulo-sp, fortaleza-ce)"
    )
    # Adiciona o segundo argumento. O nome da variável dele é categoria, porém ele está limitado aos valores dos choices. Isso será útil futuramente.
    parser.add_argument(
        "--categoria",
        choices=["eventos", "shows", "teatro", "festivais"],
        default="eventos",
        help="Categoria de eventos (default: eventos)"
    )
    # Retorna um objeto do tipo Namespace
    return parser.parse_args()


def scrape_sympla(cidade, categoria):
    url = f"https://www.sympla.com.br/eventos/{cidade}"

    print(f"[INFO] Cidade: {cidade}")
    print(f"[INFO] Categoria: {categoria}")
    print(f"[INFO] URL: {url}")
    
    response = requests.get(url)
    #Essa linha verifica se a resposta HTTP for um erro (4xx ou 5xx), e se for, ela para o programa levantando uma exceção.
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.select("a.sympla-card")

    print(f"[INFO] Eventos encontrados: {len(cards)}")

    for card in cards:
        title_tag = card.find("h3") 
        # Se não houver h3 (title_tag == None), pula para o próximo card
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = card.get("href")

        print(f"- {title}")
        print(f"  {link}")


def main():
    args = parse_args()
    scrape_sympla(args.cidade, args.categoria)

# esse if _name_ == valor, só executa isso se este arquivo for o programa principal, e não uma biblioteca importada
if __name__ == "__main__":
    main()
