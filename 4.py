#Napisz funkcję, która otrzymuje dwa obiekty iterowalne (sekwencje) i zwraca listę wspólnych dla obu obiektów wartości.#
def intersection(lista1, lista2):
    lista3 = []
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3
l1 = [1,2,3,4,5]
l2 = [2,3,6,7,8]
print(intersection(l1,l2))
wynik = intersection("napis", "napis2")
print(wynik)
wynik2 = intersection((123,456,789),(123,777,888))
print(wynik2)