from nltk.tokenize.treebank import TreebankWordDetokenizer
from .training import train_by_pony, train_participant_order

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
    print(generate_sentence(dialogs_chains['Narrator']))
    print(generate_sentence(dialogs_chains['Spike']))
    print(generate_sentence(dialogs_chains['Twilight Sparkle']))
    print(generate_sentence(dialogs_chains['Everypony']))
    print(generate_sentence(dialogs_chains['Applejack']))
    # print(dialogs_chains['Narrator'].rows.keys())
    # print(dialogs_chains['Narrator'].get_weighted([None, None, None]))
    # participant_order_chain = train_participant_order(csv_path)

    # author = 'Others'
    # for _ in range(10):
    #     sentence = generate_sentence(dialogs_chains[author])
    #     dialog_line = "{}: {}".format(author.upper(), sentence)

    #     print('

    #     author = participant_order_chain.generate_new_value(prev)

