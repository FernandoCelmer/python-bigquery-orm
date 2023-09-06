from bigquery_orm.base.table import BaseTable
from bigquery_orm.exception import ExceptionInvalidModel
from samples import UserDataClass, UserPydantic, UserSQLAlchemy


def test_base_table_dataclass_instance_success():
    table = BaseTable(model_class=UserDataClass)

    assert table.model_class == UserDataClass


def test_base_table_pydantic_instance_success():
    table = BaseTable(model_class=UserPydantic)

    assert table.model_class == UserPydantic


def test_base_table_sqlalchemy_instance_success():
    table = BaseTable(model_class=UserSQLAlchemy)

    assert table.model_class == UserSQLAlchemy


def test_base_table_instance_error(caplog):
    BaseTable(model_class=object)

    assert isinstance(caplog.records[0].msg, ExceptionInvalidModel)
