import string


def convert_words_from_file(word_txt_path):
    """Reads a file, breaks each line into words, strips whitespace and punctuation from
    the words, and converts them to lowercase; returns the result"""
    cleaned_word_file = []
    with open(word_txt_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                cleaned_word = word.strip(string.whitespace + string.punctuation).lower()
                cleaned_word_file.append(cleaned_word)
    return cleaned_word_file


def get_clean_camping_ebook():
    """Reads the camping/camp cooking ebook, skips over the header information at the beginning of the file;
    strips whitespace and punctuation from the words, and converts them to lowercase"""
    cleaned_ebook = []
    with open('project_gutenberg_ebook_of_camping_and_camp_cooking.txt', 'r', encoding='utf-8') as file:
        found_line = False
        for line in file:
            if not found_line:
                if 'FRANK A. BATES.' in line.strip():
                    found_line = True
                continue
            for word in line.split():
                cleaned_word = word.strip(string.whitespace + string.punctuation).lower()
                cleaned_ebook.append(cleaned_word)
    return cleaned_ebook


def get_word_counts_from_cleaned_camping_ebook():
    """Gets the total word count, and word count per word used in the cleaned camping ebook"""
    cleaned_ebook = get_clean_camping_ebook()
    total_word_count = len(cleaned_ebook)
    unique_word_count = dict()
    for word in cleaned_ebook:
        if word not in unique_word_count:
            unique_word_count[word] = 1
        else:
            unique_word_count[word] += 1
    print("Total word count: " + str(total_word_count))
    print("Unique word count:")
    for word, amount in unique_word_count.items():
        print(word + ": " + str(amount))


get_word_counts_from_cleaned_camping_ebook()