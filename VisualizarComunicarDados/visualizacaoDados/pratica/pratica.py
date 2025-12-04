import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Config pd
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Cria DataFrame
df = pd.read_csv('D:/GitHub/Cursos-EBAC/VisualizarComunicarDados/visualizacaoDados/pratica/ecommerce_estatistica.csv')
print(df.describe())

print(df.nunique())

# Gráfico de Histograma
plt.figure(figsize=(10, 6))
plt.hist(df[['Nota']], bins='auto', color='green', alpha=0.8)
plt.title('Histograma de Notas')
plt.xlabel('Quantidade Notas')
plt.ylabel('Frequencia')
plt.xticks(ticks=range(0, int(df['Nota'].max()) + 1, 1))
plt.grid(True)
plt.show()

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Nota'], df['Desconto'], color='#5883a8', alpha=0.6, s=30)
plt.title('Dispersao entre Nota e desconto')
plt.xlabel('Nota')
plt.ylabel('Desconto')
plt.show()

# Mapa de calor
corr = df[['N_Avaliações_MinMax', 'Qtd_Vendidos_Cod', 'Material_Cod', 'Material_Freq']].corr()
plt.figure(figsize=(12, 8))
ax = sns.heatmap(corr, annot=True, cmap='RdBu')
ax.collections[0].colorbar.set_label("Força de Correlação")
plt.title('Correlação colunas DataFrame')
plt.show()

# Gráfico de barra
plt.figure(figsize=(10, 6))
plt.bar(df['Nota'].value_counts().index, df['Nota'].value_counts().values, color='#60aa65')
plt.title('Grafico de Barras Nota x Quantidade')
plt.xlabel('Nota')
plt.ylabel('Quantidade')
plt.show()

# Gráfico de pizza
plt.figure(figsize=(12, 7))
plt.pie(df['Temporada'].value_counts().values, labels=None, autopct='%.1f%%', startangle=90)
plt.legend(df['Temporada'].value_counts().index, title='Temporada', loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()

# Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade de Preço')
plt.show()

# Gráfico de Regressão
plt.figure(figsize=(10, 6))
sns.regplot(x=df['N_Avaliações_MinMax'], y=df['Qtd_Vendidos_Cod'], color="#8f3727", scatter_kws={'alpha': 0.8, 'color':'#34c289'})
plt.title('Regressao entre Numero de Avaliações x Quantidade Vendida')
plt.xlabel('Numero de Avaliações')
plt.ylabel('Quantidade Vendida')
plt.show()