from pprint import pprint
from test_faker import names
import math

def binary_search(names, item, low, high, count):

    if (low > high):
        return None

    else:

        mid = math.ceil((low + high) / 2)

        count[0] = count[0] + 1

        if (names[mid] == item):
            return mid
        else:
            if (names[mid] > item):
                return binary_search(names, item, low, mid-1, count)
            else:
                return binary_search(names, item, mid+1, high, count)

count = [0]

print("Logarithm 128 ", int(math.log(len(names), 2)))

found = binary_search(names, "Nicole", 0, (len(names)-1), count)

if (found != -1):
    print("Your name was found in names list at index ", found)
else:
    print("Your name was not found in list")

print

print("The number of elements searched in names was ", count[0])