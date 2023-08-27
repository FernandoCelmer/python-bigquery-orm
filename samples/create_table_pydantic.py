from google.cloud.bigquery import Client

from bigquery_orm import Table

from samples import UserPydantic
from samples.client_bigquery import client


def create_table_pydantic(client: Client = client) -> None:
    table = Table(model_class=UserPydantic, client=client)
    table.create()
