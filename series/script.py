"""
Given a string of digits, 
outputs all the contiguous substrings of length n in that string in the order that they appear.
"""

def slices(series, length):
    """
    Parameters:
        series (str): string of number
        length (int): length of substring

    Returns:
        list: collection of substrings of length n in string

    Examples:
        >>> slices("49142", 3)
        ["491", "914", "142"]
        >>> slices("49142", 4)
        ["4914", "9142"]
    """
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 1:
        raise ValueError("slice length cannot be negative")

    if len(series) == 0:
        raise ValueError("series cannot be empty")

    new_series, result = [], []
    
    while len(series) > 0:
        for digit in series[0 : 1]:
            new_series.append("".join(digit))
            series = series.removeprefix(digit)

    if length > len(new_series):
        raise ValueError("slice length cannot be greater than series length")

    while len(new_series) >= length:
        result.append("".join(new_series[0: length]))
        new_series.remove(new_series[0])

    return result