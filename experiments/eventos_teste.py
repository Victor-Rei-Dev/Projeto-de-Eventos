import requests
from bs4 import BeautifulSoup

url = "https://www.sympla.com.br/eventos/fortaleza-ce"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify()[:1000])
print("evento" in html)
print("workshop" in html)
print("curso" in html)

for card in soup.select("a.sympla-card"):
   titulo = card.select_one("h3.pn67h1f")
   link = card.get("href")
   if titulo and link:
       print(titulo.get_text(strip=True))
       print(link)
       print()
