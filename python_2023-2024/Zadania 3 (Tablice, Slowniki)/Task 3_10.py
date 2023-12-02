#10. Napisz program rysujący macierz wypełnioną kolejnymi,  liczbami naturalnymi od 0. Program powinien zawierać funkcję, która przyjmuje parametr określający rozmiar macierzy (np. 7x7 lub 12x12 …)
def macierza(rozmiar1):
    for i in range(rozmiar1):
        for j in range(rozmiar1):
            print(i * rozmiar1 + j, end="\t")
        print()

rozmiar2 = 3
macierza(rozmiar2)