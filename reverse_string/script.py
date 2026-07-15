"""Reverse a text"""


def reverse(text):
    """This function reverses a text.
    
        Parameters (str) : text to reverse.
        Returns str: reversed text.
    """
    text = list(text)
    reversed_text = []

    for char in text[: : -1]:
        reversed_text.append(char)

    return "".join(reversed_text)