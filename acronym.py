def abbreviate(words):
    """Generate the abbreviated form of a phrase.
    
    :param words/phrase: str - Phrase to be abbreviated.
    :return: str - Abbreviated phrase.

    This function takes a phrase as argument, removes every separators including 
    spaces, and hyphens, captitalizes the initials of every word in the phrase
    and returns the abreviated form of the phrase. 
    """
    
    words = words.replace('-', '').replace('_', '').title().split()
    return ''.join(char[0] for char in words)
