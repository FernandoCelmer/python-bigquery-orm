from google.cloud.bigquery import Client

from bigquery_orm import Table
from samples import UserDataClass


def create_table_dataclass(client: Client) -> None:
    table = Table(model_class=UserDataClass, client=client)
    table.create()
