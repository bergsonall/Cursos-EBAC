import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('C:/Users/Bruno/PycharmProjects/PythonProject/tratamentoDados/clientes_limpos.csv')

df_filtro_basico = df[df['idade'] > 100]

print(f'Filtro basico: \n{df_filtro_basico[['nome', 'idade']]}')

#Identificar outliers com Z-Score
z_score = stats.zscore(df['idade'])
outliers_z = df[z_score >= 3]
print(f'Outliers pelo Z-Score: \n{outliers_z}')

#Filtra os outliers usando o Z-Score
df_zscores = df[(z_score < 3)]
print(f'Dados sem outliers Z-Score: \n{df_zscores}')

#Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print(f'Limite IQR Baixo: {limite_baixo}, Limite IQR Alto: {limite_alto}')

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print(f'Outliers pelo IQR: \n{outliers_iqr}')

#Filtra os outliers usando o IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]
print(df_iqr)

#Filtrar endereços invalidos (menos de 3 linhas)
df['endereco'] = df['endereco'].apply(lambda x: 'Endereco invalido' if not isinstance(x, str) or len(x.split('\n')) < 3 else x)
print(f'Dados com enderecos invalidados: {(df['endereco'] == 'Endereco invalido').sum()}')

#Filtrar nomes muito longos (mais de 50 caracteres)
df['nome'] = df['nome'].apply(lambda x: 'Nome invalido' if isinstance(x, str) and len(x) > 50 else x)
print(f'Dados com nomes invalidados: {(df['nome'] == 'Nome invalido').sum()}')

df.to_csv('C:/Users/Bruno/PycharmProjects/PythonProject/tratamentoDados/clientes_remove_outliers.csv', index=False)