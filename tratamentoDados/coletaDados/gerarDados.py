import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

dados_pessoais = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    endereco = faker.street_address()
    estado = faker.state()
    pais = 'Brasil'

    pessoas = {
        'nome' : nome,
        'cpf' : cpf,
        'idade' : idade,
        'data' : data,
        'endereco' : endereco,
        'estado' : estado,
        'pais' : pais
    }

    dados_pessoais.append(pessoas)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

df_pessoas = pd.DataFrame(dados_pessoais)
print(df_pessoas)

df_pessoas.to_csv('clientes.csv')