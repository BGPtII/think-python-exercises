from string import punctuation, whitespace, digits
from math import log
from chapterten import cumulative_sum_list, build_word_list, in_bisect
from random import randint


def get_words_from_text_file(text_file_path):
    """Returns the words from a text file, strips the whitespace and the punctuation from each word"""
    cleaned_words = []
    with open(text_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for line_word in line.split():
                for split_word in line_word.split('--'):
                    cleaned_word = split_word.strip(punctuation + whitespace + digits).lower()
                    if len(cleaned_word) != 0:
                        cleaned_words.append(cleaned_word)
    return cleaned_words


def text_file_histogram(text_file_path):
    """Returns a histogram of word frequency within a specified text file"""
    word_frequency = dict()
    cleaned_words = get_words_from_text_file(text_file_path)
    for word in cleaned_words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency


def text_file_20_most_frequent_words(text_file_path):
    """Returns the 20 most frequently used words within a specified text file"""
    frequency_top_20 = dict(sorted(text_file_histogram(text_file_path).items(), key=lambda x: x[1], reverse=True)[:20])
    return frequency_top_20


def text_file_words_not_in_word_file(word_file_path, text_file_path):
    """Returns unique words that are in the text file but not the file of words"""
    return set(text_file_histogram(text_file_path).keys()) - set(build_word_list(word_file_path))


def histogram(collection):
    """Maps the amount of occurrences to an item in a collection"""
    hist = dict()
    for item in collection:
        hist[item] = hist.get(item, 0) + 1
    return hist


def choose_from_hist(hist_dict):
    """Takes a histogram and returns a random value from the histogram,
    chosen with probability in proportion to frequency"""
    hist_keys = list(hist_dict.keys())
    cumulative_sum = cumulative_sum_list(hist_dict.values())
    return hist_keys[in_bisect(cumulative_sum, randint(1, cumulative_sum))]


def zipfs_law_get_log_f_log_r(word_file_path, selected_word):
    """Uses Zipf's law to return the log(f) and log(r) of a selected word in a file of words"""
    word_occurrences = dict()
    with open(word_file_path) as file:
        for word in file:
            word = word.strip()
            word_occurrences[word] = word_occurrences.get(word, 0) + 1
    if selected_word not in word_occurrences:
        return "Selected word not found"
    log_f = log(word_occurrences[selected_word])

    sorted_word_occurrences = sorted(word_occurrences.items(), key=lambda x: x[1], reverse=True)
    selected_word_rank = -1
    for rank, (word, occurrences) in enumerate(sorted_word_occurrences, start=1):
        if word == selected_word:
            selected_word_rank = rank
    log_r = log(selected_word_rank)

    return {"log(f)": log_f, "log(r)": log_r}