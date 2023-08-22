class Defaul:
    ...


try:
    from pydantic import BaseModel
    from sqlalchemy.orm.decl_api import DeclarativeMeta
except Exception:
    BaseModel = Defaul
    DeclarativeMeta = Defaul
