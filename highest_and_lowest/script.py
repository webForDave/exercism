def high_and_low(numbers):
    nums = numbers.split(" ")
    lowest, highest = int(nums[0]), int(nums[0])

    for digit in nums:
        if int(digit) < lowest:
            lowest = int(digit)
        if int(digit) > highest: 
            highest = int(digit)

    return " ".join([str(highest), str(lowest)])
        


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))