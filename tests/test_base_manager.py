from typing import List
from bigquery_orm.base.manager import BaseManager


class BaseManagerTest(BaseManager):

    def _load_keys(self) -> List[str]:
        return True

    def _load_map(self):
        return True

    def _translator(self, field: str, detail: object):
        return True


def test_base_manager_instance():
    manager = BaseManagerTest(model_class=object)

    assert manager.keys is True
    assert manager.map is True
    assert isinstance(manager.model_class, object)


def test_base_manager_load_keys_attr():
    manager = BaseManagerTest(model_class=object)

    assert manager._load_keys()
    assert hasattr(BaseManager, "_load_keys")


def test_base_manager_load_map_attr():
    manager = BaseManagerTest(model_class=object)

    assert manager._load_map()
    assert hasattr(BaseManager, "_load_map")


def test_base_manager_translator_attr():
    manager = BaseManagerTest(model_class=object)

    assert manager._translator(field="id", detail=object)
    assert hasattr(BaseManager, "_translator")
