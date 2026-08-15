"""Function to check whether a sentence/phrase is an Isogram or not
An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, 
however spaces and hyphens are allowed to appear multiple times.
"""

import re

def is_isogram(phrase: str):
    """
    Parameters:
        phrase (str): English phrase to validate

    Returns:
        bool: Whether or not the phrase contains repeating letters.

    Examples:
    >>> is_isogram("lumberjacks")
        True

    >>> is_isogram("background")
        True

    >>> is_isogram("Hello world)
        False
    """

    alphabets = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    phrase = phrase.lower()

    # search the string and removes every non English character (eg: empty spaces, numbers and symbols)
    for char in phrase:
        if not re.search('[a-z]', char):
            phrase = phrase.replace(char, '')

    # searches the phrase, if the current character in the phrase is found in the alphabet dictionary
    # adds 1 to the current value of the letter in the dictionary
    for char in phrase:
        for letter, _ in alphabets.items():
            if char == letter:
                alphabets[letter] += 1
            

    for letter in alphabets:
        if alphabets[letter] > 1:
            return False

    return True

print(is_isogram("six-year-old"))