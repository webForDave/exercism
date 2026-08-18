"""
Converts a phrase to its acronym.
"""

def abbreviate(words: str):
    """
    Parameters:
        word (str): word to abbreviate
    Returns:
        str: Abbreviated word

    Examples:
        >>> abbreviate("As Soon As Possible")
        ASAP
    """
    special_characters = [",", ".", "<", ">", "/", "?", ":", ";", "'", "{", "}", "[", "]", "=", "+", "-", "_", "|", "!", "~", "`"]
    abbreviation = ""
    for char in words:
        if char == "-":
            words = words.replace("-", " ")

        if char in special_characters:
            words = words.replace(char, "")

    words = words.split()

    for word in words:
        abbreviation += word[0].upper()

    return abbreviation