from bigquery_orm.base.bigquery import Mode
from bigquery_orm.modules.sqlalchemy.translator import TranslatorSQLAlchemy as TR


def test_translator_sqlalchemy_get_mode_required():
    assert TR._mode(value=False) == Mode.REQUIRED


def test_translator_sqlalchemy_get_mode_nullable():
    assert TR._mode(value=True) == Mode.NULLABLE
