"""Implementation of the Ceasar Cipher 
"""

import re

def rotate(text: str, key: int):
    """
    Parameters:
        text (str): Sentence/Phrase to apply the cipher on
        key (int): Number of steps to use for each letter

    Returns:
        str: Encoded word/sentence/phrase

    Examples:
        >>> rotate("abcdefghijklmnopqrstuvwxyz", 13)
        "nopqrstuvwxyzabcdefghijklm"

        >>> rotate("omg", 5)
        "trl"
    """
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_text, encoded_text = text.lower(), []

    for char, word in zip(new_text, text):
        if not re.search("[a-z]", char):
            encoded_text.append(char)
            continue
        try:
            # Try the direct addition – may raise IndexError if out of range
            new_index = alphabets.index(char) + key
            if word == word.upper():
                encoded_text.append(alphabets[new_index].upper())
            else:
                encoded_text.append(alphabets[new_index])
        except IndexError:
            # If it goes out of range, wrap it using modulo by the alphabet length
            safe_index = (alphabets.index(char) + key) % len(alphabets)
            if word == word.upper():
                encoded_text.append(alphabets[safe_index].upper())
            else:
                encoded_text.append(alphabets[safe_index])

    return "".join(encoded_text)