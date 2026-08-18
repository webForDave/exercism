"""
Determines the Nth prime number.
"""

def prime(n):
    """
    Returns the nth prime number.
    
    Args:
        n: A positive integer (1-indexed)
        
    Returns:
        The nth prime number
        
    Raises:
        ValueError: If n is less than 1
    """
    # Handle invalid input
    if n < 1:
        raise ValueError('there is no zeroth prime')
    
    # First prime is 2
    if n == 1:
        return 2
    
    primes = [2]
    num = 3
    
    # Keep checking numbers until we find the nth prime
    while len(primes) < n:
        is_prime = True
        
        # Check if num is prime
        # Only need to check up to sqrt(num)
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
        
        num += 2  # Only check odd numbers
    
    return primes[-1]