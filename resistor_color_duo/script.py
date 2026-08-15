"""Returns the value of the first two resistor colors
"""

color_and_code = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def value(colors):
    """
    Parameters:
        colors (list): Colors whose value to lookup.

    Returns:
        int: The value of the first two colors from list
    """
    result = [str(color_and_code[colors[0]]), str(color_and_code[colors[1]])]
    return int("".join(result))
