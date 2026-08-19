"""
Given a name and a new_number,
produces a sentence using that name and that new_number as an ordinal numeral.
"""

def line_up(name, number):
    """
    Parameters: 
        name (str): Name of person
        new_number (int): Location in line

    Returns:
        str: Name of person with position of person as a sentence

    Examples:
        >>> line_up("Mary", 1)
        "Mary, you are the 1st customer we serve today. Thank you!"
    """
    new_number = str(number)

    if new_number.endswith("1"):
        if new_number.endswith("11"):
            new_number += "th"
        else:
            new_number += "st"

    if new_number.endswith("2"):
        if new_number.endswith("12"):
            new_number += "th"
        else:
            new_number += "nd"

    if new_number.endswith("3"):
        if new_number.endswith("13"):
            new_number += "th"
        else:
            new_number += "rd"

    if len(new_number) == len(str(number)):
        new_number += "th"

    return f"{name}, you are the {new_number} customer we serve today. Thank you!"