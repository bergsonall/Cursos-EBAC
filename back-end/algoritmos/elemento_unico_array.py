from collections import Counter

array = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

contador = Counter(array)
unico = [item for item, count in contador.items() if count == 1]
print(sum(unico))