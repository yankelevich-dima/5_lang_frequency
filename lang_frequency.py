import re
import sys
from itertools import groupby


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
    words_frequency = {
        k: len(list(g))/len(words)
        for k, g in groupby(sorted(words))
    }
    return sorted(words_frequency.items(), key=lambda x_y: x_y[1], reverse=True)


if __name__ == '__main__':
    filepath = sys.argv[1]
    for word, frequency in get_most_frequent_words(load_data(filepath))[:10]:
        print('{} - {}'.format(word, frequency))
