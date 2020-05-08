import csv, itertools, nltk

csv_file = open('data/clean_dialog.csv', 'r')

def csv_tokens(csv_file):
    """
    Yields consecutive NLTK tokens, read from
    4th column in `csv_file`.
    """
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')

    for row in reader:
        for word in nltk.word_tokenize(row[3]):
            yield word

def consecutive(iterator, window = 2):
    """
    Yields list of consecutive elements for given `iterator`.
    Number of consecutive elements is defined by `window`.
    """
    previous = []

    for element in iterator:
        previous.append(element)

        if len(previous) >= window:
            yield previous[-window:]

def csv_consecutive_tokens(csv_file, window = 2):
    """
    Yields list of consecutive tokens in given `csv_file`.
    Number of tokens can be set by `window`.
    """
    return consecutive(csv_tokens(csv_file), window)
