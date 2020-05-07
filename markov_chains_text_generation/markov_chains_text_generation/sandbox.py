import csv
import itertools
from collections import defaultdict

def read_dialogs(csv_path):
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        return [row[3] for row in reader][1:]

class MarkovChain:
    def __init__(self):
        self._rows = defaultdict(self._create_row)

    def add_occurence(self, from_val, to_val):
        self._rows[from_val][to_val] +=1

    def items(self):
        return self._rows.items();

    def _create_row(_):
        return defaultdict(lambda: 0)

def print_occurences(dialogs):
    dialog = dialogs[0]

    chain = MarkovChain()

    words = dialog.split()
    for prev,curr in itertools.zip_longest(words, words[1:]):
        chain.add_occurence(prev, curr)

    for from_word,to_words in chain.items():
        print('FROM WORD: ', from_word)
        for to_word,count in to_words.items():
            print("  ", to_word, " = ", count)

def main():
    csv_path = "data/clean_dialog.csv"
    dialogs = read_dialogs(csv_path)
    print_occurences(dialogs)
