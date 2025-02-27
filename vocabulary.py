"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    new_word = []
    for char in word:
        new_word.append(char)
    new_word.insert(0, 'un')
    return ''.join(new_word)


def make_word_groups(*vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    new_list = [vocab_words[0]]
    for i in vocab_words[1:]:
        if vocab_words[0] == 'en':
            word = f'en{i}'
            new_list.append(word)
        elif vocab_words[0] == 'pre':
            word = f'pre{i}'
            new_list.append(word)
        if vocab_words[0] == 'auto':
            word = f'auto{i}'
            new_list.append(word)
        if vocab_words[0] == 'inter':
            word = f'inter{i}'
            new_list.append(word)
    return ' :: '.join(new_list)

print(make_word_groups('pre', 'postion', 'tend'))


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    word_list = list(word)
    if word_list[-5] == 'i':
        word_list[-5] = 'y'
    del word_list[-4:]

    return ''.join(word_list)


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    sentence_as_list = sentence.split(' ')
    adjective = sentence_as_list[index]

    if '.' in adjective:
        adjective = adjective.strip('.')
    adjective = list(adjective)
    adjective.append('en')
    return ''.join(adjective)
