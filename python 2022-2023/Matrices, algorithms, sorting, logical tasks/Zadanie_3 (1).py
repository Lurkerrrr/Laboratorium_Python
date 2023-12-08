#Dokonaj symulacji poszczególnych algorytmów sortowania zapisanych w kolejnych arkuszach skoroszytu sortowanie xls. Następnie przetestuj podane algorytmy sortowanie w języku python, dla 100 elementowej listy, zawierającej liczby wygenerowane losowe z przedziału od 20 do 70.

#BubbleSort

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

arr = [24, 7, 15, 34, 5, 18]
bubbleSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print(arr[i], end = "")