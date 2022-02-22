from bs4 import BeautifulSoup
import util

url = 'https://alura-site-scraping.herokuapp.com/index.php'
html = util.obtem_html(url)
soup = BeautifulSoup(html, "html.parser") # Objeto do tipo <class 'bs4.BeautifulSoup'>

# Pesquisando a tag img com o método find
#print(soup.find('img')) # É o mesmo que soup.img

# O método findAll retorna um objeto do tipo bs4.element.ResultSet. É possível limitar o resultado da busca
# passando um segundo parãmetro chamado limit.
tags_img = soup.findAll('img')
# Outra forma de se obter o mesmo resultado acima é:
tags_img = soup('img')
#print(tags_img)
# Com findAll é possível obter a lista de diferentes tags numa única operação
headers = soup.findAll(['h1', 'h2', 'h3','h4','h5'])
#print(headers)

# Pesquisando atributos específicos de uma tag.
# Nesse exemplo são pesquisadas todas as tags p do documento html e para cada um deles será recuperado o atributo
# txt-value.
# print(soup.findAll('p', {'class' : 'txt-value'}))

# Para recuperar todas as tags p que contenham 'Belo Horizonte - MG' em seu texto
# print(soup.findAll('p', text = 'Belo Horizonte - MG'))

# Utilizando diretamente os atributos de uma tag na pesquisa
# print(soup.findAll('img', alt = "Foto"))
# É possível iterar sobre um resultado dessa natureza e obter para cada elemento da lista outros atributos.
for item in soup.findAll('img', alt = "Foto"):
    pass
    # Imprime o endereço da imagem
    # print(item.get('src'))

# Cuidodo ao se pesquisar utilizando o atributo class: como class é uma palavra reservada do Python, para se
# realizar uma pesquisa com findAll baseado no valor do atributo class, é preciso utilizar a seguinte sintaxe:
# print(soup.findAll('p', class_="txt-value"))

# Para se obter uma lista com todos os textos encontrados dentro das tags de um documento html:
print(soup.findAll(text=True))