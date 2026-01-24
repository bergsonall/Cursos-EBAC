opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]

menu = "\n".join([f"{i+1} - {op}" for i, op in enumerate(opcoes)])

soma = lambda x, y: x+y
sub = lambda x, y: x-y
mult = lambda x, y: x*y
div = lambda x, y: x/y

rodando = True

def calc(rodando):
    while rodando:
        continua = ''
        num1 = float(input("Insira o primeiro número:"))
        num2 = float(input("Insira o segundo número:"))
        print(f"Escolha uma operação: \n{menu}")
        try:
            operacao = int(input('Digite o numero da operação escolhida: '))
        except:
            print('Por favor, digite uma opção valida!')
        if operacao == 1:
            print(soma(num1, num2))
        elif operacao == 2:
            print(sub(num1, num2))
        elif operacao == 3:
            print(mult(num1, num2))
        elif operacao == 4:
            while num2 == 0:
                print('Divisão por zero não é permitida. Por favor, insira outro número: 2')
                num2 = float(input("Insira o segundo número:"))
            print(div(num1, num2))
        while continua != 'y' and continua != 'n':
            continua = input('Deseja realizar outra operação? [y/n]')
            if continua == 'n':
                rodando = False
try:
    calc(rodando)
except ValueError:
    print('Valor inválido, por favor digite um número.')
    calc(rodando)