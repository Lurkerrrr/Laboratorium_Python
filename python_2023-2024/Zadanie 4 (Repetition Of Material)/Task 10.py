#10.  Konwertuje listę 

def konwertuj_na_zagniezdzone_slownik(lista):
    if not lista:
        return {}
    
    slownik = {}
    aktualny_slownik = slownik

    for element in lista:
        aktualny_slownik[element] = {}
        aktualny_slownik = aktualny_slownik[element]

    return slownik

# Przykładowa lista
lista = [1, 2, 3, 4]

# Konwersja na zagnieżdżony słownik kluczy
wynik = konwertuj_na_zagniezdzone_slownik(lista)

# Wyświetlenie wyniku
print(wynik)