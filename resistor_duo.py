def value(colors):
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

    first_index = list_of_colors.index(colors[0])
    second_index = list_of_colors.index(colors[1])

    indexes = f"{first_index}{second_index}"

    return int(indexes)