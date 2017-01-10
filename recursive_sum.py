def sum(arr, size):
    if size == 0:
        return 0
    else:
        return arr[size - 1] + sum( arr, size - 1)


arr = [2 , 4, 6]
print("Sum:",sum(arr, len(arr)))
