def ack(m, n):
    """Evaluates the Ackermann function for integers m & n"""
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


def is_power(a, b):
    """takes parameters a and b and returns True if a is a power of b"""
    if a % b != 0:
        return False
    elif a / b == b:
        return True
    a = a / b
    return is_power(a, b)


def greatest_common_divisor(a, b):
    """Takes parameters a and b and returns their greatest common divisor"""
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)


def is_palindrome(s):
    """Takes a string argument s and returns True if it
    is a palindrome and False otherwise"""
    index = 0
    while index < len(s):
        if s[index] != s[index - 1]:
            return False
        else:
            return True
        index += 1

