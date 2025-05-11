def is_paired(input_string):
    open_curly_braces = close_curly_braces = open_parenthesis = close_parenthesis = open_brackets = close_brackets = 0

    for char in input_string:
        if char == '{':
            open_curly_braces += 1
        elif char == '}':
            close_curly_braces += 1
        elif char == '(':
            open_parenthesis += 1
        elif char == ')':
            close_parenthesis += 1
        elif char == '[':
            open_brackets += 1
        elif char == ']':
            close_brackets += 1

    if open_curly_braces == close_curly_braces and open_parenthesis == close_parenthesis and open_brackets == close_brackets:
        return True
    return False

print(is_paired("{hello ([agent672)}"))