from google.cloud import bigquery
from google.oauth2.service_account import Credentials

from bigquery_orm import Table

from samples.model_sqlalchemy import UserSQLAlchemy
from samples.model_pydantic import UserPydantic
from samples.model_dataclass import UserDataClass


client = bigquery.Client(credentials=Credentials.from_service_account_file(
        filename="./credentials.json"
    )
)


schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("email", "STRING", mode="NULLABLE"),
]

# Tests
table_1 = Table(UserSQLAlchemy)
table_2 = Table(UserPydantic)
table_3 = Table(UserDataClass)
