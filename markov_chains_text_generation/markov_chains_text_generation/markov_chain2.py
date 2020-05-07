from pandas import DataFrame

class MarkovChain2:
    def __init__(self):
        self._data = DataFrame()

    @property
    def data(self):
        return self._data;
