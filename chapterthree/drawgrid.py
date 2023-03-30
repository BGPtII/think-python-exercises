def draw_grid():
    """Prints a 2x2 grid
    """
    row_separator = '+ - - - - + - - - - +\n'
    cell_border = '|         |         |\n'
    print(row_separator + cell_border * 4 + row_separator + cell_border * 4 + row_separator)