#Przykład 1

import random

array = [[0 for j in range(10)] for i in range(10)]

for i in range(10):
    for j in range(10):
        array[i][j] = random.randint(-20, 50)

max_value = array[0][0]
for i in range(10):
    for j in range(10):
        if array[i][j] > max_value:
            max_value = array[i][j]

print("Wygenerowana tablica: ")
for row in array:
    print(row)

print("Maksymalna wartość w tablicy: ", max_value)


#Przykład 2

def createTwodimArray(m, n):
    lista = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(random.randint(-20, 50))
        lista.append(a)
    return lista

def printTwoDimArray(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end = "\t")
        print()


