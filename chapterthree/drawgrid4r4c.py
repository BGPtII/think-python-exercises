def draw_grid_4r_4c():
    """Draws a 4x4 grid
    """
    row_separator = '+ - - - - + - - - - + - - - - + - - - - +\n'
    cell_border = '|         |         |         |         |\n'
    print((row_separator + cell_border * 4 + row_separator + cell_border * 4) * 2 + row_separator)