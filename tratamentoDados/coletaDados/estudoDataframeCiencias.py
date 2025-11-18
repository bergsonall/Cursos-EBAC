import pandas as pd

# Lista
lista_nomes = ['Ana', 'Marcos', 'Carlos']
print(lista_nomes)
print(lista_nomes[0])

# Dicionario
dicionario_pessoa = {
    'nome': 'Bruno',
    'idade': 23,
    'cidade': 'Porto Alegre'
}
print(dicionario_pessoa)
print(dicionario_pessoa.get('nome'))

# Lista de dicionarios
dados = [
    {'nome': 'Ana', 'idade': 20, 'cidade': 'Sao Paulo'},
    {'nome': 'Marcos', 'idade': 25, 'cidade': 'Rio de janeiro'},
    {'nome': 'Carlos', 'idade': 30, 'cidade': 'Porto Alegre'}
]

# Transforma em dados tabulares
df = pd.DataFrame(dados)
print(df['nome'], '\n')

print(df['nome'], '\n')

print(df[['nome', 'idade']], '\n')

print(df.iloc[0])

# Adiciona uma nova coluna
df['salario'] = [4100, 3600, 5200]

# Adiciona um novo registro
df.loc[len(df)] = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'Taubaté',
    'salario': 4800
}

print(df)

#Romome uma coluna
df.drop('salario', axis=1, inplace=True)

#Filtro de dados
filtro_idade = df[df['idade'] >= 30]
print(filtro_idade)

#Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)

#Lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados.csv')
print('Leitura do CSV', df_lido)