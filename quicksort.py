def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] #Recursive case
        less = [i for i in array[1:] if i <= pivot] #Sub-array of the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot] #Sub-array of all the elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3, 324, 5313, 523, 625,7, 52]))