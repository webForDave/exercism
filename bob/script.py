"""What will bob say based on what you say to him?"""

import re

def response(hey_bob: str):
    """Returns the phrase Bob will say when you talk to him
    Parameters:
        hey_bob (str): What is said to bob.

    Returns:
        str: Wht bob replies based on what is said to him.

    Examples:
    >>> response("How are you?")
        "Sure."
    >>> response("HEY")
        "Whoa, chill out!"    
    """
    hey_bob = hey_bob.strip()

    if len(hey_bob) == 0:
        return "Fine. Be that way!"

    # regex pattern checks if the string contains non alphabet characters.
    if not re.search("[a-zA-Z]", hey_bob):
        if hey_bob.endswith("?"):
            return "Sure."
        return "Whatever."

    if hey_bob.endswith("?") and  hey_bob.upper() == hey_bob:
        return "Calm down, I know what I'm doing!"

    if hey_bob.endswith("?"):
        return "Sure."

    if hey_bob == hey_bob.upper():
        return "Whoa, chill out!"

    return "Whatever."