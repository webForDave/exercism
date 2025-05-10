def piggy(text):

    """
    Let's confuse those grown-ups 😈
    This function takes a normal word and turns it into Pig Latin — the secret language of chaos and children.
    You’ll only understand it if you still have recess or eat cereal with cartoons on. 🍭
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    text_as_list = list(text)
    removed_consnants = []

    if text_as_list[0] in vowels or "".join(text_as_list[0:2]) == "xr" or "".join(text_as_list[0:2]) == "yt":
        text_as_list.append('ay')
    # actual brain of piggy 😂
    elif text_as_list[0] not in vowels:
        for _ in text_as_list: # we're just looping for vibe, fr 
            if text_as_list[0] not in vowels:
                if "".join(text_as_list[0:2]) == "qu":
                    removed_consnants.append("".join(text_as_list[0: 2]))
                    text_as_list.pop(0)
                    text_as_list.pop(0)
                    break
                removed_consnants.append(text_as_list[0])
                text_as_list.pop(0)
            if text_as_list[0] == 'y':
                break

        text_as_list += removed_consnants
        text_as_list.append("ay")

    return ''.join(text_as_list)

def translate(text):

    """
    Translates an entire sentence into Pig Latin using the mighty piggy() function.
    Just hand it a string — it'll handle the chaos.
    """
    
    words = text.split()
    new_words = []
    
    if words:
        for word in words:
            new_words.append(piggy(word))
        return " ".join(new_words)
    return piggy(text)

print(translate("quick"))