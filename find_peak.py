def peak(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = nums[middle]

        if middle == max(nums):
            return middle_value
        elif max(nums) > middle_value:
            right = middle - 1
        else:
            left = middle + 1


print(peak([1, 3, 8, 12, 4, 2]))