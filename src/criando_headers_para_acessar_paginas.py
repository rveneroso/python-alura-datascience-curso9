from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# Ao tentar acessar a página da Alura, ocorre o Forbidden devido à ausência do header User-Agent.
# Então esse header deve ser criado e passado na requisição.
url = 'https://www.alura.com.br'
# Cria o header como um dicionário.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

# Cria a requisição passando a URL e o header criado acima. Idealmente a requisição deve ser feita em um bloco
# try / except. Nota: o HTTPError deve aparecer primeiro porque, se o URLError vier antes, ele irá capturar o erro
# de ausência do header User-Agent (ou outros erros que podem aparecer) e não será possível exibir o status do
# erro.
try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    print(response.read())
except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)