def square_digits(num):
    """Takes every digit in the numer and squares it.
    """
    num = str(num)
    return int("".join([str(int(digit) * int(digit)) for digit in num]))