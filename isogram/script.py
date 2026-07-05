"""An Isogram is a word or phrase without a repeating letter, 
however spaces and hyphens are allowed to appear multiple times.
"""



def is_isogram(phrase):
    """Determine if a word or phrase is an isogram.
    
    Parameters:
        phrase (str): word/phrase to check.
    Returns:
        bool: whether or not the phrase is an isogram.

    Examples:
        >>> is_isogram("isograms")
            False

    """

    # coverts the argument into string for easy handling, makes it lowecased and strips off whitespaces.
    phrase = list(str(phrase).lower().strip())

    special_characters = ['.', ',', '/', '?', ':', ';', '[', ']', '{', '}', '+', '=', '_', '|', '"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    phrase = [character for character in phrase if character not in special_characters]


    for char in phrase:
        if char in {' ', '-'}:
            continue 
        if phrase.count(char) > 1:
            return False
        
    return True

print(is_isogram('Isograms'))