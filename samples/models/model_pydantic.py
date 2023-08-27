from pydantic import BaseModel, Field


class UserPydantic(BaseModel):
    __tablename__ = 'user'
    __table_id__ = 'bigquery-orm.dataset.user'

    id: int
    email: str = Field(default=None, description="Customer Contact")
