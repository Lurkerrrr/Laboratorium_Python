#2. Trójki Pitagorejskie
def trojki_pitagorskie(n):
    tab = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= n:
                tab.append((a, b, int(c)))
    return tab

n = 30
wynik = trojki_pitagorskie(n)
print("Trojki pitagorejskie w przedziale od 1 do", n, "to: ")
print(wynik)