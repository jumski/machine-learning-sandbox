import csv
import itertools
from collections import defaultdict

def read_dialogs(csv_path):
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')

        return [row[3] for row in reader][1:]

def main():
    csv_path = "data/clean_dialog.csv"
    dialogs = read_dialogs(csv_path)
    dialog = dialogs[0]

    def create_row():
        return defaultdict(lambda: 0)
    chain = defaultdict(create_row)

    words = dialog.split()
    for prev,curr in itertools.zip_longest(words, words[1:]):
        chain[prev][curr] += 1

    print(chain)


    # print(dialogs[0])
