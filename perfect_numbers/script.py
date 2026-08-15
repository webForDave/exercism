"""Determine if a number is perfect, abundant, or deficient 
based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.
"""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    total = 0
    for digit in range(1, number):
        if number % digit == 0:
            total += digit

    if total == number:
        return "Perfect"

    if total > number:
        return "Abundant"

    return "Deficient"

print(classify(28))