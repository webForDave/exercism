def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text_as_list = list(text)

    if text_as_list[0] in vowels or (text_as_list[0] == 'x' and text_as_list[1] == 'r') or (text_as_list[0] == 'y' and text_as_list[1] == 't'):
        text_as_list.append('ay')

    return ''.join(text_as_list)


print(translate("pig"))