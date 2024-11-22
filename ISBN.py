def is_valid(isbn):
    isbn = isbn.replace('-', '')
    isbn_as_list = list(isbn)
    list_of_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0', 'X']
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

print(is_valid("98245726788"))