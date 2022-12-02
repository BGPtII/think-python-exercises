import math

def mysqrt(a):
    """Takes a as a parameter, chooses a reasonable value of x, and returns an estimate
     of the square root of a"""
    x = a / 2
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def test_square_root():
    print('a' + '   ' + 'mysqrt(a)' + '      ' + 'math.sqrt(a)' + '   ' + 'diff')
    print('-   ---------      ------------   ----')
    for i in range(1, 10):
        col1 = float(i)
        col2 = round(mysqrt(col1), 11)
        col3 = round(math.sqrt(col1), 11)
        col4 = abs(mysqrt(col1) - math.sqrt(col1))
        if col4 != 0:
            col4 = '{:.11e}'.format(col4)
        print(col1, '{:<14} {:<14}'.format(col2, col3), col4)


def eval_loop():
    """iteratively prompts the user, takes the resulting input and evaluates it using eval,
    and prints the result. Continues until the user enters 'done', and then
    returns the value of the last expression it evaluated
    """
    while True:
        user_input = input('Enter what you want evaluated: ')
        if user_input == 'done':
            return last_input
        else:
            last_input = eval(user_input)
            print(last_input)
