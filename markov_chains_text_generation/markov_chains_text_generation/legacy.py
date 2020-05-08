
from nltk.tokenize.treebank import TreebankWordDetokenizer



# def main3():
    # def is_terminated(sentence):
        # return sentence[-1] in set(['.', '?', '!'])
#     csv_file = open(csv_path, 'r')
#     window = 3
#     chains = {}

#     chain = MarkovChain()
#     print('Building markov chain...')
#     for *from_tokens, to_token in csv_consecutive_tokens(csv_file, window + 1):
#         chain.add_transition(from_tokens, to_token)

#     sentence = ['What', 'if', 'you']

#     print()

#     while not is_terminated(sentence):
#         input_tokens = sentence[-window:]
#         new_token = chain.generate_new_value(input_tokens)
#         sentence.append(new_token)

#     print(TreebankWordDetokenizer().detokenize(sentence))
