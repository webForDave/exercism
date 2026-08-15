"""Functions to:
1. look up the numerical value associated with a particular color band
2. list the different band colors
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

def color_code(color):
    """Computes the numeric value associated with a resistor color.

    Parameters:
        color (str): Color whose number to look up.

    Returns: 
        int: Numeric value associated with resistor color
  
    """

    return color_and_code[color]


def colors():
    """Retuns all the colors present in the colors diction as a list
    """
    colors_list = []

    for color in color_and_code:
        colors_list.append(color)

    return colors_list

print(colors())