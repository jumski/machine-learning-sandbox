import numpy

class MarkovChain:
    def __init__(self):
        self.rows = {}

    def add_transition(self, from_value, to_value):
        row_key = tuple(from_value)

        if row_key not in self.rows:
            self.rows[row_key] = {}
        row = self.rows[row_key]

        if to_value not in row:
            row[to_value] = 0

        row[to_value] += 1

    def get_possibilities(self, from_value):
        row_key = tuple(from_value)

        return self.rows[row_key]

    def get_weighted(self, from_value):
        row_key = tuple(from_value)
        row = self.rows[row_key]

        total = sum(row.values())
        weights = {}

        for to_value in row:
            weights[to_value] = row[to_value] / total

        return weights

    def generate_new_value(self, from_value):
        weighted = self.get_weighted(from_value)

        possibilities = list(weighted.keys())
        weights = list(weighted.values())

        return numpy.random.choice(possibilities, p=weights)

