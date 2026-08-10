import math

def find_next_square(sq):
    """ Finds the next perfect square.

    Parameters:
        sq (int): Number whose next perfect square is to be found
    Returns: 
        int: The perfect square after sq
    """
    perfect_square = (math.sqrt(sq)) + 1

    if not perfect_square.is_integer(): return -1
    else: return int(perfect_square * perfect_square)