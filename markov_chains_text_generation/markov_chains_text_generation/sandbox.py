from .data import csv_consecutive_tokens

csv_path = 'data/clean_dialog.csv'

def main():
    csv_file = open(csv_path, 'r')

    for tokens in csv_consecutive_tokens(csv_file, 3):
        print(tokens)
