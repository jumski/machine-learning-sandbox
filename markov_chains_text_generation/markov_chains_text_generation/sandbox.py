import pickle
from .data import csv_consecutive_tokens

csv_path = 'data/clean_dialog.csv'

class MarkovChain2:
    def __init__(self):
        self.rows = {}

    def add_transition(self, from_value, to_value):
        row_key = tuple(from_value)

        if row_key not in self.rows:
            self.rows[row_key] = {}
        row = self.rows[row_key]

        if to_value not in row:
            row[to_value] = 0

        row[to_value] += 1

    def get_possibilities(self, from_value):
        row_key = tuple(from_value)

        return self.rows[row_key]

def main():
    csv_file = open(csv_path, 'r')

    with open('data/markov.cache', 'rb') as cache:
        try:
            chain = pickle.load(cache)
        except EOFError:
            chain = MarkovChain2()

    # for *from_tokens, to_token in csv_consecutive_tokens(csv_file, 3):
    #     chain.add_transition(from_tokens, to_token)
    print(chain.get_possibilities(['What', 'if']))

    # with open('data/markov.cache', 'wb') as cache:
    #     pickle.dump(chain, cache)

