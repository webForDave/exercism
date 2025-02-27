def label(colors):
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

    value = f"{list_of_colors.index(colors[0])}{list_of_colors.index(colors[1])}{list_of_colors.index(colors[2])}"
    
    if value[-1] == '9':
        value.replace(value[-1], 'gigaohms')
    
    return value

print(label(["white", "white", "white"]))