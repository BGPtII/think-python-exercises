def get_words_with_more_than_20_characters(file_name):
    """Reads a word list & returns only the words with more than 20 characters (not including whitespace)"""
    words = set()
    with open(file_name) as fin:
        for line in fin:
            word = line.strip()
            if len(word) > 20:
                words.add(word)
    return words


def has_no_e(word):
    """Returns whether the given word doesn't have the letter 'e' in it"""
    return 'e' not in word.lower()


def avoids(word, string_of_letters):
    """Takes a word and a string of forbidden letters; returns True whether the word uses any of the letters"""
    word = word.lower()
    string_of_letters = string_of_letters.lower()
    for letter in string_of_letters:
        if letter in word:
            return False
    return True


def uses_only(word, string_of_letters):
    """Takes a word and a string of letters; returns whether the word contains only letters in the list"""
    word = word.lower()
    string_of_letters = string_of_letters.lower()
    for letter in word:
        if letter not in string_of_letters:
            return False
    return True


def uses_all(word, string_of_letters):
    """Takes a word and a string of letters; returns whether the word uses all the required letters at least once"""
    uses_only(string_of_letters, word)


def is_abecedarian(word):
    """Returns whether the letters in a word appear in alphabetical order (double letters are ok)"""
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


def three_double_letters(word):
    """Returns whether there are three sets of consecutive double letters in the word"""
    word = word.lower()
    count = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    if count == 3:
        return True
    return False


def find_three_double_letter_words(word_file):
    """Returns the words that have three sets of consecutive double letters in a specified wordlist"""
    words = set()
    with open(word_file) as file:
        for line in file:
            word = line.strip()
            if three_double_letters(word):
                words.add(word)
    return words


def integer_is_palindrome(integer, start, length):
    """Returns whether the integer is a palindrome at a specific start and length"""
    integer_string = str(integer)[start: start + length]
    return integer_string[::-1] == integer_string


def has_required_palindromes(integer):
    """Returns whether the 6-digit integer has palindromes at each condition"""
    return ((integer_is_palindrome(integer, 2, 4)
             and integer_is_palindrome(integer + 1, 1, 5))
            and integer_is_palindrome(integer + 2, 1, 4)
            and integer_is_palindrome(integer + 3, 0, 6))


def odometer_required_palindrome_numbers():
    """Returns the odometer integers where the puzzle requirements are met"""
    numbers = set()
    i = 100000
    while i <= 999999:
        if has_required_palindromes(i):
            numbers.add(i)
        i += 1
    return numbers
