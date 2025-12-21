#Crie um programa para gerenciar um estoque de produtos.

#Utilize um dicionário para armazenar os produtos. Cada produto será uma chave no dicionário, e o valor será outro dicionário contendo duas chaves: "quantidade" (indicando a quantidade disponível) e "preço" (o preço do produto).
produtos = {'banana': {'5': 5.79}, 'pera': {'1': 9.99}, 'laranja': {'12': 3.79}, 'tangerina': {'7': 2.79}, 'melancia': {'3': 7.79}, 'abacate': {'2': 12.79}, 'abacaxi': {'8': 6.79}}

#Ao selecionar "adicionar produto", o programa deve pedir o nome do produto, a quantidade e o preço.
#Adicione o produto ao dicionário com a quantidade e preço informados.
def adicionar_produto():
    while True:
        try:
            nome = input('Digite o nome do produto: ').strip()
            if nome in produtos:
                print('Produto ja pertence a esta lista')
                break
            else:
                quantidade = int(input('Digite a quantidade: '))
                preco = float(str(input('Digite o preço: ')).replace(',', '.'))
        except ValueError:
            print('\nDigite valores validos.')
        produtos[nome] = {quantidade : preco}
        return print('\nProduto adicionado com sucesso!')
    
#Ao selecionar "listar produtos", exiba todos os produtos no formato:
#Nome do produto: Quantidade disponível - Preço
#Os produtos devem ser exibidos em ordem alfabética (use uma função lambda para ordenar os produtos).

def listar_produtos():
    produtos_ordenados = dict(sorted(produtos.items()))
    for i, v in produtos_ordenados.items():
        for x, y in v.items():
            print(f'{i.title()} || Quantidade: {x} || Valor: {y}')


#Ao selecionar "remover produto", peça o nome do produto a ser removido. Verifique se o produto existe no dicionário antes de removê-lo. Caso o produto não exista, exiba uma mensagem de erro.
def remover_produto():
    nome = input('Digite o produto: ').strip()
    try:
        del produtos[nome]
        print('\nProduto removido!')
    except ValueError:
        print('\nProduto não esta na lista!!')

#Ao selecionar "atualizar quantidade de produto", o programa deve pedir o nome do produto e a nova quantidade. Se o produto existir, a quantidade deve ser atualizada. Caso contrário, exiba uma mensagem de erro.
def atualizar_quantidade():
    nome = input('Digite o produto: ').strip()
    if nome in produtos:
        quantidade = int(input('Digite a nova quantidade: '))
        att = produtos[nome].items()
        produtos[nome] = { quantidade : x for y, x in att}
        print("\nQuantidade atualizada!")
    else:
        print('\nProduto não encontrado!')

#O programa deve exibir um menu com as opções: adicionar produto, listar produtos, remover produto, atualizar quantidade de produto e sair do programa.
#O programa deve rodar em um loop até que o usuário escolha a opção de sair.

def main():
    while True:
        print('''
    MENU
    1 - Adicionar produtos
    2 - Listar produtos
    3 - Romever produto
    4 - Atualizar quantidade
    5 - SAIR
    ''')
        try:
            opt = int(input('Digite a opção a ser executada: '))
        except ValueError:
            print('Digite um valor valido')
        match opt:
            case 1:
                adicionar_produto()
            case 2:
                listar_produtos()
            case 3:
                remover_produto()
            case 4:
                atualizar_quantidade()
            case 5:
                break
            case _:
                print('\nOpção invalida.')

if __name__ == '__main__':
    main()