"""Reverses a string"""

def reverse(text):
    """
    Parameters:
        text (str): text to reverse

    Results:
        str: Reversed text
    """
    reversed_string = []

    for char in text[: :-1]:
        reversed_string.append(char)

    return "".join(reversed_string)