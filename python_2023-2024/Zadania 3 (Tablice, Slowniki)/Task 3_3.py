#3. Napisz program, który doda dwie listy według indeksu, tak żeby lista1 i lista 2 pokazały logiczne zdanie
lista1 = ["M", "n", "im", "Pio"]
lista2 = ["am", "a", "ie", "tr"]

zdanie = " ".join([x + y for x, y in zip(lista1, lista2)])

print(zdanie)