from bigquery_orm.base.manager import BaseManager


class QueryFilter(BaseManager):

    def all(self):
        pass

    def first(self):
        pass

    def order_by(self):
        pass


class Query(BaseManager):

    def filter(self):
        pass


class Delete(BaseManager):
    ...


class Insert(BaseManager):
    ...


class Update(BaseManager):
    ...


class Object(BaseManager):

    def query(self, *args, **kwargs):
        return Query(
            model_class=self.model_class
        )

    def delete(self, *args, **kwargs):
        return Delete(
            model_class=self.model_class
        )

    def insert(self, *args, **kwargs):
        return Insert(
            model_class=self.model_class
        )

    def update(self, *args, **kwargs):
        return Update(
            model_class=self.model_class
        )
