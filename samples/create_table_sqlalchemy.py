from google.cloud.bigquery import Client

from bigquery_orm import Table

from samples import UserSQLAlchemy
from samples.client_bigquery import client


def create_table_sqlalchemy(client: Client = client) -> None:
    table = Table(model_class=UserSQLAlchemy, client=client)
    table.create()
