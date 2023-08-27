from abc import ABC, abstractclassmethod
from typing import Any

from bigquery_orm.base.bigquery import Type, Mode


class BaseTranslator(ABC):

    @abstractclassmethod
    @staticmethod
    def _type(value: Any) -> Type:
        pass

    @abstractclassmethod
    @staticmethod
    def _mode(value: Any) -> Mode:
        pass
