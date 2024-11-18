def convert(number):
    """
    Converts a number into a specific string based on divisibility:
    - "Pling" for 3
    - "Plang" for 5
    - "Plong" for 7
    If not divisible by any, returns the original number as a string.

    :param number: The number to evaluate.
    
    :returns str: The corresponding string or the number itself.
    """
    int_num = int(number)
    result = ''

    if int_num % 3 == 0:
        result += 'Pling'
    if int_num % 5 == 0:
        result += 'Plang'
    if int_num % 7 == 0:
        result += 'Plong'

    return result 

    # if int_num % 3 == 0 and int_num % 5 == 0 and int_num % 7 == 0:
    #     return 'PlingPlangPlong'
    # elif int_num %3 == 0 and int_num % 5 == 0:
    #     return 'PlingPlang'
    # elif int_num % 3 == 0 and int_num % 7 == 0:
    #     return 'PlingPlong'
    # elif int_num % 5 == 0 and int_num % 7 == 0:
    #     return 'PlangPlong'
    # elif int_num % 3 == 0:
    #     return 'Pling'
    # elif int_num % 5 == 0:
    #     return 'Plang'
    # elif int_num % 7 == 0:
    #     return 'Plong'
    # else:
    #     return str(number)
