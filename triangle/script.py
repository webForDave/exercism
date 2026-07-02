"""Functions that tell the type of a triangle based on the length of its size."""



def equilateral(sides):
    """An equilateral trianlge has its three sides equal.

    Parameters:
        sides (list): The sides of the triangle.

    Returns:
        bool: whether the sides satisfy the check.

    Examples: 
        >>> equilateral([3, 3, 3])
        True

        >>> equilateral([2, 4, 6])
        False

    This functions determines whether a triangle is equilateral.

    """

    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False
    
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    """An isosceles triangle has at least two sides the same length.

    Parameters:
        sides (list): The sides of the triangle.

    Returns:
        bool: whether the sides satisfy the check.

    Examples: 
        >>> isosceles([3, 3, 5])
        True

        >>> isosceles([2, 4, 6])
        False

    This functions determines whether a triangle is an isosceles triangle.

    """

    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False
    
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    return False


def scalene(sides):
    """A scalene triangle has all sides with different lengths.

    Parameters:
        sides (list): The sides of the triangle.

    Returns:
        bool: whether the sides satisfy the check.

    Examples: 
        >>> scalene([3, 4, 5])
        True

        >>> isosceles([2, 4, 4])
        False

    This functions determines whether a triangle is a scalene triangle.

    """

    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False
    
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return False
    return True
