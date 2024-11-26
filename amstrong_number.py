def is_amstrong(number):
    number_as_string = str(number)
    sum = 0

    for num in number_as_string:
        sum += int(num) ** len(number_as_string)
    return bool(sum == number)
