def disemvowel(string_):
    """Removes vowels from a string
        Parameters:
            string_ (str): Sentence/Phrase/word
        Returns:
            str: vowel free sentence/phrase/word
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for char in string_:
        if char in vowels:
            string_ = string_.replace(char, "")

    return string_
