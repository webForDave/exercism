"""Functions to determine the types of triangles based on the length of their sides.
"""

def sides_validity(sides):
    """Validates the sides of a triangle to to conform to the criteria.

    Parameters:
        sides (list): three sides of the triangle
    Returns:
        bool: whether or not the triangle conforms to the criteria

    Note:
        For a shape to be a triangle at all, 
        all sides have to be of length > 0, 
        and the sum of the lengths of any two sides must be greater than or equal to the length of the third side.
    """

    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    
    if sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[1] + sides[2] < sides[0]:
        return False

    return True

def equilateral(sides):
    """Checks whether a triangle is equilateral

    Parameters:
        side (list): three sides of a triangle
    Returns:
        bool: whether or not the triangle with the given sides is equilateral
    """

    if sides_validity(sides=sides) is False:
        return False

    if sides[0] == sides[1] == sides[2]:
        return True

    return False


def isosceles(sides):
    """Checks whether a triangle is isosceles
    
    Parameters:
        side (list): three sides of a triangle
    Returns:
        bool: whether or not the triangle with the given sides is isosceles
    """

    if sides_validity(sides=sides) is False:
        return False
    
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True

    return False


def scalene(sides):
    """Checks whether a triangle is scalene
    
    Parameters:
        side (list): three sides of a triangle
    Returns:
        bool: whether or not the triangle with the given sides is scalene
    """
    
    if sides_validity(sides=sides) is False:
        return False
    
    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        return True

    return False