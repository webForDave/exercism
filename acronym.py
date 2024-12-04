def abbreviate(words):
    """Gives the abbreviation of a word.
    
    :param words/phrase: str - argument to check acronym.
    :return: str - abbreviated form of word/phrase.

    Function that takes a group of words, and convert them into the abbreviated form.
    """
    
    words = words.replace('-', ' ').replace('_', ' ').title().split()
    acronyms = ''
    for word in words:
        acronyms += word[0].title()
    return acronyms


print(abbreviate("Portable Network Graphics"))