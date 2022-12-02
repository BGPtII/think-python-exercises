def is_palindrome_v2(s):
    """Takes a string argument s and returns True if it
    is a palindrome and False otherwise"""
    s_reverse = s[::-1]
    if s == s_reverse:
        return True
    return False


def rotate_word(s, amount):
    """Takes a string s and an integer amount as parameters, and returns a new string
    that contains the letters from the original string rotated by the given amount;
    positive rotates s right, negative rotates s left"""
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    index = 0
    s_rotated = ''
    while index < len(s):
        current_letter = s[index]
        if current_letter.isupper():
            alphabet_index = alphabet_upper.index(current_letter)
            s_rotated += alphabet_upper[alphabet_index + amount]
        else:
            alphabet_index = alphabet_lower.index(current_letter)
            s_rotated += alphabet_lower[alphabet_index + amount]
        index += 1
    return s_rotated
