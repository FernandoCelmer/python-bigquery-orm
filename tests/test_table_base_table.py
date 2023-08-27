
from tests.conftest import (
    mock_base_table_keys as keys,
    mock_base_table_mapping as mapping
)

from samples import UserDataClass, UserPydantic, UserSQLAlchemy
from bigquery_orm.base.table import BaseTable
from bigquery_orm.exception import ExceptionInvalidModel


def test_base_table_set_sqlalchemy_success(keys, mapping):
    table = BaseTable(model_class=UserSQLAlchemy)
    table.set_sqlalchemy()

    assert table.keys == keys
    assert table.mapping == mapping


def test_base_table_set_pydantic_success(keys, mapping):
    table = BaseTable(model_class=UserPydantic)
    table.set_pydantic()

    assert table.keys == keys
    assert table.mapping == mapping


def test_base_table_set_dataclass_success(keys, mapping):
    table = BaseTable(model_class=UserDataClass)
    table.set_dataclass()

    assert table.keys == keys
    assert table.mapping == mapping


def test_base_table_setup_dataclass_with_success():
    table = BaseTable(model_class=UserDataClass)
    table.__setup__()


def test_base_table_setup_pydantic_with_success():
    table = BaseTable(model_class=UserPydantic)
    table.__setup__()


def test_base_table_setup_sqlalchemy_with_success():
    table = BaseTable(model_class=UserSQLAlchemy)
    table.__setup__()


def test_base_table_setup_sqlalchemy_with_error(caplog):
    table = BaseTable(model_class=object)
    table.__setup__()

    assert isinstance(caplog.records[0].msg, ExceptionInvalidModel)
