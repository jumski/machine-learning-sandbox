from collections import defaultdict
from .data import csv_consecutive_tokens

csv_path = 'data/clean_dialog.csv'

class MarkovChain2:
    def __init__(self):
        self.rows = defaultdict(lambda:
                                defaultdict(lambda: 0))

    def add_transition(self, from_value, to_value):
        row_key = tuple(from_value)

        self.rows[row_key][to_value] += 1

    def get_possibilities(self, from_value):
        row_key = tuple(from_value)

        return self.rows[row_key]

def main():
    csv_file = open(csv_path, 'r')
    markov_chain = MarkovChain2()

    for *from_tokens, to_token in csv_consecutive_tokens(csv_file, 3):
        markov_chain.add_transition(from_tokens, to_token)

    print(markov_chain.get_possibilities(['What', 'if']))
