def abbreviate(words):
    words = words.replace('-', ' ').replace('_', ' ').title().split()
    acronyms = ''
    for word in words:
        acronyms += word[0].title()
    return acronyms


print(abbreviate("Portable Network Graphics"))