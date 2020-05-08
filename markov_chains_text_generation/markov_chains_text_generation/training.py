import nltk
import itertools
from collections import defaultdict
from .markov_chain import MarkovChain
from .data import consecutive
from .dialogs import read_dialogs

def train_chain(chain, text, window=3):
    for *from_tokens, to_token in consecutive(nltk.word_tokenize(text), window + 1):
        chain.add_transition(from_tokens, to_token)

def create_markov_chain(*_):
    return MarkovChain()

def train_by_pony(csv_path):
    dialogs = read_dialogs(csv_path)
    chains = defaultdict(create_markov_chain)

    for *_, pony, text in dialogs:
        chains[pony] = chains[pony] or MarkovChain()
        train_chain(chains[pony], text)

    return chains

def train_author_order(csv_path):
    dialogs = read_dialogs(csv_path)
    chain = MarkovChain()

    key_fn = lambda e: e[0]

    for title_name, title_dialogs in itertools.groupby(dialogs, key_fn):
        for cons_dialogs in consecutive(title_dialogs, 2):
            if cons_dialogs[0] != None:
                participants = [d[2] for d in cons_dialogs]
                chain.add_transition(*participants)

    return chain
