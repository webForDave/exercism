def repetitve_work(text: str):
    """Prevents writing unnecessarily long code
    """
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


    if text[0] in vowels or text.startswith("xr") or text.startswith("yt"):
        return text + "ay"

    for char in text:
        if text.startswith("qu"):
            text += "qu"
            text = text.removeprefix("qu")
        elif char[0] in consonants:
            text += char
            text = text.removeprefix(char)
            continue
        else:
            return text + "ay"

    for char in text:
        if text[0] in consonants:
            text += char
            text = text.removeprefix(char)
        else: 
            return text + "ay"
        if text[0] == "y":
            return text + "ay"
        

    for char in text:
        if char[0] in consonants:
            text += char
            text = text.removeprefix(char)
            continue
        return text + "ay"

    return None

def translate(text: str):
    """Actual translate code
    """
    result = []
    text = text.split()

    for word in text:
        result.append(repetitve_work(word))

    return " ". join(result)  