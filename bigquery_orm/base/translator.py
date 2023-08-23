import typing

from typing import Any

from dataclasses import _MISSING_TYPE
from bigquery_orm._internal import Defaul


class BigQueryMode:

    REQUIRED = "REQUIRED"
    REPEATED = "REPEATED"
    NULLABLE = "NULLABLE"


class BigQueryType:

    STRING = "STRING"
    BYTES = "BYTES"
    INTEGER = "INTEGER"
    INT64 = "INTEGER"
    FLOAT = "FLOAT"
    FLOAT64 = "FLOAT"
    DECIMAL = "NUMERIC"
    BIGDECIMAL = "BIGNUMERIC"
    BOOLEAN = "BOOLEAN"
    BOOL = "BOOLEAN"
    GEOGRAPHY = "GEOGRAPHY"
    RECORD = "RECORD"
    STRUCT = "RECORD"
    TIMESTAMP = "TIMESTAMP"
    DATE = "DATE"
    TIME = "TIME"
    DATETIME = "DATETIME"


class Pydantic:

    _type = {
        int: BigQueryType.INTEGER,
        str: BigQueryType.STRING,
        typing.Optional[str]: BigQueryType.INTEGER,
        typing.Optional[int]: BigQueryType.STRING,
    }

    @staticmethod
    def _mode(value: Any):
        return {
            True: BigQueryMode.REQUIRED,
            False: BigQueryMode.NULLABLE
        }.get(value)


class SQLAlchemy:

    try:
        from sqlalchemy import Integer, String
    except Exception:
        Integer = Defaul
        String = Defaul

    _type = {
        Integer: BigQueryType.INTEGER,
        String: BigQueryType.STRING
    }

    @staticmethod
    def _mode(value: Any):
        return {
            False: BigQueryMode.REQUIRED,
            True: BigQueryMode.NULLABLE
        }.get(value)
 

class DataClass:

    _type = {
        str: BigQueryType.STRING,
        int: BigQueryType.INTEGER,
        typing.Optional[str]: BigQueryType.STRING,
        typing.Optional[int]: BigQueryType.STRING,
    }

    @staticmethod
    def _mode(value: Any):
        return {
            _MISSING_TYPE: BigQueryMode.REQUIRED
        }.get(value, BigQueryMode.NULLABLE)
