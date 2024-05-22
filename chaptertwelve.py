def sum_all(*numbers):
    """Takes any number of arguments and returns their sum"""
    return sum(numbers)


def most_frequent(text):
    """Takes a string and prints the letters in decreasing order of frequency"""
    letter_to_frequency = dict()
    for letter in text:
        letter_to_frequency[text.count(letter)] = letter
    descending_frequency = list(sorted(letter_to_frequency.keys(), reverse=True))
    for frequency in descending_frequency:
        print(letter_to_frequency[frequency])


def print_anagrams(word_file):
    """Reads from a word list and prints the collections of anagrams"""
    with open(word_file) as file:
        anagram_dict = dict()
        for word in file:
            word = word.strip()
            formatted_word = ''.join(sorted(word))
            if formatted_word not in anagram_dict:
                anagram_dict[formatted_word] = [word]
            else:
                anagram_dict[formatted_word].append(word.strip())
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            print(anagram_list)


def find_longest_anagram_list(word_file):
    """Reads from a word lists and prints the collections all anagrams from longest to shortest collection."""
    with open(word_file) as file:
        anagram_dict = dict()
        for word in file:
            word = word.strip()
            formatted_word = ''.join(sorted(word))
            if formatted_word not in anagram_dict:
                anagram_dict[formatted_word] = [word]
            else:
                anagram_dict[formatted_word].append(word)
    sorted_anagram_values = []
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            sorted_anagram_values.append(tuple(anagram_list))
    for anagram_list in sorted(sorted_anagram_values, key=len, reverse=True):
        print(anagram_list)
