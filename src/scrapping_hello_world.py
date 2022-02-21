from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
# get_text retorna somente o texto do elemento propriamente dito, eliminando as tags HTML
print(soup.find('h1', id="hello-world").get_text())
print(soup.find('p').get_text())