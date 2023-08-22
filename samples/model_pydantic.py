from pydantic import BaseModel, Field


class UserPydantic(BaseModel):
    __tablename__ = 'user'
    __table_id__ = 'bigquery-orm.dataset.user'

    id: int = Field(default=None)
    email: str = Field(default=None)
