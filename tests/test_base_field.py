import pytest

from tests.conftest import mock_base_field_input, mock_base_field_output
from bigquery_orm.base.field import BaseField


def test_base_field_instance_with_success(mock_base_field_input, mock_base_field_output):
    base_field = BaseField(**mock_base_field_input)
    assert base_field.properties == mock_base_field_output


def test_base_field_instance_with_error(mock_base_field_input):
    field = mock_base_field_input.copy()
    field.pop("name")

    with pytest.raises(TypeError) as error:
        BaseField(**field)

    assert "missing 1 required positional argument: 'name'" in error.value.args[0]
