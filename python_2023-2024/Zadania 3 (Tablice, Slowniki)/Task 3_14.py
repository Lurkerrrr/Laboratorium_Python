#14. Napisz program,  który w tablicy dwuwymiarowej 10×10 umieszcza losowo na jednej części po przekątnej liczby od 0 do 9, wraz z przekątną, a poza nią zera.  Napisz funkcję, która odwraca tę macierz symetrycznie w osi przekątnej powstałej macierzy.
def reverse_matrix(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

example_matrix = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]

print("Macierz przed odwróceniem:")
for row in example_matrix:
    print(row)

reverse_matrix(example_matrix)

print("\nMacierz po odwróceniu:")
for row in example_matrix:
    print(row)