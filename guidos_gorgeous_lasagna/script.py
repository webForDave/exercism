"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for lasagna.

    Parameters:
        number_of_layers (int): The number of layers to go in the oven.

    Returns:
        int: The preparation time per minute for all layers.
    """

    return PREPARATION_TIME * number_of_layers



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the total number of minutes a chef has been in the kitchen.

    Parameters:
        number_of_layers (int): the number of layers added to the lasagna.
        elapsed_bake_time (int): the number of minutes the lasagna has spent baking in the oven already.

    Returns:
        int: total number of minutes spent in the kitchen.
    """
    return elapsed_bake_time + (number_of_layers * 2)