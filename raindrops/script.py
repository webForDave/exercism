"""Function to implement a complex version of FizzBuzz."""


def convert(number):
    """What is the correspoinding raindrop sound?

    Parameters: 
        number (int): number to be checked and converted.

    Returns:
        str: raindrop sound.

    Examples:
        >>> convert(28)
        "Plong"

        >>> convert(30)
        "PlingPlang"

    This function converts a number into its corresponding raindrop sound.

    """
    result = ""

    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        result = str(number)
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    return result