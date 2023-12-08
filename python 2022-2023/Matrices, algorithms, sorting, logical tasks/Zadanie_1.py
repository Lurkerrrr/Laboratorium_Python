#Napisz program, który znajduje pozycję najmniejszego elementy listy(tablicy). Program wyświetla pozycję i wartość najmniejszego elementu listy.

import random
lista = [random.randint(0, 100)]
najmniejszy = min(lista)
pozycja = lista.index(najmniejszy)

print(f"Najmniejszy element:{najmniejszy}, pozycja:{pozycja}")
