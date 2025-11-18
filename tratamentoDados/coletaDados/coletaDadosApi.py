import requests


def enviar_arquivo():
    # Caminho arquivo
    caminho = r'C:\Users\Bruno\Downloads\produtos_informatica.xlsx'

    with open(caminho, 'rb') as file:
        requisicao = requests.post('https://tmpfiles.org/api/v1/upload', files={'file': file})

    print("Status:", requisicao.status_code)
    print("Resposta:", requisicao.text)

    if requisicao.ok:
        dados = requisicao.json()
        link = dados['data']['url']
        print(f'✅ Arquivo enviado com sucesso!\n🔗 Link: {link}')
    else:
        print("❌ Erro ao enviar arquivo.")


def receber_arquivo(file_url):
    # receber arquivo
    requisicao = requests.get(file_url)

    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso')
    else:
        print(f'Erro ao baixar o arquivo: {requisicao.json()}')


enviar_arquivo()
receber_arquivo('http://tmpfiles.org/4947004/produtos_informatica.xlsx')
