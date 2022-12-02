def right_justify(s):
    """Takes a string named s as a parameter and prints the string with enough leading
    spaces so that the last letter of the string is in column 70 of the display
    """
    s = ' ' * (70 - len(s)) + s
    print(s)


def draw_grid():
    row_separator = '+ - - - - + - - - - +\n'
    cell_border = '|         |         |\n'
    print(row_separator + cell_border * 4 + row_separator + cell_border * 4 + row_separator)


def draw_grid_4r_4c():
    row_separator = '+ - - - - + - - - - + - - - - + - - - - +\n'
    cell_border = '|         |         |         |         |\n'
    print((row_separator + cell_border * 4 + row_separator + cell_border * 4) * 2 + row_separator)
