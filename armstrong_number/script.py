"""An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
"""

def is_armstrong_number(number):
    """Checks whether a number is an armstrong number."""
    total = 0

    for i in str(number):
        total += int(i) ** len(str(number))

    if total == number:
        return True

    return False