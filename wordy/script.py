"""
Parses and evaluate simple math word problems returning the answer as an integer.
"""

def answer(question):
    """
    Parameters:
        question (str): Math problem written as a sentence
    
    Returns:
        int: Answer to the math problem
    
    Examples: 
        >>> answer("What is 5?")
        5
        >>> answers("What is 7 minus 5?")
        2
        >>> answers("What is 25 divided by 5?")
        5
    """
     # Remove "What is" and "?" from the question
    question = question.strip()
    if not question.startswith("What is "):
        raise ValueError("syntax error")
    
    # Remove "What is " prefix and "?" suffix
    expression = question[8:]  # Remove "What is "
    if expression.endswith("?"):
        expression = expression[:-1]  # Remove "?"
    
    expression = expression.strip()
    
    # If no operations, just return the number
    if not any(op in expression for op in ["plus", "minus", "multiplied", "divided", "cubed"]):
        try:
            return int(expression)
        except ValueError:
            raise ValueError("syntax error")
    
    # Check for unsupported operations first
    # Remove valid operation patterns to check for unknown ones
    test_expr = expression
    # Temporarily remove valid operations to check for unknown ones
    test_expr = test_expr.replace("plus", " ")
    test_expr = test_expr.replace("minus", " ")
    test_expr = test_expr.replace("multiplied by", " ")
    test_expr = test_expr.replace("divided by", " ")
    test_expr = test_expr.replace("-", " ")
    
    # Check if there are any alphabetic characters left (unknown operations)
    for word in test_expr.split():
        if word.isalpha():
            raise ValueError("unknown operation")
    
    # Tokenize the expression
    tokens = []
    i = 0
    
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == '-':
            # Parse number (including negative numbers)
            num_start = i
            if expression[i] == '-':
                i += 1
            while i < len(expression) and expression[i].isdigit():
                i += 1
            tokens.append(int(expression[num_start:i]))
            continue
        elif expression[i:i+4] == "plus":
            tokens.append("plus")
            i += 4
        elif expression[i:i+5] == "minus":
            tokens.append("minus")
            i += 5
        elif expression[i:i+10] == "multiplied":
            tokens.append("multiplied")
            i += 10
            # Skip " by"
            if i < len(expression) and expression[i:i+3] == " by":
                i += 3
        elif expression[i:i+7] == "divided":
            tokens.append("divided")
            i += 7
            # Skip " by"
            if i < len(expression) and expression[i:i+3] == " by":
                i += 3
        elif expression[i] == ' ':
            i += 1
        elif expression[i] == 'b' and i+1 < len(expression) and expression[i+1] == 'y':
            # Skip standalone "by"
            i += 2
        else:
            # If we find any unexpected alphabetic character, it's an unknown operation
            if expression[i].isalpha():
                raise ValueError("unknown operation")
            i += 1
    
    # Check for valid token sequence
    if len(tokens) < 3:
        raise ValueError("syntax error")
    
    # The first token should be a number
    if not isinstance(tokens[0], (int, float)):
        raise ValueError("syntax error")
    
    # Process operations left to right
    result = tokens[0]
    i = 1
    
    while i < len(tokens):
        if i + 1 >= len(tokens):
            raise ValueError("syntax error")
        
        operation = tokens[i]
        next_num = tokens[i + 1]
        
        if not isinstance(next_num, (int, float)):
            raise ValueError("syntax error")
        
        if operation == "plus":
            result += next_num
        elif operation == "minus":
            result -= next_num
        elif operation == "multiplied":
            result *= next_num
        elif operation == "divided":
            if next_num == 0:
                raise ValueError("syntax error")
            result //= next_num
        else:
            raise ValueError("unknown operation")
        
        i += 2
    
    return result