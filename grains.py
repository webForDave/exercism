def square(number):
    n = number

    if n not in range(1, 64+1):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (n - 1)


def total():
    total = 0

    for num in range(1, 64+1):
        total += 2 ** (num - 1)
    return total


print(total())