from dataclasses import dataclass


@dataclass
class UserDataClass:
    __tablename__ = 'user'
    __table_id__ = 'bigquery-orm.dataset.user'

    id: int
    email: str
