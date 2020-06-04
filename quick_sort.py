def quicksort(array, left, right):
    i = left
    j = right
    piv = array[(left + right) // 2]
    while(i <= j):
        while(array[i] < piv):
            i += 1
        while(array[j] > piv):
            j -= 1
        if(i <= j):
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if(j > left):
        quicksort(array, left, j)
    if(i < right):
        quicksort(array, i, right)




a = [4, 5, 1, 7, 6, 2, 9, 0, 3, 8]
left = 0
right = len(a) - 1
quicksort(a, left, right)
print(a)
