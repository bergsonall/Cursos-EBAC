import pandas as pd

df = pd.read_csv('C:/Users/Bruno/PycharmProjects/PythonProject/tratamentoDados/clientes.csv')

#Verifica os primeiro registros do DataFrame
print(df.head().to_string())

#Verifica os ultimos registros do DataFrame
print(df.tail().to_string())

#Verifica o numero de linhas e colunas do DataFrame
print('Qtd: ', df.shape)

#Verifica os tipos de dados de cada coluna
print('Tipagem', df.dtypes)

#Checar valores nulos
print('Valores nulos: ', df.isnull().sum())