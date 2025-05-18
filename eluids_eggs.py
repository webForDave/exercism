def egg_count(display_value):
    bits = []
    dividend = display_value
    sum = 0

    while dividend != 0:
        if dividend % 2 == 1:
            sum +=1 
        dividend //= 2

    return sum  

print(egg_count(2000000000))