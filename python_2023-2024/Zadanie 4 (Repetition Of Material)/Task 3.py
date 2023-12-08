#3. Occurrence
def wystapienie(array):
    index = 0
    ilosc = 0
    for i in array:
        print(i, array.count(i))
        if array.count(i) > ilosc:
            ilosc = array.count(i)
            index = i
    print("\n\n",ilosc,index)