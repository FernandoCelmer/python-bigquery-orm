from abc import ABC


class BaseManager(ABC):

    def __init__(self, model_class):
        self.model_class = model_class
