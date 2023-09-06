from bigquery_orm.base.field import BaseField
from bigquery_orm.base.manager import BaseManager
from bigquery_orm.modules.sqlalchemy.translator import TranslatorSQLAlchemy as TR


class SQLAlchemy(BaseManager):

    def _load_keys(self):
        return self.model_class.__table__.columns.keys()

    def _load_map(self):
        mapping = []
        for field in self.model_class.__table__.columns:
            mapping.append(
                self._translator(
                    field=field.name,
                    detail=field
                )
            )
        return mapping

    def _translator(self, field: str, detail: object) -> BaseField:
        description = getattr(self.model_class, field).comment or detail.description

        schema = BaseField(
            name=field,
            field_type=TR._type(detail.type.__class__),
            mode=TR._mode(detail.nullable),
            description=description,
            max_length=None
        )
        return schema.properties
