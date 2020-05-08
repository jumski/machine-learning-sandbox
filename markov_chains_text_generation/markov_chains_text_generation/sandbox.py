import numpy
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

    def get_weighted(self, from_value):
        row_key = tuple(from_value)
        row = self.rows[row_key]

        total = sum(row.values())
        weights = {}

        for to_value in row:
            weights[to_value] = row[to_value] / total

        return weights

    def generate_new_value(self, from_value):
        weighted = self.get_weighted(from_value)

        possibilities = list(weighted.keys())
        weights = list(weighted.values())

        return numpy.random.choice(possibilities, p=weights)

def main():
    csv_file = open(csv_path, 'r')

    with open('data/markov.cache', 'rb') as cache:
        try:
            chain = pickle.load(cache)
        except EOFError:
            chain = MarkovChain2()

    # for *from_tokens, to_token in csv_consecutive_tokens(csv_file, 3):
    #     chain.add_transition(from_tokens, to_token)
    # print(chain.get_possibilities(['What', 'if']))

    print(chain.generate_new_value(['What', 'if']))

    # with open('data/markov.cache', 'wb') as cache:
    #     pickle.dump(chain, cache)

