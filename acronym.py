def abbreviate(words):
    if '-' in words:
        words = words.replace('-', ' ')
    if '_' in words:
        words = words.replace('_', ' ')

    new_words = words.split()
    acronyms = ''
    for word in new_words:
        acronyms += word[0].title()
    return acronyms


print(abbreviate("Portable Network Graphics"))