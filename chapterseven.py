def mysqrt(a):
    """Takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a"""
    x = a / 2

    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 1e-6:
            return y
        x = y


def eval_loop():
    """ Iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.
    Continues until the user enters 'done', and then return the value of the last expression it"""
    result = None
    while True:
        expression = input("Enter a Python expression to evaluate (or 'done' to exit): ")
        if expression == 'done':
            break
        try:
            result = eval(expression)
            print(result)
        except Exception as e:
            print("Error:", e)
    return result
