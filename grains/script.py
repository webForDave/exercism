"""Functions to solve grains on a chessboard problem.

square: returns the number of grains on a particular square on the chessboard.
total: returns the total number of grains on the chessboard.
"""

def square(number):
    """Calculates the number of grains in a square on the chessboard.

    Parameters:
        Number (int): The square number on the chessboard.

    Returns:
        int: The total number of grains in the given square.
    """

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    square_number = number - 1
    return 2 ** square_number

def total():
    """Calculates the total number of grains on the chessboard.
    """

    total_grains = 0

    for num in range(1, 65):
        square_num = num - 1
        total_grains += 2 ** square_num

    return total_grains