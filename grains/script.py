"""Calculate the number of grains of wheat on a chessboard.
A chessboard has 64 squares. 
Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.
"""


def square(number):
    """Calculates the number of grains on a given square.
    
        Parameters (int): specific number square number.
        Returns (int): The number of grain on the specified square
    """

    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")

    total_on_square = 1

    for x in range(1, number + 1):
        if x == 1: continue
        total_on_square += total_on_square
    return total_on_square


def total():
    """Calculates the total number of grains on the chessboard.

    Returns (int): The total number of grains of wheat on the chessboard.
    """
    total_on_square = 0

    for x in range(1, 65):
        total_on_square += square(x)

    return total_on_square

