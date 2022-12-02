def has_no_e(word):
    """returns True if string word doesn't have the letter e in
    it, False is otherwise
    """
    for letter in word:
        if letter == 'e':
            return False
    return True


def avoids(word, forbidden_letters):
    """Takes a word (string) and a string of forbidden letters, that returns True if
    the word doesn't use any of the forbidden letters and False otherwise.
    NOT case sensitive
    """
    word = word.lower()
    forbidden_letters = forbidden_letters.lower()
    for letter in word:
        for f_letter in forbidden_letters:
            if letter == f_letter:
                return False
    return True
