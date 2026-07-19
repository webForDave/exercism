def line_up(name, number):
    number = str(number)

    if number.endswith("11") or number.endswith("12") or number.endswith("13"):
        number += "th"
    elif number.endswith("1"):
        number += "st"
    elif number.endswith("2"):
        number += "nd"
    elif number.endswith("3"):
        number += "rd"
    else: number += "th"

    return f"{name}, you are the {number} customer we serve today. Thank you!"

print(line_up("David", 120))