def rotate(text, key):
    list_of_alphabet = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    indexes = []
    actual_index = []
    new_letters = []

    for letter in text:
        if letter.upper() in list_of_alphabet:
            indexes.append(list_of_alphabet.index(letter.upper()))
        else: 
            indexes.append(letter)

    for num in indexes:
        if type(num) == str:
            # actual_index.append(num)
            continue
        else:
            actual_index.append((num + key) % 26)

    for index in actual_index:
        new_letters.append(list_of_alphabet[index])

    list_as_sentnece = ''.join(new_letters)
    newest_char = []

    for new_char, char in zip(list_as_sentnece, text):
        if char == ' ':
            newest_char.append(' ')
        if type(char) == int:
            newest_char.append(char)
        if(char == char.lower()):
            new_char = new_char.lower()
        newest_char.append(new_char)

    new_word = ''.join(newest_char)

    return new_word


print(rotate("Testing 1 2 3 testing", 4))