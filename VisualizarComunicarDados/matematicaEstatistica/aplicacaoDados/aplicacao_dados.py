import pandas as pd
import joblib

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Carregar modelo treinado
modelo_regressao_linear = joblib.load('D:\GitHub\Cursos-EBAC\VisualizarComunicarDados\matematicaEstatistica\modeloRegressao\modelo_regressao_linear.pkl')
modelo_regressao_logistica = joblib.load('D:\GitHub\Cursos-EBAC\VisualizarComunicarDados\matematicaEstatistica\modeloClassificacao\modelo_regressao_logistica.pkl')
modelo_arvore_decisao = joblib.load('D:\GitHub\Cursos-EBAC\VisualizarComunicarDados\matematicaEstatistica\modeloClassificacao\modelo_arvore_decisao.pkl')

# Dados dos novos funcionarios
dados_novos_funcionario = pd.DataFrame({
    'idade': [35, 45, 30],
    'anos_experiencia': [6, 12, 5],
    'nivel_educacao_cod': [2, 3, 4], #Ensino media, Ensino superior, Pos graduacao
    'area_atuacao_cod': [1, 4, 3] #Educacao, Tecnologia, Saude
})

# Prever o salario com o modelo treinado
salario_previsto = modelo_regressao_linear.predict(dados_novos_funcionario)

for x in range(len(salario_previsto)):
    print(f"Salario previsto do {x+1}º funcionario: R${salario_previsto[x]:.2f}")


# Classificar o salario com modelo de treinamento
categoria_salario = modelo_regressao_logistica.predict(dados_novos_funcionario)

for x in range(len(salario_previsto)):
    categoria = 'Acima da mediana' if categoria_salario[x] == 1 else 'Abaixo da mediana'
    print(f"Categoria de salario previsto do {x+1}º funcionario: {categoria}")