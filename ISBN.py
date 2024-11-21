def is_valid(isbn):
    isbn = isbn.replace('-', '')
    isbn_as_list = list(isbn)

    if isbn == '':
        return False
    else:
        if 'X' in isbn_as_list:
            isbn_as_list[-1] = '10'

        new_isbn_list = []

        for number in isbn_as_list:
            if number != int(number) :
                return False
            else:
                new_isbn_list.append(int(number))
        for i in new_isbn_list:
            if i != int(i):
                print(type(i))
            else:
                lenght_of_digits = len(new_isbn_list)
                multiples = []

                for index, value in enumerate(new_isbn_list):
                    multiples.append((lenght_of_digits - index) * value)

                return bool(sum(multiples) % 11 == 0)


print(is_valid("3-598-21507-X"))