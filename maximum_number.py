def max_number(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_number(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max_number([14534,45632, 44352]))
