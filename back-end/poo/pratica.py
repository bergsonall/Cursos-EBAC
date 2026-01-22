class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emitiu um som genérico."
    
class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro latiu!"
    
class Gato(Animal):
    def emitir_som(self):
        return "O gato miou!"
    
cachorro = Cachorro('bob', 6)
print(cachorro.emitir_som())
gato = Gato('Billy', 3)
print(gato.emitir_som())