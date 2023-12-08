#1. Funkcja wypełniająca tablicę losowymi liczbami
import random


def random_numbers(n=100):
    tab = []
    for i in range(n):
        tab.append(random.randint(1, 21))
        return tab

answer = random_numbers(10)
print(answer)