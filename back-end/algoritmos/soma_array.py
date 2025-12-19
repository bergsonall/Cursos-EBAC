from collections import Counter

meu_array = [1, 2, 2, 3, 3, 4, 5, 6, 6]

contador = Counter(meu_array)
print(contador)

unicos_soma = [item for item, count in contador.items() if count == 1]
print(sum(unicos_soma))