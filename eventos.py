import requests
from bs4 import BeautifulSoup

url = "https://www.sympla.com.br/eventos/fortaleza-ce"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for card in soup.select("a.sympla-card"):
    titulo_tag = card.find("h3")
    link = card.get("href")

    if titulo_tag and link:
        titulo = titulo_tag.get_text(strip=True)
        print(titulo)
        print(link)
        print()

