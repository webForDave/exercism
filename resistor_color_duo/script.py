def value(colors):
    val = []
    colors_and_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    val.append(str(colors_and_values[colors[0]]))
    val.append(str(colors_and_values[colors[1]]))


    return int("".join(val))