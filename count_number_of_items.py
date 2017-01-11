def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print("Number of items in list:", count([1,2,3]))