from time import time


def convert_epoch_time():
    """Reads the current epoch time; returns it as (days, hours, minutes, seconds) since epoch"""
    epoch_time = time()
    days, remainder = divmod(epoch_time, 24 * 3600)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    return int(days), int(hours), int(minutes), int(seconds)


def check_fermat(a, b, c, n):
    """Takes four parameters and checks to see if Fermat’s theorem holds"""
    if n > 2 and a**n + b**n == c**n:
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn’t work."


def check_fermat_prompt():
    """Prompts the user to enter the values a, b, c, n to check Fermat's theorem"""
    try:
        a = int(input("Enter a value for a: "))
        b = int(input("Enter a value for b: "))
        c = int(input("Enter a value for c: "))
        n = int(input("Enter a value for n: "))
        return check_fermat(a, b, c, n)
    except ValueError:
        return "Invalid input, numbers only."


def is_triangle():
    """Prompts the user to enter 3 sticks' lengths (must be the same unit); returns if they can form a triangle"""
    try:
        a = int(input("Enter a value for a: "))
        b = int(input("Enter a value for b: "))
        c = int(input("Enter a value for c: "))
        return a > b + c or b > a + c or c > a + b
    except ValueError:
        return "Invalid input, numbers only."
