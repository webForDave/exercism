def rebase(input_base, digits, output_base):
    power = len(digits) - 1
    dividend = 0
    new_bases = []

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2: 
        raise ValueError("output base must be >= 2")
    

    for number in digits:
        if number < 0 or number >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        dividend += number * (input_base**power)
        power -= 1

    while dividend !=0 :
        new_bases.insert(0, dividend % output_base)
        dividend = dividend // output_base 

    if len(new_bases) == 0:
        return [0]

    return new_bases

print(rebase(2, [1, 2, 1, 0, 1, 0], 10))