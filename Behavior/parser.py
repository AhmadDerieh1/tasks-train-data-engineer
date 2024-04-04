from Iextract_strategy import data_extract_strategy
class parser:
    def __init__(self, strategy: data_extract_strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: data_extract_strategy):
        self._strategy = strategy

    def parser_data(self, data):
        return self._strategy.parser_data(data)