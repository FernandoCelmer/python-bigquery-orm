from typing import Any

from bigquery_orm._internal import SQLAlchemyInteger, SQLAlchemyString
from bigquery_orm.base.bigquery import Mode, Type


class TranslatorSQLAlchemy:

    @staticmethod
    def _type(value: Any):
        objects = {
            SQLAlchemyInteger: Type.INTEGER,
            SQLAlchemyString: Type.STRING
        }
        return objects.get(value)

    @staticmethod
    def _mode(value: Any):
        objects = {
            False: Mode.REQUIRED,
            True: Mode.NULLABLE
        }
        return objects.get(value)
