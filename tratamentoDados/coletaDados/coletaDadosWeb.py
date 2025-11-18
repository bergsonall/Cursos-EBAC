import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/games'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#Extrai e exibi o texto na tag H2
for i in extracao.find_all('h2'):
    titulo = i.text.strip()
    print(f'Titulo: {titulo}')


#Exibi quantos h2 e quantos p
print(len(extracao.find_all('h2')))
print(len(extracao.find_all('p')))


#Extrair o nome da tag
for i in extracao.find_all('p'):
    print(i.name)


#primeiro "for" le os "h2" dentro da variavel
for i in extracao.find_all('h2'):
    print(f'Titulo: {i.text.strip()}')

#segundo "for" le as proximas tag HTML selecionada dentro do mesmo container
    for link in i.find_next_siblings('p'):

#terceiro "for" le os "a"
        for a in link.find_all('a', href=True):
            print(f'Texto link: {a.text.strip()}  /  URL: {a["href"]}')