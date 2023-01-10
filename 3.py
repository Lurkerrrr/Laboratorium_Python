def dodawanie(liczba1, liczba2):
    return liczba1 + liczba2
def odejmowania(liczba1, liczba2):
    return liczba1 - liczba2
def mnorzenia(liczba1, liczba2):
    return liczba1 * liczba2
def dzielenia(liczba1, liczba2):
    if liczba2 == 0:
        return None
    return liczba1 / liczba2

x = {'+':dodawanie, '-':odejmowania, '*':mnorzenia, '/':dzielenia}
a = float(input("Podaj liczbe 1: "))
b = float(input("Podaj liczbe 2: "))
d = input("Podaj dziawania (+, -, *, /): ")
wynik = x[d](a,b)
print(wynik)