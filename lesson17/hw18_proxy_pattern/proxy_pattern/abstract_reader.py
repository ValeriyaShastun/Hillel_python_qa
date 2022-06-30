from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def read_file(self):
        pass
