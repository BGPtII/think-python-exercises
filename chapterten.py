import random


def nested_sum(outer_list):
    """Takes a list of lists of integers and adds up the elements from all the nested lists"""
    total_sum = 0
    for inner_list in outer_list:
        total_sum += sum(inner_list)
    return total_sum


def cumulative_sum_list(number_list):
    """Takes a list of numbers and returns a new list where the ith element is
    the sum of the first i + 1 elements from the original list"""
    cumulative_list = []
    cumulative_sum = 0
    for number in number_list:
        cumulative_sum += number
        cumulative_list.append(cumulative_sum)
    return cumulative_list


def middle(old_list):
    """Takes a list and returns a new list that contains all but the first and last elements"""
    return old_list[1:-1]


def chop(list_to_chop):
    """Takes a list, modifies it by removing the first and last elements"""
    if len(list_to_chop) > 1:
        del list_to_chop[0]
        del list_to_chop[-1]


def is_sorted(list_to_check):
    """Takes a list as a parameter and returns True if the list is sorted in ascending order"""
    for i in range(1, len(list_to_check)):
        if list_to_check[i] < list_to_check[i - 1]:
            return False
    return True


def is_anagram(word1, word2):
    """Takes two strings and returns True if they are anagrams"""
    word1 = word1.replace(' ', '').lower()
    word2 = word2.replace(' ', '').lower()
    return sorted(word1) == sorted(word2)


def has_duplicates(list_to_check):
    """Returns True if a list contains duplicate entries"""
    return len(list_to_check) != len(set(list_to_check))


def build_word_list(word_file_name):
    """Builds a list of words from a file containing words"""
    word_list = []
    with open(word_file_name, 'r') as words:
        for word in words:
            word_list.append(word.strip())
    return word_list


def in_bisect(sorted_word_list, word):
    """Check if a word is in a sorted word list using binary search"""
    low = 0
    high = len(sorted_word_list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_word = sorted_word_list[mid]
        if mid_word == word:
            return True
        elif mid_word < word:
            low = mid + 1
        else:
            high = mid - 1


def reverse_pair(word_list):
    """Two words are a reverse pair if each is the reverse of the other;
    prints all the reverse pairs in a word list"""
    for word in word_list:
        reverse_word = word[::-1]
        if reverse_word in word_list and reverse_word != word:
            print(word)
