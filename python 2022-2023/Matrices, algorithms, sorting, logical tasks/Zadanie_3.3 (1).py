#Dokonaj symulacji poszczególnych algorytmów sortowania zapisanych w kolejnych arkuszach skoroszytu sortowanie xls. Następnie przetestuj podane algorytmy sortowanie w języku python, dla 100 elementowej listy, zawierającej liczby wygenerowane losowe z przedziału od 20 do 70.

#selectionSort

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])

arr = [24, 7, 15, 34, 5, 18]
selectionSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print(arr[i])