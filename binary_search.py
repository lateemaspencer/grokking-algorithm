def binary_search(list, item):
    #low and high keep track of which
    #part of the list you'll search in.
    #first element
    low = 0
    #last element
    high = len(list) - 1
    #while the first element is less
    # than the last
    #this is a real expectation since
    #binary sort already assumes that the
    #list is sorted
    while low <= high:
        #we have to continuously recalculate
        #the middle element
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None #Null means nil in Python

my_list = [1 ,3, 5, 7, 9]

print binary_search(my_list, 3) # => 1
print binary_search(my_list, -1) # => None
