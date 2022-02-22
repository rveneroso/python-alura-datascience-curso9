from bs4 import BeautifulSoup
import util

url = 'https://alura-site-scraping.herokuapp.com/index.php'
html = util.obtem_html(url)
soup = BeautifulSoup(html, "html.parser") # Objeto do tipo <class 'bs4.BeautifulSoup'>

# Acessando a tag html de um documento
print(soup.html)

# Acessando a tag head de um documento
print(soup.head)

# Acessando a tag title de um documento
print(soup.head.title)
# Outra forma é acessar diretamente a tag title mas isso só vale quando só há uma tag do tipo no documento.
print(soup.title)

# Navegando pela árvore de tags div até chegar na tag h5.
print(soup.body.div.div.div.div.h5)

# Pegando apenas o valor da tag
print(soup.body.div.div.div.div.h5.get_text())
# Ou ainda
print(soup.body.h5.getText())
# Acessando a tag body de um documento
print(soup.body)
# Obtendo somente o texto (ignorando as tags) do documento html completo
print(soup.get_text())

# Acessando atributos de uma tag
print(soup.img.attrs) # Imprime um dicionário do tipo
                      # {'src': 'img/alura-logo.svg', 'class': ['d-inline-block', 'align-top'], 'alt': 'Alura'}
# Obtendo somente as chaves dos atributos de uma tag
print(soup.img.attrs.keys()) # Retorna um dicionário no estilo dict_keys(['src', 'class', 'alt'])
# Obtendo somente os valores dos atributos de uma tag
print(soup.img.attrs.values())
# Para acessar o atributo src de uma tag img:
print(soup.img.get('src'))
