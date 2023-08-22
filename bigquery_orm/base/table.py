import logging

from typing import Dict, Any

from bigquery_orm.base.manager import BaseManager
from bigquery_orm.base.bigquery import Pydantic, SQLAlchemy, DataClass


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

    def __setup__(self):
        class_name = self.model_class.__class__.__name__
        try:
            if class_name == "DeclarativeMeta":
                self.__set_keys_sqlalchemy()

            if class_name == "ModelMetaclass":
                self.__set_keys_pydantic()

            if class_name == "type":
                self.__set_keys_dataclass()

        except Exception as error:
            logging.error(error)

    def __set_keys_sqlalchemy(self):
        self.keys = self.model_class.__table__.columns.keys()

        for field in self.model_class.__table__.columns:
            self.mapping.append(
                self.__translator_sqlalchemy(
                    field=field.name,
                    detail=field
                )
            )

    def __set_keys_pydantic(self):
        self.keys = [item[0] for item in self.model_class.model_fields.items()]

        for field in self.model_class.model_fields:
            self.mapping.append(
                self.__translator_pydantic(
                    field=field,
                    detail=self.model_class.model_fields[field]
                )
            )

    def __set_keys_dataclass(self):
        self.keys = [item for item in self.model_class.__annotations__]

        for field in self.model_class.__annotations__:
            self.mapping.append(
                self.__translator_dataclass(
                    field=field,
                    detail=self.model_class.__annotations__[field]
                )
            )

    def __translator_sqlalchemy(self, field: str, detail: object):
        schema = BaseField(
            name=field,
            field_type=SQLAlchemy._type.get(detail.type.__class__),
            mode=SQLAlchemy._type.get(detail.nullable),
            description=detail.description,
            max_length=None
        )
        return schema.properties

    def __translator_pydantic(self, field: str, detail: object):
        schema = BaseField(
            name=field,
            field_type=Pydantic._type.get(detail.annotation),
            mode=Pydantic._type.get(detail.is_required()),
            description=detail.description,
            max_length=None
        )
        return schema.properties

    def __translator_dataclass(self, field: str, detail: object):
        schema = BaseField(
            name=field,
            field_type=DataClass._type.get(detail),
            mode=False,
            description=None,
            max_length=None
        )
        return schema.properties


class Table(BaseTable):

    def create(self):
        pass

    def delete(self):
        pass
