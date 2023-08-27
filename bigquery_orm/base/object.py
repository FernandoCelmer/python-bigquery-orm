class QueryFilter:

    def all(self):
        pass

    def first(self):
        pass

    def order_by(self):
        pass


class Query:

    def filter(self):
        pass


class Delete:
    ...


class Insert:
    ...


class Update:
    ...


class Object:

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
