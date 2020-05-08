import random
from nltk.tokenize.treebank import TreebankWordDetokenizer
from .training import train_by_pony, train_author_order, train_on_all

def is_terminated(sentence):
    return sentence[-1] in set(['.', '?', '!'])

def generate_sentence(chain):
    window = 3
    sentence = [None for _ in range(window)]

    while not is_terminated(sentence):
        input_tokens = sentence[-window:]
        new_token = chain.generate_new_value(input_tokens)
        sentence.append(new_token)

    sentence_without_nones = sentence[window:]
    return TreebankWordDetokenizer().detokenize(sentence_without_nones)

def main():
    csv_path = 'data/clean_dialog.csv'
    dialogs_chains = train_by_pony(csv_path)
    chain = train_on_all(csv_path)
    author_order_chain = train_author_order(csv_path)

    author = random.choice(list(author_order_chain.rows.keys()))
    for _ in range(15):
        author = author_order_chain.generate_new_value(author)
        # sentence = generate_sentence(chain)
        sentence = generate_sentence(dialogs_chain[author])

        dialog_line = "{}: {}".format(author.upper(), sentence)

        print(dialog_line)


