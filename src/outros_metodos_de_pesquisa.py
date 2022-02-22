from bs4 import BeautifulSoup
import util

html = open('../data/pagina_para_teste.html')
soup = BeautifulSoup(html, "html.parser")

# Localizando a primeira tag h2
# print(soup.find('h2'))

# Localizando a tag div que é pai da primeira tag h2. Observar que no comando abaixo, o print irá retornar
# TODO o conteúdo da div
# print(soup.find('h2').findParent('div'))

# Obtendo todos os parents da tag h2. Observar que as tags estarão numa ordem específica dentro do objeto
# retornado.
# print(soup.find('h2').findParents())

# Não é possível realizar uma pesquisa do tipo findParent em cima de um resultado no caso em que esse resultado
# é composto de mais de uma tag. A linha abaixo resulta em erro:
# print(soup.findAll('h2').findParent('div'))

# Uma solução para o problema acima é iterar sobre cada item do primeiro resultado e executar a pesquisa do
# parent individualmente.
# for item in soup.findAll('h2'):
#    print(item.find_parent('div')) # Observar que nesse caso o método é find_parent e não findParent

# São considerados siblings elementos que se encontram no mesmo nível dentro da hierarquia de um documento html.
# Encontra o próximo 'irmão' do primeiro elemento h2
#print(soup.find('h2').findNextSibling()) # Resulta em <p>Texto de conteúdo A</p>
# Encontra o irmão anterior do primeiro elemento h2
#print(soup.find('h2').findPreviousSibling()) # Resulta em <h1>Título A</h1>
# Encontrando todos os irmãos anteriores do primeiro elemento p
#print(soup.find('p').findPreviousSiblings()) # Resulta em [<h2 class="ref-a">Sub título A</h2>, <h1>Título A</h1>]
# Encontra todos os elementos seguintes ao primeiro elemento h2
#print(soup.find('h2').findAllNext())
'''
Imprime:
[<p>Texto de conteúdo A</p>, <div id="container-b">
<h1>Título B</h1>
<h2 class="ref-b">Sub título B</h2>
<p>Texto de conteúdo B</p>
</div>, <h1>Título B</h1>, <h2 class="ref-b">Sub título B</h2>, <p>Texto de conteúdo B</p>]
'''
# Encontra todos os elementos anteriores ao primeiro elemento h2
print(soup.find('h2').findAllPrevious())
'''

Imprime:
[<h1>Título A</h1>, <div id="container-a">
<h1>Título A</h1>
<h2 class="ref-a">Sub título A</h2>
<p>Texto de conteúdo A</p>
</div>, <body>
<div id="container-a">
<h1>Título A</h1>
<h2 class="ref-a">Sub título A</h2>
<p>Texto de conteúdo A</p>
</div>
<div id="container-b">
<h1>Título B</h1>
<h2 class="ref-b">Sub título B</h2>
<p>Texto de conteúdo B</p>
</div>
</body>, <html>
<body>
<div id="container-a">
<h1>Título A</h1>
<h2 class="ref-a">Sub título A</h2>
<p>Texto de conteúdo A</p>
</div>
<div id="container-b">
<h1>Título B</h1>
<h2 class="ref-b">Sub título B</h2>
<p>Texto de conteúdo B</p>
</div>
</body>
</html>]

'''