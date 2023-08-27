from google.cloud.bigquery import Client

from bigquery_orm import Table

from samples import UserDataClass
from samples.client_bigquery import client


def create_table_dataclass(client: Client = client) -> None:
    table = Table(model_class=UserDataClass, client=client)
    table.create()
