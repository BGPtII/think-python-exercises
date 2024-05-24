def letter_frequency(word):
    """Returns the letter-to-frequency in decreasing order in a word"""
    letter_to_frequency = dict()
    for letter in word:
        letter_to_frequency[letter] = letter_to_frequency.get(letter, 0) + 1
    return dict(sorted(letter_to_frequency.items(), key=lambda x: x[1], reverse=True))


def get_anagrams(word_file_path):
    """Reads from a word list file and returns the collections of all anagrams"""
    with open(word_file_path) as file:
        anagram_dict = dict()
        for word in file:
            word = word.strip()
            formatted_word = ''.join(sorted(word))
            if formatted_word not in anagram_dict:
                anagram_dict[formatted_word] = [word]
            else:
                anagram_dict[formatted_word].append(word.strip())
    return list(anagram_dict.values())


def get_anagrams_descending_order(word_file_path):
    """Reads from a word lists and returns a collections of all anagrams from longest to shortest"""
    return sorted(get_anagrams(word_file_path), key=len, reverse=True)
