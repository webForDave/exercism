def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text_as_list = list(text)
    removed_consnants = []

    if text_as_list[0] in vowels or (text_as_list[0] == 'x' and text_as_list[1] == 'r') or (text_as_list[0] == 'y' and text_as_list[1] == 't'):
        text_as_list.append('ay')
    else:
        for _ in text_as_list:
            if text_as_list[0] not in vowels:
                removed_consnants.append(text_as_list[0])
                text_as_list.pop(0)
        text_as_list = text_as_list + removed_consnants
        text_as_list.append('ay')

    return ''.join(text_as_list)


print(translate("thrush"))