def ack(m, n):
    """Evaluates the Ackermann function"""
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))


def is_palindrome(s):
    """Takes a string argument and returns True if it is a palindrome and False otherwise"""
    reversed_s = s[::-1]
    return s == reversed_s


def is_power(a, b):
    """Takes parameters a and b and returns True if a is a power of b"""
    if a == 1:
        return True
    if a == 0 or (a % b != 0):
        return False
    return is_power(a // b, b)


def gcd(a, b):
    """Takes parameters a and b and returns their greatest common divisor"""
    while b != 0:
        a, b = b, a % b
    return a



