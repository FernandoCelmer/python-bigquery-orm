from typing import Any

from bigquery_orm.base.bigquery import Type, Mode
from bigquery_orm.base.translator import BaseTranslator


class BaseTranslatorTest(BaseTranslator):

    @staticmethod
    def _type(value: Any) -> Type:
        return True

    @staticmethod
    def _mode(value: Any) -> Mode:
        return True


def test_base_translator_instance():
    translator = BaseTranslatorTest()

    assert translator._type(value=object)
    assert translator._mode(value=object)


def test_base_manager_mode_instance():
    translator = BaseTranslatorTest()

    assert translator._mode(value=object)
    assert hasattr(BaseTranslator, "_mode")


def test_base_manager_type_instance():
    translator = BaseTranslatorTest()

    assert translator._type(value=object)
    assert hasattr(BaseTranslator, "_type")
