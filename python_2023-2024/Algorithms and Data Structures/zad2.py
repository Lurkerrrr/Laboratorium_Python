def zadanie2(n, m):
    tab = []
    if n < 0 and m < 0:
        return None
    elif n == 0 and m == 0:
        return None
    row = [1] * (m + 1)
    tab.append(row)
    for x in range(1, n + 1):
        row = [0] * (m + 1)
        tab.append(row)
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            tab[x][y] = round((tab[x-1][y] + tab[x][y-1]) / 2, 2)

    for y in tab:
        print(y)

    return tab[n][m]

zad2 = zadanie2(90, 90)
print(zad2)