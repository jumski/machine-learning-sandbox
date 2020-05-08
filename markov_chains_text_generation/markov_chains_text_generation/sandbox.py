from .data import csv_consecutive_tokens

csv_path = 'data/clean_dialog.csv'

def main():
    csv_file = open(csv_path, 'r')

    for *from_tokens,to_token in csv_consecutive_tokens(csv_file, 3):
        print(from_tokens, ' => ', to_token)
