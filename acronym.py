def abbreviate(words):
    sentence = words.replace('-', ' ').replace('_', ' ').title().split()
    acronyms = ''
    for word in sentence:
        acronyms += word[0].title()
    return acronyms


print(abbreviate("Portable Network Graphics"))