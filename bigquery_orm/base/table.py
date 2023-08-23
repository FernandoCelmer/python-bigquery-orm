import logging

from typing import Dict, Any

from bigquery_orm.base.manager import BaseManager
from bigquery_orm.base.translator import Pydantic, SQLAlchemy, DataClass
from bigquery_orm.exception import ExceptionInvalidDataClass


class BaseField:

    def __init__(
        self,
        name: str,
        field_type: str,
        mode: str,
        description: str,
        max_length: int
    ) -> None:
        self.properties: Dict[str, Any] = {
            "name": name,
            "type": field_type,
            "mode": mode,
            "description": description,
            "max_length": max_length
        }


class BaseTable(BaseManager):

    def __init__(self, model_class):
        super().__init__(model_class)
        self.keys = []
        self.mapping = []

    def __setup__(self):
        try:
            if self.model_class.__class__.__name__ == "DeclarativeMeta":
                self.set_sqlalchemy()

            elif self.model_class.__class__.__name__ == "ModelMetaclass":
                self.set_pydantic()

            elif hasattr(self.model_class, "__dataclass_fields__"):
                self.set_dataclass()

            else:
                raise ExceptionInvalidDataClass()

        except ExceptionInvalidDataClass as error:
            logging.error(error)

    def set_sqlalchemy(self):
        self.keys = self.model_class.__table__.columns.keys()

        for field in self.model_class.__table__.columns:
            self.mapping.append(
                self.translator_sqlalchemy(
                    field=field.name,
                    detail=field
                )
            )

    def set_pydantic(self):
        self.keys = [item[0] for item in self.model_class.model_fields.items()]

        for field in self.model_class.model_fields:
            self.mapping.append(
                self.translator_pydantic(
                    field=field,
                    detail=self.model_class.model_fields[field]
                )
            )

    def set_dataclass(self):
        self.keys = [item for item in self.model_class.__dataclass_fields__]

        for field in self.model_class.__dataclass_fields__:
            self.mapping.append(
                self.translator_dataclass(
                    field=field,
                    detail=self.model_class.__dataclass_fields__[field]
                )
            )

    def translator_sqlalchemy(self, field: str, detail: object):
        description = getattr(self.model_class, field).comment or detail.description

        schema = BaseField(
            name=field,
            field_type=SQLAlchemy._type.get(detail.type.__class__),
            mode=SQLAlchemy._mode(detail.nullable),
            description=description,
            max_length=None
        )
        return schema.properties

    def translator_pydantic(self, field: str, detail: object):
        description = detail.description or field

        schema = BaseField(
            name=field,
            field_type=Pydantic._type.get(detail.annotation),
            mode=Pydantic._mode(detail.is_required()),
            description=description,
            max_length=None
        )
        return schema.properties

    def translator_dataclass(self, field: str, detail: object):
        description = detail.metadata.get("description") or field

        schema = BaseField(
            name=field,
            field_type=DataClass._type.get(detail.type),
            mode=DataClass._mode(detail.default.__class__),
            description=description,
            max_length=None
        )
        return schema.properties


class Table(BaseTable):

    def __init__(self, model_class):
        super().__init__(model_class)
        self.setup__()

    def create(self):
        pass

    def delete(self):
        pass
