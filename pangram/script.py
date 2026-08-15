"""Function to check whether a sentence is a Pangram or not
A pangram is a sentence using every letter of the alphabet at least once. 
It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
"""

import re

def is_pangram(sentence: str):
    """
    Parameters:
        sentence (str): English sentence to validate

    Returns:
        bool: Whether or not the sentence contains all the alphabets of English language.

    Examples:
    >>> pangram("abcdefghijklmnopqrstuvwxyz")
        True

    >>> pangram("a quick movement of the enemy will jeopardize five gunboats")
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

    sentence = sentence.lower()

    # search the string and removes every non English character (eg: empty spaces, numbers and symbols)
    for char in sentence:
        if not re.search('[a-z]', char):
            sentence = sentence.replace(char, '')

    # searches the sentence, if the current character in the sentence is found in the alphabet dictionary
    # adds 1 to the current value of the letter in the dictionary
    for char in sentence:
        for letter, _ in alphabets.items():
            if char == letter:
                alphabets[letter] += 1
            

    for letter in alphabets:
        if alphabets[letter] == 0:
            return False

    return True