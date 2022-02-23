from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def obtem_pagina_html(url):
    response = urlopen(url)
    html = response.read().decode('utf-8')
    return BeautifulSoup(html, 'html.parser')

def obtem_informacoes_anuncio(anuncio):
    card = {}
    # Valor
    card['value'] = anuncio.find('p', {'class': 'txt-value'}).getText()

    # Obtém todas as tags p que estão definidas dentro da div cujo atributo class=body-card. Essas tags p
    # contêm as informações sobre o veículo.
    infos = anuncio.find('div', {'class': 'body-card'}).findAll('p')
    for info in infos:
        # Cria o dicionário com os dados do veículo utilizando as próprias tags html e seus valores.
        card[info.get('class')[0].split('-')[-1]] = info.get_text()
    # Obtendo a lista dos acessórios de um veículo
    items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
    items.pop()
    acessorios = []
    for item in items:
        acessorios.append(item.getText().replace('► ', ''))
    card['acessorios'] = acessorios

    # Obtendo a imagem do anúncio
    image = anuncio.find('div', {'class': 'image-card'}).img
    image.get('src')

    urlretrieve(image.get('src'), '../img/' + image.get('src').split('/')[-1])

    return card

cards = []
# Obtendo informações de quantas paǵinas no total existem
url_principal = 'https://alura-site-scraping.herokuapp.com/index.php'
soup = obtem_pagina_html(url_principal)
# Na página principal, recupera a tag que define quantas páginas existem no total.
info_paginas = soup.find('span',class_='info-pages').getText().split()
# Gera o número de página inicial e final
num_pagina_inicial = int(info_paginas[1])
num_pagina_final = int(info_paginas[-1])

# Cria a url de cada uma das páginas, lê o conteúdo html e extrai as informações necessárias.
for pagina in range(num_pagina_inicial,num_pagina_final+1):
    url = 'https://alura-site-scraping.herokuapp.com/index.php?page=' + str(pagina)
    soup = obtem_pagina_html(url)
    # Recupera os anúncios da página em questão.
    anuncios = soup.find('div', {"id": "container-cards"}).findAll('div', class_="card")
    for anuncio in anuncios:
        card = obtem_informacoes_anuncio(anuncio)
        cards.append(card)

# Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)
dataset.to_csv('../data/anuncios.csv', sep=';', index = False, encoding = 'utf-8-sig')

print(f'Foram criados {len(cards)} cards')