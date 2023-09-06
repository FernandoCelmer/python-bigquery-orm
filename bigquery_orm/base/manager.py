from abc import ABC, abstractmethod
from typing import List, Optional


class BaseManager(ABC):

    def __init__(self, model_class: object, client: object = None):
        self.model_class = model_class
        self.client = client

        self.keys = self._load_keys()
        self.map = self._load_map()

    @abstractmethod
    def _load_keys(self) -> List[str]:
        pass

    @abstractmethod
    def _load_map(self):
        pass

    @abstractmethod
    def _translator(self, field: str, detail: object):
        pass

    def create(self, table_id: Optional[str] = None) -> None:
        return "Method not Implemented"

    def delete(self) -> None:
        return "Method not Implemented"
