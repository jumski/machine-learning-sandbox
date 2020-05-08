import pickle
from .data import csv_consecutive_tokens
from .markov_chain import MarkovChain
from nltk.tokenize.treebank import TreebankWordDetokenizer

csv_path = 'data/clean_dialog.csv'

def main():
    csv_file = open(csv_path, 'r')
    window = 3

    chain = MarkovChain()
    print('Building markov chain...')
    for *from_tokens, to_token in csv_consecutive_tokens(csv_file, window + 1):
        chain.add_transition(from_tokens, to_token)

    sentence = ['What', 'if', 'you']

    print()
    for i in range(500):
        input_tokens = sentence[-window:]
        new_token = chain.generate_new_value(input_tokens)
        sentence.append(new_token)

    print(TreebankWordDetokenizer().detokenize(sentence))

