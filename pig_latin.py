def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text_as_list = list(text)
    removed_consnants = []

    if text_as_list[0] in vowels or "".join(text_as_list[0:2]) == "xr" or "".join(text_as_list[0:2]) == "yt":
        text_as_list.append('ay')

    return ''.join(text_as_list)

print(translate("rhythm"))