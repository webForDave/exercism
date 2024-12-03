def divide_list(nums, divisor):
    new_list = [num / divisor for num in nums]
    return new_list


print(divide_list([6, 8, 10], 2))