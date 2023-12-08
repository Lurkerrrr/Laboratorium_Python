#4. Napisz program, który oblicza sumę̨ wyrażenia 1 + 2 - 3+ 4 - 5 + ... ± n dla dowolnego n. 
n = int(input("Podaj liczbe: "))

def obliczenie(n):
    result = 0
    sign = 1

    for i in range(1, n + 1):
        result += sign * i
        sign *= -1

    return result

a = int(input("Wartosc n: "))
result = obliczenie(n)
print(f"Suma 1+2-3+4-5+...± n {n} wynosi {result}")