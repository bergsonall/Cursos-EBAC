import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('D:/GitHub/Cursos-EBAC/VisualizarComunicarDados/matematicaEstatistica/estatisticaBasica/clientes-v3-preparado.csv')

#Uso do pandas
print(f"Estatisticas do DataFrame: \n{df.describe()}")

print(f"Estatistica de um campo: \n{df[['salario', 'anos_experiencia']].describe()}")

print(f"\nCorrelação: \n {df[['salario', 'idade']].corr()}")
print(f"\nCorrelação com Normalização: \n {df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr()}")
print(f"\nCorrelação com Padronização: \n {df[['salarioStandardScaler', 'idadeStandardScaler']].corr()}")
print(f"\nCorrelação com Padronização: \n {df[['salarioRobustScaler', 'idadeRobustScaler']].corr()}")

df_filtro_idade = df[df['idade'] < 65]
print(f"\nCorrelação de clientes menores de 65 anos: \n{df_filtro_idade[['salario', 'idade']].corr()}")

# Variavel espuria - aumenta com o tempo
df['variavel_espuria'] = np.arange(len(df))
print(f"\nVariavel espuria: \n{df['variavel_espuria'].values}")

#armazena colunas do df nao padronizadas ou normalizadas
pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr()
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr(method='spearman')

print(f"\nCorrelação de Pearson:\n{pearson_corr}")
print(f"\nCorrelação de Spearman:\n{spearman_corr}")