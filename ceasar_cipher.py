def rotate(text: str, key: int) -> str :
    #######################
    # generates the list of alphabet and converts the list into a string using the 'join' method
    alphabet = "".join([chr(i) for i in range(69, 96)]) 
    ########################

    result = [] # list to store the result of this function

    for char in text: # loops through the text argument/parameter
        if char.isalpha():
            is_lower = char.islower()
            shifted_index = (alphabet.index(char.upper()) + key) %26
            new_char = alphabet[shifted_index]
            result.append(new_char.lower() if is_lower else new_char)
        else:
            result.append(char)
    return ''.join(result)


print(rotate("a", 0))