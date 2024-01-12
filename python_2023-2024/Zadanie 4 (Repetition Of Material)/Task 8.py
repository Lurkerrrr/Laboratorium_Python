#8. Przybliżona wartość liczby e  

import math


def przyblizona_e(liczba_iteracji):
    suma = 0
    for i in range(liczba_iteracji):
        suma += 1 / math.factorial(i)
    return suma

liczba_iteracji = int(input("Podaj liczbę iteracji: "))
wynik_e = przyblizona_e(liczba_iteracji)

print(f"Przybliżona wartość liczby e po {liczba_iteracji} iteracjach: {wynik_e}")