#11. Zmodyfikuj powyższy program program tak, aby wypisywał tabliczkę mnożenia.
def tabliczka(rozmiar):
    for i in range(1, rozmiar + 1):
        for j in range(1, rozmiar + 1):
            print(i * j, end="\t")
        print()

tabliczka_rozmiar = 5
tabliczka(tabliczka_rozmiar)