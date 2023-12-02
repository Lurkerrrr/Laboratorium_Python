#12. Napisz program, który posiada funkcję fill, wypełniającą tablicę o rozmiarze n (podanym przez użytkownika), liczbami losowymi, z zakresu od 1 do 10. Dodatkowo program musi posiadać funkcję wypisującą elementy tablicy na ekranie, w jednym wierszu oraz funkcję search, wyszukującą wystąpienie liczby n, w wypełnionej tablicy.
import random

def fill_array(size):
    return [random.randint(1, 10) for _ in range(size)]

def print_array(array):
    print(*array)

def search_number(array, number):
    return number in array

array_size = int(input("Podaj rozmiar tablicy: "))
my_array = fill_array(array_size)
print("Wypełniona tablica:")
print_array(my_array)
number_to_search = int(input("Podaj liczbę do wyszukania: "))
if search_number(my_array, number_to_search):
    print(f"Liczba {number_to_search} znajduje się w tablicy.")
else:
    print(f"Liczba {number_to_search} nie znajduje się w tablicy.")