def is_valid(isbn):
    isbn = isbn.replace('-', '')
    isbn_as_list = list(isbn)
    list_of_chars = list(map(str, range(1, 11)))
    list_of_chars.append('0')
    list_of_chars.append('X')
    print(list_of_chars)
    digits = []

    if len(isbn_as_list) == 0:
        return False
    elif len(isbn_as_list) > 10 or len(isbn_as_list) < 10:
        return False 
    elif 'X' in isbn_as_list and isbn_as_list[-1] != 'X':
        return False
    else:
        if isbn_as_list[-1] == 'X':
            isbn_as_list[-1] = '10'

        for char in isbn_as_list:
            if char not in list_of_chars:
                return False
            else:
                digits.append(int(char))

        length_of_digits = len(digits)
        multiplied_vlues = []

        for index, value in enumerate(digits):
            multiplied_vlues.append((length_of_digits - index) * value)

        return bool(sum(multiplied_vlues) % 11 == 0)

print(is_valid("3-598-21508-8"))