def is_paired(input_string):
    open_square = 0
    closed_square = 0 
    open_curly = 0
    closed_curly = 0
    open_paren = 0
    closed_paren =0
    input_as_list = list(input_string)

    for brace in input_as_list:
        if brace == '[':
            open_square += 1
        elif brace == ']':
            closed_square += 1
        elif brace == '{':
            open_curly += 1
        elif brace == '}':
            closed_curly += 1
        elif brace == '(':
            open_paren += 1
        elif brace == ')':
            closed_paren += 1

        if open_square != open_square or open_curly != open_curly or open_paren != closed_paren:
            return False
        else:
            return True

print(is_paired("([{])"))