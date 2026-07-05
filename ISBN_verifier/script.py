"""The ISBN-10 verification process is used to validate book identification numbers."""


def is_valid(isbn):
    """Validates a book identification number.
    
    Parameters:
        isbn (str): ISBN string.
        
    Returns:
        bool: if isbn number is valid.
    """
    isbn = list(isbn)
    multiplier, new_isbn, total = 10, [], 0

    if len(isbn) < 1:
        return False
    
    if isbn[-1] not in {'X', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        return False

        
    if isbn[-1] == 'X':
        isbn[-1] = 10

    isbn = [char for char in isbn if char != '-']

    for char in isbn[0 : 9]:
        if char not in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
            return False

    if len(isbn) < 10 or len(isbn) > 10:
        return False
    

    for num in isbn:
        new_isbn.append(int(num) * multiplier)
        multiplier -= 1

    for num in new_isbn:
        total += num

    if total % 11 == 0:
        return True

    return False