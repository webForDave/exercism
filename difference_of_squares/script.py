"""Functions that find:
1. the square of the sum of the first N natural numbers.
2. the sum of the squares of the first N natural numbers.
3..the difference between them
"""

def square_of_sum(number):
    """Finds the square of the sum of the first N natural numbers.

    Parameters:
        number (int): natural number (N)

    Returns:
        int: square of the sum of the first natural numbers up to number.

    Examples:
        >>> square_of_sum(5)
        225
        >>> square_of_sum(10)
        3025
    """
    total = 0

    for num in range(1, number + 1):
        total += num

    return total ** 2


def sum_of_squares(number):
    """Finds the sum of the squares of the first natural numbers

    Parameters:
        number (int): natural number (N)
    
    Returns:
        int: sum of the squares of the first natural numbers up to number.
    
    Examples:
        >>> sum_of_squares(5)
        55
        >>> sum_of_squares(10)
        385
    """
    total = 0

    for num in range(1, number + 1):
        total += num ** 2

    return total


def difference_of_squares(number):
    """Finds the diference between:
    the square of the sum of the first N natural numbers and 
    the sum of the squares of the first natural numbers.

    Parameters: 
        number (int): natural number (N)

    Returns:
        int: Difference between the squares

    Examples:
        >>> difference_of_squares(5)
        170
        >>> difference_of_squares(100)
        25164150

    """
    return square_of_sum(number) - sum_of_squares(number)