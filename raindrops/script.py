"""Alternative implementation of FizzBuzz"""

def convert(number):
    """Gives the sentence result of divisions by 3, 5, and 7

    Parameters:
        number (int): The value to play with.
    Returns:
        str: result from dividion results

    Example:
        >>> convert(30)
            "PlingPlang"
        >>> convert(34)
            "34
    """
    result = str()

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)

    return result 
