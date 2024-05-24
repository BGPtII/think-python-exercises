def count_letter_a_in_banana():
    """Uses the count method to return the number of letter 'a's in the word banana"""
    return 'banana'.count('a')


def any_lowercase(word):
    """Returns whether the word contains a lowercase letter"""
    for char in word:
        if char.islower():
            return True
    return False


def rotate_word(s, amount):
    """Takes a string and an integer as parameters, and returns a new string that contains the letters from the
    original string rotated by the given amount"""
    rotated_string = ''
    for char in s:
        if char.isupper():
            rotated_char = chr((ord(char) - ord('A') + amount) % 26 + ord('A'))
        elif char.islower():
            rotated_char = chr((ord(char) - ord('a') + amount) % 26 + ord('a'))
        else:
            rotated_char = char
        rotated_string += rotated_char
    return rotated_string
