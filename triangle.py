def equilateral(sides):
    a, b, c = sides
    if a == 0 and b == 0 and c == 0:
        return False
    elif a == b == c:
        return True
    else:
        return False


def isosceles(sides):
    a, b, c = sides
    if a == b and a + b >= c:
        return True
    elif a == c and a + c >= b:
        return True
    elif b == c and b + c >= a:
        return True
    else:
        return False


def scalene(sides):
    a, b, c = sides
    if a != b and a != c and b != c:
        if a + b >= c  and a + c >= b and b + c >= a:
            return True
    return False