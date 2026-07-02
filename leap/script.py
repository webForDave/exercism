"""Function to determine whether a given year is a leap year."""

def leap_year(year):
    """Checks a year if it meets the criteria for being a leap year.

    Parameters:
        year (int): Year to be checked.

    Returns: 
        bool: whether or not the year is a leap year.
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0