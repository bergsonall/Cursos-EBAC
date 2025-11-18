import pandas as pd

#Função para calcular o cubo de um numero
def eleva_cubo(num):
    return num ** 3


#Expressao de lambda para calcular o cubo de um numero
eleva_cubo_lambda = lambda num: num**3

#Testando as duas funcoes
print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

#Carregando o DataFrame
df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]})

df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo_lambda'] = df['numeros'].apply(lambda x: x**3)

print(df.to_string())