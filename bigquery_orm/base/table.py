import logging

from typing import Optional

from bigquery_orm._internal import BigQueryClient
from bigquery_orm.exception import ExceptionInvalidModel
from bigquery_orm.modules import DataClass, Pydantic, SQLAlchemy


class Table:

    def __init__(self, model_class: object, client: BigQueryClient):
        self.client = client
        try:
            if hasattr(model_class, "__dataclass_fields__"):
                self.handler = DataClass(model_class=model_class)

            elif model_class.__class__.__name__ == "ModelMetaclass":
                self.handler = Pydantic(model_class=model_class)

            elif model_class.__class__.__name__ == "DeclarativeMeta":
                self.handler = SQLAlchemy(model_class=model_class)

            else:
                raise ExceptionInvalidModel()

        except ExceptionInvalidModel as error:
            logging.error(error)

    def create(self, table_id: Optional[str] = None):
        pass

    def delete(self):
        pass
