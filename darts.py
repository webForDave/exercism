def score(x, y):
    distance = pow((x**2 + y**2), 1/2)

    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    else:
        return 10


print(score(-9, 9))