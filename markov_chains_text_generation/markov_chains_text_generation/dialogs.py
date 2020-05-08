import csv

def read_dialogs(csv_path):
    csv_file = open(csv_path, 'r')
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    next(reader) # skip the header

    # "title","writer","pony","dialog" for each row
    return reader
