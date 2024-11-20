list_of_colors = [
    'black', 
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white',
    ]


def color_code(color):
    for i in range(len(list_of_colors)):
        if list_of_colors[i] == color:
            return i

def colors():
    return list_of_colors
    