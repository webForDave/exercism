def steps(number):
    """Calculates the number of steps it takes to reach 1 
    according to the rules of the Collatz Conjecture.

    Parameter:
        number (int): The number to run the puzzle on.

    Returns:
        error: If the number is less than 1.
        int: The number of steps taken on the number.

    Examples: 
        >>> steps(12)
        9
    
    """
    total_steps = 0

    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    while number != 1:
        total_steps += 1
        if number % 2 == 0:
            number /= 2
        else: 
            number = (number * 3) + 1
    
    return total_steps