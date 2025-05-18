def egg_count(display_value):
    bits_as_one = 0

    while display_value != 0:
        if display_value % 2 == 1:
            bits_as_one +=1 
        display_value //= 2

    return bits_as_one  

print(egg_count(2000000000))