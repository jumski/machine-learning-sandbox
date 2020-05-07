from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self._rows = defaultdict(self._create_row)

    def add_occurence(self, from_val, to_val):
        self._rows[from_val][to_val] +=1

    def items(self):
        return self._rows.items();

    def _create_row(_):
        return defaultdict(lambda: 0)

