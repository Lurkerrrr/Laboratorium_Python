#Napisz program, który znajduje pozycję najmniejszego elementy listy(tablicy). Program wyświetla pozycję i wartość najmniejszego elementu listy.

import random


def find_min_elem(dane):
    min_dane = [0]
    for i in dane:
        if i < min:
            min = i

    return min

def find_poz_min_elem(dane):
    min_poz = 0
    for i in range(1, len(dane)):
        if dane[i] < dane[min_poz]:
            min_poz = i
    return min_poz

lista = []
for i in range(20):
    lista.append(random.randint(10, 50))
print(lista)
print("Najmniejszy element listy to:", find_min_elem(lista))
print("Pozycja tego elementu to:", find_poz_min_elem(lista) + i)

poz = find_poz_min_elem(lista)
print("Najmniejszy elemnt listy to:", lista[poz])
print("Pozycja tego elementu to:", poz + i)
