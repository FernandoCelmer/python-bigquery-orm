from tests.conftest import (
    mock_base_table_keys as keys,
    mock_base_table_mapping as mapping
)

from samples import UserPydantic
from bigquery_orm.modules.pydantic.base import Pydantic


def test_base_sqlalchemy_instance_keys(keys):
    table = Pydantic(model_class=UserPydantic)

    assert table.keys == keys


def test_base_sqlalchemy_instance_map(mapping):
    table = Pydantic(model_class=UserPydantic)

    assert table.map == mapping
