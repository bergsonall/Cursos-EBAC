import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\GitHub\Cursos-EBAC\analiseDados\VisualizarComunicarDados\matematicaEstatistica\estatisticaBasica\clientes-v3-preparado.csv')

# Grafico de dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')

# Grafico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de Salarios')
plt.xlabel('Salario')
plt.show()

# Grafico PairPlot - Densidade e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.title('Pairplot')
plt.show()

# Grafico de Regressao
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
plt.title('Regressao de salario por idade')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

# Grafico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nivel de educação')
plt.show()