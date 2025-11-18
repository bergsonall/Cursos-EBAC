import pandas as pd

df = pd.read_csv('C:/Users/Bruno/PycharmProjects/PythonProject/tratamentoDados/clientes.csv')

#Seta DataFrame displayWidth para None (sem limite)
pd.set_option('display.width', None)
print(df.head())

#Romove a coluna 'pais' e a linha de indice 2
df.drop('pais', axis=1, inplace=True)
df.drop(2, axis=0, inplace=True)
print(df.head())

#Normalizar campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()
print(df.head())

#Converter tipos de dados
df['idade'] = df['idade'].astype(int)

#Tratar valores nulos (NaN)
df_fillna = df.fillna(0) #Substituir valores nulos por 0
df_dropna = df.dropna() #Remover linhas com valores nulos
df_dropna4 = df.dropna(thresh=4) #Remover linhas com menos de 4 valores nao nulos
df = df.dropna(subset=['cpf']) #Remover linhas com valores nulos na coluna 'cpf'

print(f'Qtd de valores nulos \n{df.isnull().sum()}')
print(f'Qtd de registros nulos com fillna: {df_fillna.isnull().sum().sum()}')
print(f'Qtd de registros nulos com dropna: {df_dropna.isnull().sum().sum()}')
print(f'Qtd de registros nulos com drona4: {df_dropna4.isnull().sum().sum()}')
print(f'Qtd de registros nulos com CPF: {df.isnull().sum().sum()}')

#Substituir valores nulos na coluna 'estado' por 'Desconhecido'
df.fillna({'estado': 'Desconhecido'}, inplace=True)

#Substituir valores nulos na coluna 'endereco' por 'Endereco nao informado' 
df.fillna({'endereco': 'Endereco nao informado'}, inplace=True) 

#Cria nova coluna 'idade_corrigida' substituindo valores nulos pela media da coluna 'idade'
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

#Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') #Converter para datetime, valores invalidos vira NaT

print(f'Qtd de registros atual: {df.shape[0]}')
df.drop_duplicates(inplace=True) #Remover registros duplicados
df.drop_duplicates(subset=['cpf'], inplace=True) #Remover registros duplicados baseado na coluna 'cpf'
print(f'Qtd de registros removendo as duplicadas: {len(df)}')

print(f'Dados limpos: \n{df}')

#Atualiza colunas originais com as colunas corrigidas
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df.drop(['data_corrigida', 'idade_corrigida'], axis=1, inplace=True)
print(f'Dados finais: \n{df}')

df.to_csv('C:/Users/Bruno/PycharmProjects/PythonProject/tratamentoDados/clientes_limpos.csv', index=False)