from google.cloud.bigquery import Client
from google.oauth2.service_account import Credentials


client = Client(credentials=Credentials.from_service_account_file(
        filename="./credentials.json"
    )
)
