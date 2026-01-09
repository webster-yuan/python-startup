from pydantic import BaseModel, ConfigDict


class HeroCreate(BaseModel):
    name: str
    age: int | None = None
    secret_name: str


class ORMBase(BaseModel):
    # 允许 FastAPI 把 ORM 对象直接转 JSON
    # SQLModel 已经继承自 Pydantic，orm_mode 可以省，但写上更直观
    model_config = ConfigDict(from_attributes=True)


class HeroRead(ORMBase):
    id: int
    name: str
    age: int | None = None


class HeroSelect(BaseModel):
    id: int
