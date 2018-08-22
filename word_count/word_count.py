import chardet
from collections import Counter

files = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']


def get_text_from_file(file_name):
    with open(file_name, 'rb') as data:
        text = data.read()
        encoding = chardet.detect(text)['encoding']
        return text.decode(encoding)


def take_value(tuple):
    return tuple[0]


def get_words_from_text(text, length, amount):
    def check_length(word):
        return len(word) > length
    words = text.split(' ')
    word_list = list(words)
    word_list = list(filter(check_length, word_list))
    top_words = Counter(word_list).most_common(amount)
    top_words = list(map(take_value, top_words))
    return top_words


def count_common_words(files, length, amount):
    for file in files:
        text = get_text_from_file(file)
        common_words = get_words_from_text(text, length, amount)
        print('Top-{} most frequent words longer then {} characters in file "{}":'.format(amount, length, file))
        for word in common_words:
            print(word)


count_common_words(files, 6, 10)
