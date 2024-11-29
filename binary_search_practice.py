def find_occurence(iterable, target):
    left = 0
    right = len(iterable) - 1

    if len(iterable) == 0:
        raise ValueError("Temperature list is empty")
    
    while left <= right:
        middle = (left + right) // 2
        middle_value = iterable[middle]

        if middle_value == target:
            return middle
        elif middle_value > target:
            right = middle - 1
        elif middle_value < target:
            left = middle + 1
    return -1


print(find_occurence([10, 20, 25, 30, 40, 50], 25))