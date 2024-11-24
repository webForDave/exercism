def square_of_sum(number):
    nums = 0
    for num in range(number + 1):
        nums += num
    return nums**2


def sum_of_squares(number):
    squares = 0
    for num in range(number + 1):
        squares += num ** 2
    return squares


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
