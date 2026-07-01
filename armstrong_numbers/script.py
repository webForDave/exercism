"""Provides a function to determine whether a number is an Armstrong number.
"""

def is_armstrong_number(number):
    """Checks if a number is an armstrong number

    Parameter:
        number (int): Value to check.

    Returns:
        bool: whether or not the number is an armstrong number.
    """

    total = 0

    # This computes the total number of digits in the number.
    number_of_digits = len(str(abs(number)))

    for digit in str(number):
        total += int(digit) ** number_of_digits

    if total == number:
        return True
    return False