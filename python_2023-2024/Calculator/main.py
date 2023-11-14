print(
" 1) dodawanie"
" 2) Odejmowanie"
" 3) mnożenie"
" 4) dzielenie"
" 5) potęgowanie")

x = int(input('Liczba - '))
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

if x == 1:
    print (a + b)
if x == 2:
    print(a - b)
if x == 3:
    print(a * b)
if x == 4:
    print(a / b)
if x == 5:
    print(a ** b)
else:
    print('nieprawidłowy numer')
