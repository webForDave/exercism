"""What would lackadaisical Bob say?"""


def response(hey_bob):
    """Bob's response predictor.
    Parameters:
        hey_bob (str): What someone says to Bob.

    Returns:
        (str): What Bob replies.

    Examples: 
        >>> response("How are you?")
        "Sure."

        >>> response("ARE YOU OKAY?")
        "Calm down, I know what I'm doing!"


    Note:
        Bob only ever answers one of five things:
        1. Sure.
        2. Whoa, chill out!
        3. Calm down, I know what I'm doing!
        4. Fine. Be that way!
        5. Whatever.
    """

    reply = "Whatever."
    hey_bob = str(hey_bob).strip()

    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    
    if hey_bob.endswith("?"): # handles cases where Bob is asked a question.
        if hey_bob.isalpha() is False: 
            if hey_bob == hey_bob.lower(): # handles questions that are in lower case
                return "Sure."
        if hey_bob == hey_bob.upper(): # handles questions that are yelled at him.
            return "Calm down, I know what I'm doing!"
        return "Sure."
    
    # handles statements that contains other characters like numbers, and symbols.
    if not any(character.isalpha() for character in hey_bob): 
        return reply

    if hey_bob == hey_bob.upper():
        return "Whoa, chill out!"
    
    return reply
