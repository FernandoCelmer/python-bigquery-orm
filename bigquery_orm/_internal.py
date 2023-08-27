class Defaul:
    ...


try:
    from pydantic import BaseModel as PydanticBaseModel
except Exception:
    PydanticBaseModel = Defaul


try:
    from sqlalchemy.orm.decl_api import (
        DeclarativeMeta as SQLAlchemyDeclarativeMeta
    )
    from sqlalchemy import (
        Integer as SQLAlchemyInteger,
        String as SQLAlchemyString
    )
except Exception:
    SQLAlchemyDeclarativeMeta = Defaul
    SQLAlchemyInteger = Defaul
    SQLAlchemyString = Defaul
