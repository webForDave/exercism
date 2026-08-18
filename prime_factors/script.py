"""
Computes the prime factors of a given natural number.
"""

def factors(value):
    """
    Parameters:
        value (int): number whose prime factors is to be found

    Returns:
        list: Collection of the prime factors of number

    Examples:
        >>> factors(60)
        [2, 2, 3, 5]
        >>> factors(901255)
        [5, 17, 23, 461]
    """

    factors_, divisor = [], 2

    while value != 1:
        if value % divisor == 0:
            factors_.append(divisor)
            value = value // divisor
            continue
        divisor += 1
        
    return factors_