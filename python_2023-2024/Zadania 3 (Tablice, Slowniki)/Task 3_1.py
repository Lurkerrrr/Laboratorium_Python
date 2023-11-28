#1. Dodaj nową pozycję do listy po określonej pozycji
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)

print(list1)