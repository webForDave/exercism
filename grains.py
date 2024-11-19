grains = []

def square(number):
    if number > 64 or number < 1:
        raise ValueError('Square must be between 1 and 64')
    for grain in range(1, number +1):
        grains.append(grain)

    return grains[number - 1]

print(square(2))


def total():
    return sum(grains)

print(total())