class Usuario:
    def __init__(self, nome, email, telefone, genero):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.genero = genero

    def __str__(self):
        return f"{self.nome}  |  {self.email}  |  {self.telefone}  |  {self.genero}"
    

class Homem(Usuario):
    def mostraGenero(self):
        return f"{self.genero}"

pessoas = []
bruno = Usuario('bruno', 'bruno@abc.com', '51999999999', 'masculino')
pessoas.append(bruno)
carol = Usuario('carol', 'carol@abc.com', '51999999999', 'feminino')
pessoas.append(carol)
vinicius = Homem('vinicius', 'vinicius@abc.com', '51999999999', 'masculino')
pessoas.append(vinicius)

for pessoa in pessoas:
    print(pessoa)