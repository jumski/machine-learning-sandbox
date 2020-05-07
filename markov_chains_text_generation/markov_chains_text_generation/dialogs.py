import csv

def dialogs_in_csv(csv_path):
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        next(reader) # skip the header

        for row in reader:
            yield row[3]
