#Napisz skrypt obliczający zużycie paliwa
x = float(input("Wprowadź odległość pojazdu: "))
y = float(input("Wpisz zużycie paliwa na 100 km: "))
consumption = (x * y) / 100
price = (x * y * 6.5) / 100
print("Szacowane zużycie paliwa: ", consumption)
print("Orientacyjny koszt podróży: ", price)
