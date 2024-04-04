from abc import ABC,abstractmethod

class data_extract_strategy(ABC):
    @abstractmethod
    def extract(self,data):
        pass
