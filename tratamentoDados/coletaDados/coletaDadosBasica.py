import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define um cabeçalho de navegador real
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/118.0.0.0 Safari/537.36"
    )
}

print('resquests: ')
response = requests.get('https://br.investing.com/indices/bovespa-historical-data#', headers = headers)
print(response.text[:600])

print('BeautifulSoup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])


print('Pandas: ')
url_dados = pd.read_html(response.text)
print(url_dados[0].head(10))