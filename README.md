# Event Scraper – Fortaleza (Sympla)

Este projeto é um script em Python que coleta automaticamente eventos do site Sympla
a partir de uma cidade especificada, extraindo o título do evento e seu link.

O objetivo do projeto é explorar web scraping de forma prática, lidando com HTML real,
estruturas dinâmicas e problemas comuns de extração de dados.

## O que o projeto faz 

Atualmente, o script:

- Acessa a página de eventos do Sympla com base em uma cidade (ex: `sao-paulo-sp`)
- Identifica os cards de eventos na página
- Extrai o título do evento diretamente do HTML
- Extrai o link correspondente a cada evento
- Salva os dados coletados em um arquivo CSV
- Exibe no terminal a quantidade total de eventos coletados

## Tecnologias

- Python
- requests
- BeautifulSoup (bs4)

## Como executar

1. Clone o repositório
2. Instale as dependências:
pip install requests beautifulsoup4
3. Execute o script:
python sympla-scraper.py


## Decisões técnicas

A primeira versão do scraper dependia de classes CSS específicas para localizar os títulos
dos eventos. Essas classes se mostraram dinâmicas e instáveis.

A versão atual utiliza a hierarquia do HTML, buscando a tag <h3> dentro do escopo de
cada card de evento (a.sympla-card), tornando a extração mais robusta e menos dependente
de mudanças visuais no site.

Os resultados são armazenados em uma lista de dicionários, facilitando futuras extensões
como exportação para outros formatos (JSON, banco de dados, etc).

Versões iniciais e testes foram mantidos no diretório experiments/ para fins de estudo
e comparação da evolução do código.

## Limitações

-O script não lida com paginação (apenas a primeira página de eventos)
-Não há tratamento avançado de erros de rede ou bloqueios
-Depende da estrutura atual do site Sympla
-Não filtra eventos por categoria ou data

## Próximos passos

-Permitir que o usuário escolha a cidade via input() ou argumentos de linha de comando
-Implementar paginação para coletar mais eventos
-Exportar dados também em JSON
-Evitar eventos duplicados
-Adicionar logs e tratamento de erros
-Criar uma versão mais modular do scraper

## Aviso

Este projeto tem fins educacionais e de estudo de web scraping e da linguagem Python.
