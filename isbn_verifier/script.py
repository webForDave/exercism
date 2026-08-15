"""is_valid checks if a given string of digits is a valid ISBN number"""

def is_valid(isbn: str):
    """
    Parameters: 
        isbn (str): String to validate

    Returns:
        bool: Whether or not the given isbn string is valid
    """

    if "-" in isbn: 
        isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    for char in isbn[:-1]:
        try:
            int(char)
        except ValueError:
            return False

    if isbn[-1] not in ["x", "X", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return False

    iterator, total = 10, 0

    for digit in isbn:
        if digit in ["X", "x"]:
            total += 10 * iterator
        else:
            total += int(digit) * iterator
        iterator -= 1

    if total % 11 == 0:
        return True

    return False