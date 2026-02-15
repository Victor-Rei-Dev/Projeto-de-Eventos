# Event Scraper – Fortaleza (Sympla)

Este projeto é um script em Python que coleta automaticamente eventos da cidade de Fortaleza
a partir do site Sympla, extraindo o título do evento e seu link.

O objetivo do projeto é explorar web scraping de forma prática, lidando com HTML real,
estruturas dinâmicas e problemas comuns de extração de dados.

## O que o projeto faz

Atualmente, o script:

- Acessa a página de eventos de Fortaleza no Sympla
- Identifica os cards de eventos
- Extrai o título do evento diretamente do conteúdo HTML
- Exibe no terminal o nome do evento e seu respectivo link

## Tecnologias

- Python
- requests
- BeautifulSoup (bs4)

## Como executar

1. Clone o repositório
2. Instale as dependências:
pip install requests beautifulsoup4
3. Execute o script:
python scraper.py


## Decisões técnicas

A primeira versão do scraper dependia de classes CSS específicas para localizar os títulos
dos eventos. Essas classes se mostraram dinâmicas e instáveis.

A versão atual utiliza a hierarquia do HTML, buscando a tag `<h3>` dentro do escopo de cada
card de evento, tornando a extração mais robusta e menos dependente de mudanças visuais no site.

A versão inicial foi mantida no diretório `experiments/` apenas para fins de comparação
e estudo da evolução do código.

## Limitações

- O script não filtra eventos por categoria
- Não há persistência dos dados (os resultados são apenas exibidos no terminal ou vs code)
- Depende da estrutura atual do site Sympla

## Próximos passos

- Filtrar eventos por palavras-chave
- Salvar os eventos coletados em arquivo (txt ou json)
- Evitar exibição de eventos duplicados

