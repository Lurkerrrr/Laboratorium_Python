#Dokonaj symulacji poszczególnych algorytmów sortowania zapisanych w kolejnych arkuszach skoroszytu sortowanie xls. Następnie przetestuj podane algorytmy sortowanie w języku python, dla 100 elementowej listy, zawierającej liczby wygenerowane losowe z przedziału od 20 do 70.

#insertionSort

def insertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [24, 7, 15, 34, 5, 18]
insertionSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print(arr[i])