#Crie um programa para gerenciar um estoque de produtos. O programa deve exibir um menu com as opções: adicionar produto, listar produtos, remover produto, atualizar quantidade de produto e sair do programa.
print('''
MENU
1 - Adicionar produtos
2 - Listar produtos
3 - Romever produto
4 - Atualizar quantidade
5 - SAIR
''')

#Utilize um dicionário para armazenar os produtos. Cada produto será uma chave no dicionário, e o valor será outro dicionário contendo duas chaves: "quantidade" (indicando a quantidade disponível) e "preço" (o preço do produto).
produtos = {'banana': {'5': 5.79}, 'pera': {'1': 5.79}, 'laranja': {'12': 5.79}, 'tangerina': {'7': 5.79}, 'melancia': {'3': 5.79}, 'abacate': {'2': 5.79}, 'abacaxi': {'8': 5.79}, }

#Ao selecionar "adicionar produto", o programa deve pedir o nome do produto, a quantidade e o preço.

#Adicione o produto ao dicionário com a quantidade e preço informados.

#Ao selecionar "listar produtos", exiba todos os produtos no formato:

#Nome do produto: Quantidade disponível - Preço

#Os produtos devem ser exibidos em ordem alfabética (use uma função lambda para ordenar os produtos).

#Ao selecionar "remover produto", peça o nome do produto a ser removido. Verifique se o produto existe no dicionário antes de removê-lo. Caso o produto não exista, exiba uma mensagem de erro.

#Ao selecionar "atualizar quantidade de produto", o programa deve pedir o nome do produto e a nova quantidade. Se o produto existir, a quantidade deve ser atualizada. Caso contrário, exiba uma mensagem de erro.

#O programa deve rodar em um loop até que o usuário escolha a opção de sair.

#Organize seu código utilizando funções. Cada funcionalidade do menu deve ser implementada como uma função separada, como por exemplo, uma função para adicionar produtos, outra para listar, etc.

#Utilize operadores condicionais e laços de repetição para manter o programa funcional e simples.

#Exemplo do menu exibido para o usuário:

#Adicionar produto

#Listar produtos

#Remover produto

#Atualizar quantidade de produto

#Sair

if __name__ == '__main__':
    main()