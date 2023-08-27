from abc import ABC, abstractclassmethod
from typing import Any

from bigquery_orm.base.bigquery import Type, Mode


class BaseTranslator(ABC):

    @staticmethod
    @abstractclassmethod
    def _type(value: Any) -> Type:
        pass

    @staticmethod
    @abstractclassmethod
    def _mode(value: Any) -> Mode:
        pass
