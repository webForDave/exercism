"""Determine if a number is perfect, abundant, or deficient 
based on Nicomachus' classification scheme for positive integers.
"""



def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    total = 0
    
    for num in range(1, number + 1):
        if num < number:
            if number % num == 0:
                total += num
            continue
        break

    if total == number:
        return "perfect"
    
    if total > number:
        return "abundant"
    
    return "deficient"