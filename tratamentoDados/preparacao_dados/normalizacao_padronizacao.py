import pandas as pd 
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('D:/GitHub/CURSOS-EBAC/tratamentoDados/preparacao_dados/clientes-v2-tratados.csv')

print(df.head())

df = df[['idade', 'salario']]

#Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

#Padronização - StanderdScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

#Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print("minMaxScaler (De 0 a 1):")
print(f'Idade - Min: {df['idadeMinMaxScaler'].min():.4f} Max: {df["idadeMinMaxScaler"].max():.4f} Mean: {df["idadeMinMaxScaler"].mean():.4f} Std: {df['idadeMinMaxScaler'].std():.4f}')
print(f'Salario - Min: {df['salarioMinMaxScaler'].min():.4f} Max: {df["salarioMinMaxScaler"].max():.4f} Mean: {df["salarioMinMaxScaler"].mean():.4f} Std: {df['salarioMinMaxScaler'].std():.4f}')

print("\nMinMaxScaler (De -1 a 1):")
print(f'Idade - Min: {df['idadeMinMaxScaler_mm'].min():.4f} Max: {df["idadeMinMaxScaler_mm"].max():.4f} Mean: {df["idadeMinMaxScaler_mm"].mean():.4f} Std: {df['idadeMinMaxScaler_mm'].std():.4f}')
print(f'Salario - Min: {df['salarioMinMaxScaler_mm'].min():.4f} Max: {df["salarioMinMaxScaler_mm"].max():.4f} Mean: {df["salarioMinMaxScaler_mm"].mean():.4f} Std: {df['salarioMinMaxScaler_mm'].std():.4f}')

print("\nStandardScaler (Ajuste a media a 0 e o desvio padrao a 1):")
print(f'Idade - Min: {df['idadeStandardScaler'].min():.4f} Max: {df["idadeStandardScaler"].max():.4f} Mean: {df["idadeStandardScaler"].mean():.18f} Std: {df['idadeStandardScaler'].std():.4f}')
print(f'Salario - Min: {df['salarioStandardScaler'].min():.4f} Max: {df["salarioStandardScaler"].max():.4f} Mean: {df["salarioStandardScaler"].mean():.18f} Std: {df['salarioStandardScaler'].std():.4f}')

print("\nRobustScaler (Ajuste a mediana e IQR):")
print(f'Idade - Min: {df['idadeRobustScaler'].min():.4f} Max: {df["idadeRobustScaler"].max():.4f} Mean: {df["idadeRobustScaler"].mean():.4f} Std: {df['idadeRobustScaler'].std():.4f}')
print(f'Salario - Min: {df['salarioRobustScaler'].min():.4f} Max: {df["salarioRobustScaler"].max():.4f} Mean: {df["salarioRobustScaler"].mean():.4f} Std: {df['salarioRobustScaler'].std():.4f}')