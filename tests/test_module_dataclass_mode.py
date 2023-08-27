from bigquery_orm.base.bigquery import Mode

from dataclasses import _MISSING_TYPE
from bigquery_orm.modules.dataclass.translator import TranslatorDataClass as TR


def test_translator_dataclass_get_mode_required():
    assert TR._mode(value=_MISSING_TYPE) == Mode.REQUIRED


def test_translator_dataclass_get_mode_nullable():
    assert TR._mode(value=object) == Mode.NULLABLE
