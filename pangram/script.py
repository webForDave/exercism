"""A pangram is a sentence using every letter of the alphabet at least once."""



def is_pangram(sentence):
    """This function checks whether a word is a pangram or not.
    
    Parameters:
        sentence (str): Sentence to check.
    Returns:
        bool: whether or not the sentence conforms to the condition.

    Examples:
        >>> is_pangram("The quick brown fox jumps over the lazy dog.")
            True

    Note:
        It is case insensitive so it does not mater if a letter is upercase (eg K) or lowercase (eg k).
    """

    # coverts the argument into string for easy handling, makes it lowecased and strips off whitespaces.
    sentence = list(str(sentence).lower().strip())

    special_characters = ['.', ',', '/', '?', ':', ';', ' ', '[', ']', '{', '}', '+', '=', '-', '_', '|', '"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    sentence = [character for character in sentence if character not in special_characters]
    seen = set()
    out = []

    for char in sentence:
        if char not in seen:
            out.append(char)
            seen.add(char)

    if len(out) != 26:
        return False
    
    return True

# print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))