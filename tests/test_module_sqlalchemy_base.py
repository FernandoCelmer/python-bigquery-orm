from tests.conftest import (
    mock_base_table_keys as keys,
    mock_base_table_mapping as mapping
)

from samples import UserSQLAlchemy
from bigquery_orm.modules.sqlalchemy.base import SQLAlchemy


def test_base_sqlalchemy_instance_keys(keys):
    table = SQLAlchemy(model_class=UserSQLAlchemy)

    assert table.keys == keys


def test_base_sqlalchemy_instance_map(mapping):
    table = SQLAlchemy(model_class=UserSQLAlchemy)

    assert table.map == mapping
