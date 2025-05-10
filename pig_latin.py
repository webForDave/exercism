def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text_as_list = list(text)
    removed_consnants = []

    if text_as_list[0] in vowels or "".join(text_as_list[0:2]) == "xr" or "".join(text_as_list[0:2]) == "yt":
        text_as_list.append('ay')
    elif text_as_list[0] not in vowels:
        for _ in text_as_list:
            if text_as_list[0] not in vowels:
                if text_as_list[0] == 'y':
                    break
                removed_consnants.append(text_as_list[0])
                text_as_list.pop(0)
        text_as_list += removed_consnants
        text_as_list.append("ay")

    return ''.join(text_as_list)

print(translate("my"))