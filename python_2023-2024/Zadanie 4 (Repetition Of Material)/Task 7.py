#7. Obliczanie liczby metodą Monte Carlo 
import random


def monte_carlo_pi(dokladnosc):
    punkty_kolo = 0
    punkty_kwadrat = 0

    for _ in range(dokladnosc):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        odleglosc = x**2 + y**2

        if odleglosc <= 1:
            punkty_kolo += 1

        punkty_kwadrat += 1

    pi_przyblizone = 4 * punkty_kolo / punkty_kwadrat

    return pi_przyblizone

dokladnosc = int(input("Podaj liczbę punktów do wygenerowania: "))
wynik_pi = monte_carlo_pi(dokladnosc)

print(f"Przybliżona wartość liczby π: {wynik_pi}") 

# Serializacja Książek 
import pickle
import random


# Klasa reprezentująca książkę
class Ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

# Funkcja do wypełniania bazy losowymi danymi
def wypelnij_baze(ilosc_ksiazek):
    baza = []
    for _ in range(ilosc_ksiazek):
        tytul = f"Tytuł{_}"
        autor = f"Autor{_}"
        rok = random.randint(1900, 2022)
        ksiazka = Ksiazka(tytul, autor, rok)
        baza.append(ksiazka)
    return baza

# Funkcja do wypisywania wszystkich danych w liniach
def wypisz_dane(baza):
    for ksiazka in baza:
        print(f"Tytuł: {ksiazka.tytul}, Autor: {ksiazka.autor}, Rok: {ksiazka.rok}")

# Funkcja do wyszukiwania książek po roku
def wyszukaj_po_roku(baza, rok):
    znalezione_ksiazki = [ksiazka for ksiazka in baza if ksiazka.rok == rok]
    return znalezione_ksiazki

# Główna część programu
if __name__ == "__main__":
    # Wypełnianie bazy losowymi danymi
    ilosc_ksiazek = 5
    baza_danych = wypelnij_baze(ilosc_ksiazek)

    # Serializacja i zapis bazy do pliku
    with open("baza_danych.pkl", "wb") as plik:
        pickle.dump(baza_danych, plik)

    # Wypisywanie wszystkich danych w liniach
    print("Wszystkie dane w bazie:")
    wypisz_dane(baza_danych)

    # Wyszukiwanie książek po roku
    rok_do_wyszukania = 2000
    znalezione_ksiazki = wyszukaj_po_roku(baza_danych, rok_do_wyszukania)

    print(f"\nKsiążki z roku {rok_do_wyszukania}:")
    wypisz_dane(znalezione_ksiazki)