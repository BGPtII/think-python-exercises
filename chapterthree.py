def right_justify(s):
    """takes a string named s as a parameter, and prints the string with enough leading spaces so that the last letter
    of the string is in column 70 of the display"""
    spaces_needed = 70 - len(s)
    print(' ' * spaces_needed + s)


def do_twice(f, value):
    """Takes two arguments, a function object and a value, and calls the function twice, passing the value as an
    argument"""
    f(value)
    f(value)


def print_twice(value):
    print(value)
    print(value)


def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)


def print_grid_3_3():
    line = '+ - - - - + - - - - +'
    side = '|         |         |'
    print(line)
    print(side)
    print(side)
    print(side)
    print(side)
    print(line)
    print(side)
    print(side)
    print(side)
    print(side)
    print(line)
