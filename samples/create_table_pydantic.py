from google.cloud.bigquery import Client

from bigquery_orm import Table
from samples import UserPydantic


def create_table_pydantic(client: Client) -> None:
    table = Table(model_class=UserPydantic, client=client)
    table.create()
