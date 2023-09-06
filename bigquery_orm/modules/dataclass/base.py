from bigquery_orm.base.field import BaseField
from bigquery_orm.base.manager import BaseManager
from bigquery_orm.modules.dataclass.translator import TranslatorDataClass as TR


class DataClass(BaseManager):

    def _load_keys(self):
        return [item for item in self.model_class.__dataclass_fields__]

    def _load_map(self):
        mapping = []
        for field in self.model_class.__dataclass_fields__:
            mapping.append(
                self._translator(
                    field=field,
                    detail=self.model_class.__dataclass_fields__[field]
                )
            )
        return mapping

    def _translator(self, field: str, detail: object) -> BaseField:
        description = detail.metadata.get("description") or field

        schema = BaseField(
            name=field,
            field_type=TR._type(detail.type),
            mode=TR._mode(detail.default.__class__),
            description=description,
            max_length=None
        )
        return schema.properties
