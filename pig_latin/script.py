"""Pig Latin is a language easily understood by children, and gives adult a hard time."""



def translate(text):
    """Translates text from English to Pig Latin.

        Parameters:
            text (str): Text to be translated from English into Pig Latin.

        Returns:
            str: Translated text.

        Examples:
            >>> translate("apple")
            appleay

            >>> translate("xray")
            xrayay

        Note:
            The translation is defined using four rules.
            These rules look at the pattern of vowels and consonants at the beginning of a word.
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', "r", 's', 't', 'v', 'w', 'x', 'y', 'z']
    text = str(text).strip()

    phrase = list(text.split())
    new_phrase = []

    if len(phrase) > 1:
        for word in phrase:
            while True:
                if word.startswith('xr') or word.startswith('yt'):
                    break

                if word[0] == 'q' and word[1] == 'u':
                    word += 'qu'
                    word = word.removeprefix('qu')
                    break

                if word[0] == 'y' and word[1] in vowels:
                    word += word[0]
                    word = word.removeprefix(word[0])
                    break

                if word[0] == 'y':
                    break
                
                if word[0] in consonants:
                    word += word[0]
                    word = word.removeprefix(word[0])
                    continue
                break
            new_phrase.append(word + 'ay')
        return ' '.join(new_phrase)
        

    while True:
        if text.startswith('xr') or text.startswith('yt'):
            break
        if text[0] == 'q' and text[1] == 'u':
            text += 'qu'
            text = text.removeprefix('qu')
            break

        if text[0] == 'y' and text[1] in vowels:
            text += text[0]
            text = text.removeprefix(text[0])
            break

        if text[0] == 'y':
            break
        
        if text[0] in consonants:
            text += text[0]
            text = text.removeprefix(text[0])
            continue
        break

    return f'{text}ay'

print(translate("quick fast run"))