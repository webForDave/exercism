def main():
    print(response("WHAT'S GOING ON?"))

def response(hey_bob):
    """Determine the response of bob when he is told something.

    :param hey_bob: phrase - what is said to Bob 
    """
    if hey_bob.strip() == '' :
        return "Fine. Be that way!" 
    elif hey_bob == hey_bob.upper() and hey_bob.endswith('?') and any(char.isalpha() for char in hey_bob):
        return "Calm down, I know what I'm doing!"
    elif hey_bob == hey_bob.upper() and any(char.isalpha() for char in hey_bob):
        return "Whoa, chill out!"
    elif hey_bob.endswith('?'):
        return 'Sure.'
    else:
        return "Whatever."

if __name__ == '__main__':
    main()