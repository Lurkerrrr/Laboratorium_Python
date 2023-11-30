#2. Podnieś każdy element listy zawierającej liczby, do potęgi ustalonej przez użytkownika.
def podnies_do_potegi(list, potega):
    wyniki = [x ** potega for x in list]
    return wyniki

list = [2, 3, 4, 5]

potega_uzytkownika = int(input("Podaj potęgę, do której chcesz podnieść elementy listy: "))

wynik = podnies_do_potegi(list, potega_uzytkownika)
print("Zaktualizowany list:", wynik)