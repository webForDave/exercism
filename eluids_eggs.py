def egg_count(display_value):
    bits = []
    dividend = display_value
    sum = 0

    while dividend != 0:
        bits.insert(0, dividend % 2)
        dividend //= 2

    for bit in bits:
        if bit == 1:
            sum += 1

    return sum  

print(egg_count(2000000000))