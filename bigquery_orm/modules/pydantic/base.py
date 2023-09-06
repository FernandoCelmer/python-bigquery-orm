from bigquery_orm.base.manager import BaseManager
from bigquery_orm.base.field import BaseField
from bigquery_orm.modules.pydantic.translator import TranslatorPydantic as TR


class Pydantic(BaseManager):

    def _load_keys(self):
        return [item[0] for item in self.model_class.model_fields.items()]

    def _load_map(self):
        mapping = []
        for field in self.model_class.model_fields:
            mapping.append(
                self._translator(
                    field=field,
                    detail=self.model_class.model_fields[field]
                )
            )
        return mapping

    def _translator(self, field: str, detail: object) -> BaseField:
        description = detail.description or field

        schema = BaseField(
            name=field,
            field_type=TR._type(detail.annotation),
            mode=TR._mode(detail.is_required()),
            description=description,
            max_length=None
        )
        return schema.properties
