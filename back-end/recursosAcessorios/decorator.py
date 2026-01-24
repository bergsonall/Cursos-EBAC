def meu_decorator(func):
    def wrapper():
        print('antes')
        func()
        print('depois')
    return wrapper

@meu_decorator
def cheguei():
    print('Oi')

@meu_decorator
def saindo():
    print('Tchau')

cheguei()
saindo()