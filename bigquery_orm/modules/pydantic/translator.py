import typing

from typing import Any
from bigquery_orm.base.bigquery import Mode, Type


class TranslatorPydantic:

    @staticmethod
    def _type(value: Any):
        objects = {
            int: Type.INTEGER,
            str: Type.STRING,
            typing.Optional[int]: Type.INTEGER,
            typing.Optional[str]: Type.STRING,
        }
        return objects.get(value)

    @staticmethod
    def _mode(value: Any):
        objects = {
            True: Mode.REQUIRED,
            False: Mode.NULLABLE
        }
        return objects.get(value)
