def bubblesort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)-1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    pass

array = [6, 8, 1, 5, 3, 0, 7, 2, 6, 4, 9]
bubblesort(array)
print(array)
