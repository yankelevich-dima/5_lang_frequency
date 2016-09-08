import re
import sys
from collections import Counter

TOP_COUNT = 10


def load_data(filepath):
    text = ''
    with open(filepath, 'r') as infile:
        text = infile.read()
    return text


def get_most_frequent_words(text):
    text = text.lower()
    # Removing special symbols
    text = re.sub('\W+', ' ', text)
    words = list(filter(None, text.split(' ')))
    c = Counter(words).most_common()
    return list(map(lambda x_y: (x_y[0], x_y[1] / len(words)), c))


if __name__ == '__main__':
    filepath = sys.argv[1]
    for word, frequency in get_most_frequent_words(load_data(filepath))[:TOP_COUNT]:
        print('{} - {}'.format(word, frequency))
