from Iextract_strategy import DataExtractionStrategy
class DataProcessor:
    def __init__(self, strategy: DataExtractionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DataExtractionStrategy):
        self._strategy = strategy

    def process_data(self, data):
        return self._strategy.process_data(data)