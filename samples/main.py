from samples.client_bigquery import client

from samples.create_table_dataclass import create_table_dataclass
from samples.create_table_pydantic import create_table_pydantic
from samples.create_table_sqlalchemy import create_table_sqlalchemy


if __name__ == "__main__":
    create_table_dataclass(client=client)
    create_table_pydantic(client=client)
    create_table_sqlalchemy(client=client)
