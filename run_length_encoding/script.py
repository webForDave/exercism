"""
Functions that implement run-length encoding and decoding.

Run-length encoding (RLE) is a simple form of data compression, 
where runs (consecutive data elements) are replaced by just one data value and count.

"""

def decode(string):
    """
    Parameters:
        string (str): Text to decode
    
    Returns:
        str: Decoded string
    
    Examples:
        >>> encode("12WB12W3B24WB")
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    
        >>> encode("2AB3CD4E")
        "AABCCCDEEEE"
    """
    if not string:
        return ""
    
    result = []
    count = 0
    
    for char in string:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            if count == 0:
                result.append(char)
            else:
                result.append(char * count)
                count = 0
    
    return "".join(result)


def encode(string):
    """
    Parameters:
        string (str): Text to encode

    Returns:
        str: Encoded string

    Examples:
        >>> encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
        "12WB12W3B24WB"

        >>> encode("AABCCCDEEEE")
        "2AB3CD4E"
    """

    if not string:
        return ""
    
    result = []
    count = 1
    prev_char = string[0]
    
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(prev_char)
            prev_char = char
            count = 1
    
    if count > 1:
        result.append(str(count))
    result.append(prev_char)
    
    return "".join(result)

print(decode(encode("zzz ZZ  zZ")))