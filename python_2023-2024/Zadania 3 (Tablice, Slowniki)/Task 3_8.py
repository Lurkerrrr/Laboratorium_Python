#8. Stwórz funkcję, która rysuje choinkę. Program powinien zawierać funkcję, przyjmującą parametr, określający wielkość choinki.
def choinka(n):
    for i in range(n):
        print(("+" * (i * 2 + 1)).center(n * 2 - 1))

choinka(5)