import sys

def steps(number):

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    count = 0
    if number < 1 or number == 0:
        return count
    else:
         while number != 1:
            number = number / 2 if number % 2 == 0 else number * 3 + 1
            count += 1
    return count

print(steps(int(sys.argv[1])))