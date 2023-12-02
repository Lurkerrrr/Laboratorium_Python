#13. Napisz program,  który w tablicy dwuwymiarowej 10×10 umieszcza losowo na przekątnej liczby od 1 do 10, a poza nią zera. Dodatkowo oblicza on sumę liczb znajdujących się na przekątnej. Program powinna zawierać trzy metody:
#generujDane() — umieszcza dane w tablicy,

#wyswietlWynik() — pokazuje zawartość tablicy na ekranie monitora.

#przetworzDane() — oblicza i wyświetla sumę liczb znajdujących się na przekątnej,
import random

class DiagonalMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = self.generate_data()

    def generate_data(self):
        return [[random.randint(1, 10) if i == j else 0 for j in range(self.size)] for i in range(self.size)]

    def display_result(self):
        for row in self.matrix:
            print(row)

    def process_data(self):
        diagonal_sum = sum(self.matrix[i][i] for i in range(self.size))
        print(f"Suma liczb na przekątnej wynosi: {diagonal_sum}")

matrix_instance = DiagonalMatrix(10)
matrix_instance.display_result()
matrix_instance.process_data()