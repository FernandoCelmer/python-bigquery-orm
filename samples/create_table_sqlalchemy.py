from google.cloud.bigquery import Client

from bigquery_orm import Table
from samples import UserSQLAlchemy


def create_table_sqlalchemy(client: Client) -> None:
    table = Table(model_class=UserSQLAlchemy, client=client)
    table.create()
