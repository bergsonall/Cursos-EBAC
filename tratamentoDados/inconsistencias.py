import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('C:/Users/Bruno/PycharmProjects/PythonProject/tratamentoDados/clientes_remove_outliers.csv')

print(df.head())
print(df.head())

#Mascarar CPF, exibindo apenas os 3 primeiros e os 2 ultimos digitos
df['cpf_mascara'] = df['cpf'].apply(lambda x: f'{x[:3]}.***.***-{x[-2:]}')

#Corrigir datas usando errors='coerce' para valores invalidos virarem NaT
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')

#Ajustar idades baseando-se na data atual e na data de nascimento
data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -= ((data_atual.month < df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

print(df[['cpf', 'cpf_mascara', 'data', 'data_atualizada', 'idade', 'idade_ajustada']])

#Extrair informacoes do endereco
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Bairro nao informado')
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split('/')[-1].strip().upper() if len(x.split('/')) > 1 else 'Desconhecido')

print(df[['endereco', 'endereco_curto', 'bairro', 'estado_sigla']])


#Verificar a formatação do endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereco invalido' if len(x) > 50 & len(x) < 5 else x)

#Corrigir dados erroneos
df['cpf'] = df['cpf'].apply(lambda x: 'CPF invalido' if len(x) != 14 else x)

#Lista de estados brasileiros
estados_brasileiros = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

#Verifica se o estado cadastrado é existente 
df['estado_sigla'] = df['estado_sigla'].apply(lambda x: x if x in estados_brasileiros else 'Estado invalido')

print(f'Dados tratados:\n {df.head()}')

df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'bairro', 'estado']]
df_salvar.to_csv('C:/Users/Bruno/PycharmProjects/PythonProject/tratamentoDados/clientes_tratados.csv', index=False)

print(f'Novo DataFrame: \n {pd.read_csv('C:/Users/Bruno/PycharmProjects/PythonProject/tratamentoDados/clientes_tratados.csv')}')