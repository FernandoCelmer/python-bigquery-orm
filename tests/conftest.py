import pytest


@pytest.fixture
def mock_base_field_input():
    return {
        "name": "id",
        "field_type": "INTEGER",
        "mode": "NULLABLE",
        "description": "My ID",
        "max_length": None
    }


@pytest.fixture
def mock_base_field_output():
    return {
        "name": "id",
        "type": "INTEGER",
        "mode": "NULLABLE",
        "description": "My ID",
        "max_length": None
    }


@pytest.fixture
def mock_base_table_keys():
    return ['id', 'email']


@pytest.fixture
def mock_base_table_mapping():
    return [
        {
            'name': 'id',
            'type': 'INTEGER',
            'mode': 'REQUIRED',
            'description': 'id',
            'max_length': None
        },
        {
            'name': 'email',
            'type': 'STRING',
            'mode': 'NULLABLE',
            'description': 'Customer Contact',
            'max_length': None
        }
    ]
