from bigquery_orm._internal import (
    PydanticBaseModel as BaseModel,
    PydanticField as Field
)


class UserPydantic(BaseModel):
    __tablename__ = 'user'
    __table_id__ = 'bigquery-orm.dataset.user'

    id: int
    email: str = Field(default=None, description="Customer Contact")
