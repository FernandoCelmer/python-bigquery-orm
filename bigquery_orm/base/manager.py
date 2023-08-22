from abc import ABC, abstractmethod


class BaseManager(ABC):

    def __init__(self, model_class):
        self.model_class = model_class
        self.keys = []
        self.mapping = []

        self.__setup__()

    @abstractmethod
    def __setup__(self):
        pass
