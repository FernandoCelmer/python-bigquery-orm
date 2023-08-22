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
        str: BigQueryType.STRING
    }

    _mode = {
        True: BigQueryMode.REQUIRED,
        False: BigQueryMode.NULLABLE
    }


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

    _mode = {
        True: BigQueryMode.REQUIRED,
        False: BigQueryMode.NULLABLE
    }


class DataClass:

    _type = {
        int: BigQueryType.INTEGER,
        str: BigQueryType.STRING
    }

    _mode = {
        True: BigQueryMode.REQUIRED,
        False: BigQueryMode.NULLABLE
    }
