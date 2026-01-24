def abc():
    return 'abc123'

def teste_yield():
    yield 1
    yield 2
    yield abc()

teste = teste_yield()
print(next(teste))
print(next(teste))
print(next(teste))