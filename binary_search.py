def find(search_list, value):
    left = 0
    right = len(search_list) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = search_list[middle]

        if middle_value == value:
            return middle
        elif middle_value > value:
            right = middle - 1
        else:
            left = middle + 1
    raise ValueError("value not in array")


print(find([1, 3, 4, 6, 8, 9, 11], 1))