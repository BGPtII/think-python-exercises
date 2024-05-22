def store_words_as_keys(word_list_file_name):
    """Returns a dictionary with the words in the word list file as the keys"""
    word_dict = {}
    with open(word_list_file_name, 'r') as file:
        for word in file:
            word_dict[word.strip()] = None
    return word_dict


def inverse_dictionary(dict_sample):
    """Returns an inverted dictionary, setting the key as an empty list if it doesn't exist"""
    inverse_dict = {}
    for key, value in dict_sample.items():
        inverse_dict.setdefault(value, []).append(key)
    return inverse_dict


def has_duplicates(sample_list):
    """Uses a dictionary to return True if the sample_list has any duplicates"""
    dupe_dict = {}
    for list_item in sample_list:
        if list_item in dupe_dict:
            return True
    return False
