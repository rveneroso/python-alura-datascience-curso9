from urllib.request import urlopen

def trata_html(html_original):
    # Convertendo o tipo bytes para string
    html_tratado = html_original.decode('utf-8')
    # Eliminando os caracteres de tabulação, mudança de linha etc.
    html_tratado = " ".join(html_tratado.split()).replace("> <", "><")
    return html_tratado

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read() # Esse objeto é do tipo bytes.

html_tratado = trata_html(html)
print(html_tratado)

