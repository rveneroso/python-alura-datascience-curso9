from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
# Lista que conterá os cards
cards = []
# Dicionário que representa um veículo à venda no site da Alura Motors
card = {}
# Recupera o primeiro anúncio da página
anuncio = soup.find('div', {'class': 'well card'})

# Obtendo o valor dentro do anúncio. Como a class txt-value só existe no elemento que representa o valor do
# veículo, então podemos ir diretamente à ele sem a necessidade de navegar os elementos parents.
valor = anuncio.find('p', {'class': 'txt-value'}).getText() # Retorna R$ 338.000

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
# Transformando o dicionário em um DataFrame
dataset = pd.DataFrame.from_dict(card, orient = 'index').T
# Salvando o DataFrame em um arquivo csv
dataset.to_csv('../data/anuncios.csv', index=False, sep=';', encoding='utf8')
# Obtendo a imagem do anúncio
image = anuncio.find('div', {'class': 'image-card'}).img
image.get('src')

urlretrieve(image.get('src'), '../img/' + image.get('src').split('/')[-1])