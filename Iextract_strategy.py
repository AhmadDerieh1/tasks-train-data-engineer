from abc import ABC, abstractmethod
class data_extract_strategy(ABC):
    @abstractmethod
    def parser_data(self, data):
        pass
