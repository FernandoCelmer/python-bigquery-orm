from abc import ABC, abstractmethod
from typing import List


class BaseManager(ABC):

    def __init__(self, model_class: object):
        self.model_class = model_class
        self.keys = self.load_keys()
        self.map = self.load_map()

    @abstractmethod
    def load_keys(self) -> List[str]:
        pass

    @abstractmethod
    def load_map(self):
        pass

    @abstractmethod
    def translator(self, field: str, detail: object):
        pass
