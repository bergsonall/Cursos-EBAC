lib = {}
loan = []

options = """
\n==============MENU==============
1 - Adicionar livro

2 - Listar livros

3 - Remover livro

4 - Atualizar quantidade de livros

5 - Registrar empréstimo

6 - Exibir histórico de empréstimos

0 - Sair\n"""

def adicionar_livros():
    nome = str(input("Digite o nome do livro: ")).strip().lower()

    if nome in lib:
        print('Este livro já possui registro.')
    else:
        qtd = int(input("Digite a quantidade de livros: "))
        autor = str(input("Digite o autor do Livro: "))
        lib[nome] = {'quantidade': qtd, 'autor': autor}
        print('Livro adicionado!')

def listar_livros():
    print(f"\n\n{'Livro':^30}  ||  {'Quantidade':^14}  ||  {'Autor':^20}")
    for c, v in lib.items():
        print(f"{c:^30}  ||  {v['quantidade']:^14}  ||  {v['autor']:^20}")

def remover_livro():
    nome = str(input("Digite o nome do livro: ")).strip().lower()
    if nome not in lib:
        print("Livro não encontrado.")
    else:
        del lib[nome]

def atualizar_quantidade():
    nome = str(input("Digite o nome do livro: ")).strip().lower()
    if nome not in lib:
        print("Livro não encontrado.")
    else:
        while True:
            try:
                qtd = int(input("Digite a nova quantidade do livro: "))
                if nome not in lib:
                    print("Livro não encontrado.")
                    break
                else:
                    lib[nome]['quantidade'] = qtd
                    break
            except:
                print('Valor inválido!')
            
def registrar_emprestimo():
    nome = str(input("Digite o nome do livro: ")).strip().lower()
    if nome not in lib:
        print("Livro não encontrado.")
    else:
        while True:
            try:
                qtd = int(input("Digite a quantidade do livro: "))
                if qtd <= lib[nome]['quantidade']:
                    loan.append([nome, qtd])
                    lib[nome]['quantidade'] -= qtd
                    break
                else:
                    print('Estoque insuficiente.')
                    break
            except:
                print('Valor inválido!')
                
def log_emprestimo():
    print(f"{'Livro':^30}  ||  {'Quantidade':^14}")
    for i in loan:
        print(f"{i[0]:^30}  ||  {i[1]:^14}")

while True:
    print(options)
    try:
        userChoice = int(input("\nEscolha uma opção: "))
    except:
        continue
    
    if userChoice == 1:
        adicionar_livros()
    elif userChoice == 2:
        listar_livros()
    elif userChoice == 3:
        remover_livro()
    elif userChoice == 4:
        atualizar_quantidade()
    elif userChoice == 5:
        registrar_emprestimo()
    elif userChoice == 6:
        log_emprestimo()
    elif userChoice == 0:
        print('\nSistema encerrado!')
        break
    else:
        continue