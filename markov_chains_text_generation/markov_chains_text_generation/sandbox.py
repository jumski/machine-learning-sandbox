import nltk
import itertools
from .markov_chain import MarkovChain
from .dialogs import dialogs_in_csv

def tokens(csv_path):
    for dialog in dialogs_in_csv(csv_path):
        for token in nltk.word_tokenize(dialog):
            yield token

def main():
    csv_path = "data/clean_dialog.csv"

    iter_1 = tokens(csv_path)
    iter_2 = tokens(csv_path)
    iter_3 = tokens(csv_path)

    next(iter_2)
    next(iter_3)
    next(iter_3)

    for a,b,c in itertools.zip_longest(iter_1, iter_2, iter_3):
        print("a,b,c", [a,b,c])
