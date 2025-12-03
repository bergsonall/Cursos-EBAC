import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

df = pd.read_csv('D:/GitHub/Cursos-EBAC/VisualizarComunicarDados/matematicaEstatistica/estatisticaBasica/clientes-v3-preparado.csv')

df['salario_categoria'] = (df['salario'] > df['salario'].median()).astype(int)

X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] #Preditor
Y = df['salario_categoria'] #Prever

# Dividir Dados: Treinamento e Teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criar e treinar modelo - Regressao Logistica
modelo_lr = LogisticRegression()
modelo_lr.fit(X_train, Y_train)

# Criar e treinar modelo - Arvore de Decisao
modelo_dt = DecisionTreeClassifier()
modelo_dt.fit(X_train, Y_train)

# Prever valores de teste
Y_prev_lr = modelo_lr.predict(X_test)

# Prever valores de teste
Y_prev_dt = modelo_dt.predict(X_test)

# Métricas de avaliação - Regressao Logistica
accuracy_lr = accuracy_score(Y_test, Y_prev_lr)
precision_lr = precision_score(Y_test, Y_prev_lr)
recall_lr = recall_score(Y_test, Y_prev_lr)

print(f"\nAcuracia da Regressao Logistica: {accuracy_lr:.2f}")
print(f"Precisão da Regressao Logistica: {precision_lr:.2f}")
print(f"Recall (Sensibilidade) da Regressao Logistica: {recall_lr:.2f}")

# Métricas de avaliação - Arvore de Decisao
accuracy_dt = accuracy_score(Y_test, Y_prev_dt)
precision_dt = precision_score(Y_test, Y_prev_dt)
recall_dt = recall_score(Y_test, Y_prev_dt)

print(f"\nAcuracia da Arvore de Decisao: {accuracy_dt:.2f}")
print(f"Precisão da Arvore de Decisao: {precision_dt:.2f}")
print(f"Recall (Sensibilidade) da Arvore de Decisao: {recall_dt:.2f}")

joblib.dump(modelo_lr, 'modelo_regressao_logistica.pkl')
joblib.dump(modelo_dt, 'modelo_arvore_decisao.pkl')