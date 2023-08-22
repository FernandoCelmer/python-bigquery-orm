from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserSQLAlchemy(Base):
    __tablename__ = 'user'
    __table_id__ = 'bigquery-orm.dataset.user'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=True)
